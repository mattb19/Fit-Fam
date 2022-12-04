<style scoped>
.button {
  margin-top: 50px;
  width: 50em;
  padding-right: 500px;
}

.image {
  margin: auto;
  width: 50em;
}

.description {
  margin: auto;
  height: auto;
  width: auto;
}

form {
  max-width: 52.6em;
}

.btn {
  width: 50em;
}

.tags {
  margin: auto;
  margin-right: 10px;
}

.tag {
  text-align: center;
  width: 100px;
}

.p {
  margin-bottom: 0px;
  color: red;
}

.red {
  color: red;
}

.accept {
  color: red;
}

.bad {
  color: red;
}
</style>

<template>
  <div class="searchView">
    <navBar></navBar>
    <h1 class="header">NEW POST</h1>
    <div class="form-group">
      <div class="title">
        <input
          name="title"
          type="text"
          class="title"
          placeholder="Title"
          required
          size="80"
          id="title"
          v-model="title"
        />
      </div>
    </div>
    <div class="form-group center-align">
      <div class="description">
        <textarea
          name="description"
          placeholder="Description"
          required
          class="description"
          id="description"
          rows="10"
          cols="80"
          v-model="description"
        />
      </div>
    </div>
    <label for="tags" class="tags">Choose a tag:</label>
    <select name="tags" id="tags" class="tag" v-model="tags">
      <option value="Back" class="tag">Back</option>
      <option value="Chest" class="tag">Chest</option>
      <option value="Arms" class="tag">Arms</option>
      <option value="Legs" class="tag">Legs</option>
      <option value="Back/Bicep" class="tag">Back/Bicep</option>
      <option value="Chest/Tricep" class="tag">Chest/Tricep</option>
      <option value="Full Body" class="tag">Full Body</option>
    </select>
    <div>
      <input
        class="image"
        type="file"
        id="avatar"
        name="avatar"
        accept="image/png, image/jpeg, image/jpg"
        ref="image"
        @change="blobIt"
      />
      <p>Images must be jpeg, jpg or png format</p>

      <div class="button">
        <button
          @submit="createPost"
          type="button"
          class="btn btn-dark"
          href="/"
          v-on:click="createPost"
        >
          Post
        </button>
      </div>
      <p class="accept">{{ this.acceptance }}</p>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import NavBarComponent from "./NavBarComponent.vue";

export default {
  data() {
    return {
      backend: "",
      title: "",
      description: "",
      image: "",
      tags: "",
      acceptance: "",
      good: "",
    };
  },
  components: {
    navBar: NavBarComponent,
  },
  methods: {
    checkLoggedIn() {
      if (localStorage.getItem("id") === null) {
        this.$router.push({ name: "login" });
      }
    },
    logout() {
      localStorage.clear();
      this.$router.push({ name: "login" });
    },
    getStats() {
      const path = "http://127.0.0.1:5000/posts";
      axios
        .get(path)
        .then((res) => {
          this.backend = res.data;
        })
        .catch((err) => {
          console.error(err);
        });
    },
    blobIt() {
      this.image = this.$refs.image.files[0];
    },
    yup(img) {
      return new Promise((resolve, reject) => {
        const reader = new FileReader();
        reader.onerror = reject;
        reader.onload = () => {
          resolve(reader.result);
        };
        reader.readAsDataURL(img);
      });
    },
    async createPost() {
      const path = "http://127.0.0.1:5000/post";
      const formData = new FormData();
      formData.append("file", this.image);
      let blob;
      if (this.image != "") {
        blob = await this.yup(this.image);
      }

      if (this.title == "" || this.description == "") {
        this.acceptance = "Please complete all required * fields";
        this.good = "bad";
      } else {
        axios
          .post(path, {
            title: this.title,
            description: this.description,
            userId:
              localStorage.getItem("id") /*this should be a number no a name*/,
            tags: this.tags,
            image: blob,
          })
          .then((res) => {
            console.log(res);
          })
          .catch((error) => {
            console.log(error);
          });
        this.$router.push({ name: "home" });
      }
    },
    userProfile() {
      this.$router.push({
        name: "profile",
        params: { id: localStorage.getItem("id") },
      });
    },
  },
  created() {
    this.getStats();
    setTimeout(() => {
      this.checkLoggedIn();
    }, 1);
  },
};
</script>

<style scoped>
.addmargin {
  margin-top: 10px;
  margin-bottom: 10px;
}

.home {
  background-color: #383c44;
}

.button {
  margin-top: 50px;
}

.image {
  margin: auto;
  width: 50em;
}

.title {
  margin: auto;
  width: 50em;
}

.description {
  margin: auto;
  width: 50em;
}

.header {
  margin-top: 20px;
}

.btn {
  width: 50em;
}

.types {
  margin: auto;
  width: 50em;
  text-align: left;
}

.form-check {
  margin: auto;
}

.tags {
  margin: auto;
  margin-right: 10px;
}

.tag {
  text-align: center;
  width: 100px;
}
</style>

<template>
  <div class="searchView">
    <link
      rel="stylesheet"
      href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/materia/bootstrap.min.css"
      integrity="sha384-B4morbeopVCSpzeC1c4nyV0d0cqvlSAfyXVfrPJa25im5p+yEN/YmhlgQP/OyMZD"
      crossorigin="anonymous"
    />
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <div class="container-fluid">
        <a class="navbar-brand" href="http://localhost:8080/home">FitFam</a>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarColor02"
          aria-controls="navbarColor02"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarColor02">
          <ul class="navbar-nav me-auto">
            <li class="nav-item">
              <a class="nav-link" href="/home">Global</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="/groups">Groups</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="/profile">Profile</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="/search">Search</a>
            </li>
            <li class="nav-item">
              <button @click="logout">Logout</button>
            </li>
          </ul>
        </div>
      </div>
    </nav>
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
    </div>
    <p class="types">Image must be jpg, jpeg, or png</p>
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
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      backend: "",
      title: "",
      description: "",
      image: "",
      tags: "",
    };
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
        console.log(blob);
      }

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

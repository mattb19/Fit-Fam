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
        <a class="navbar-brand" href="http://localhost:8080/">FitFam</a>
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
              <a class="nav-link" href="/">Global</a>
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
              <a class="nav-link" href="/signup">Sign Up</a>
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
    };
  },
  methods: {
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
      let file = this.$refs.image.files[0];
      let reader = new FileReader();
      reader.onloadend = function () {
        document.write(reader.result);
      };
      this.image = reader.readAsDataURL(file);
      console.log(this.image);
    },
    createPost() {
      const path = "http://127.0.0.1:5000/post";
      const formData = new FormData();
      formData.append("file", this.image);
      console.log(this.image);
      const fileInput = document.querySelector("input[type=file]");
      const path1 = fileInput.value;
      const fileName = path1.split(/(\\|\/)/g).pop();

      axios
        .post(path, {
          title: this.title,
          imagePath: fileName,
          description: this.description,
          userId: "John J Jacobson",
          tags: "Legs, Arms",
          image: this.image,
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
  },
};
</script>

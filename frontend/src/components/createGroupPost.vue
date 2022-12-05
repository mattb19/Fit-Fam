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
              <a class="nav-link" @click="userProfile">Profile</a>
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
    <div>
      <input
        class="image"
        type="file"
        id="avatar"
        name="avatar"
        accept="image/png, image/jpeg"
        ref="image"
        @change="selectFile"
      />
    </div>
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
      groupId: 2,
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
    selectFile() {
      this.image = this.$refs.image.files[0];
    },
    createPost() {
      console.log({
        title: this.title,
      });
      const path = "http://127.0.0.1:5000/group_post";
      const formData = new FormData();
      formData.append("file", this.file);
      axios
        .post(path, {
          title: this.title,
          image: "../assets/post-button.png",
          description: this.description,
          userId: "John J Jacobson",
          tags: "Legs, Arms",
        })
        .then((res) => {
          console.log(res);
        })
        .catch((error) => {
          console.log(error);
        });
      this.$router.push({ name: "home" });
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
    }, 200);
  },
};
</script>

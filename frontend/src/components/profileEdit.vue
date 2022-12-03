<style scoped>
.addmargin {
  margin-top: 10px;
  margin-bottom: 10px;
}

.home {
  background-color: #383c44;
}

.example {
  width: 20%;
  height: 50%;
  max-height: 100%;
  border: 2px solid #488084;
}

input {
  width: 100%;
  height: 10px;
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
    <p></p>
    <p></p>
    <form @submit="save" class="profile">
      <h1>{{ backend.realName }}</h1>
      <label for="nickName">What do you want your nickname to be</label>
      <input
        type="text"
        id="nickName"
        name="nickName"
        required
        v-model="nickName"
      />
      <label for="aboutMe">What do you want in your about me</label>
      <input
        type="text"
        id="aboutMe"
        name="aboutMe"
        required
        v-model="aboutMe"
      />
      <div class="button">
        <button class="submit" type="submit">Save</button>
        <button @click="cancel">Cancel</button>
      </div>
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      backend: "",
      nickName: "",
      aboutMe: "",
    };
  },
  methods: {
    checkLoggedIn() {
      if (localStorage.getItem("id") === null) {
        this.$router.push({ name: "login" });
      }
    },
    getStats() {
      const path = "http://127.0.0.1:5000/profileEdit";
      axios
        .post(path, {
          userId: localStorage.getItem("id"),
        })
        .then((res) => {
          this.backend = res.data;
        })
        .catch((err) => {
          console.error(err);
        });
    },
    logout() {
      localStorage.clear();
      this.$router.push({ name: "login" });
    },
    save() {
      const path = "http://127.0.0.1:5000/profileEdit";
      axios
        .post(path, {
          userId: localStorage.getItem("id"),
          nickName: this.nickName,
          aboutMe: this.aboutMe,
        })
        .then((res) => {
          this.backend = res.data;
        })
        .catch(() => {});
      setTimeout(() => {
        this.$router.push({
          name: "profile",
          params: { id: localStorage.getItem("id") },
        });
      }, 50);
    },
    cancel() {
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
  userProfile() {
    this.$router.push({
      name: "profile",
      params: { id: localStorage.getItem("id") },
    });
  },
};
</script>

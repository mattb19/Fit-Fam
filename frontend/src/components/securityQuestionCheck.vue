<style scoped>
.addmargin {
  margin-top: 0.625em;
  margin-bottom: 0.625em;
}
.col-sm-12 {
  margin-right: 6.25em;
}
nav {
  margin-bottom: 2em;
}
.large {
  color: #488084;
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
    <h1 class="large centeralign">Security Question Check</h1>
    <form @submit="getStats">
      <label for="answer1">Answer to Question1:</label>
      <input
        type="text"
        id="answer1"
        name="answer1"
        required
        v-model="answer1"
      /><br /><br required />
      <label for="answer2">Answer to Question2:</label>
      <input
        type="text"
        id="answer2"
        name="answer2"
        required
        v-model="answer2"
      /><br /><br />
      <input type="submit" value="Submit" />
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  // props: ["userEmail"],
  data() {
    return {
      //userEmail: "",
      secQuestion1: "",
      answer1: "",
      secQuestion2: "",
      answer2: "",
      backend: "",
      user: "",
    };
  },
  methods: {
    checkLoggedIn() {
      if (localStorage.getItem("email") === null) {
        this.$router.push({ name: "login" });
      }
    },
    getStats() {
      const path = "http://127.0.0.1:5000/securityQuestionCheck";
      axios
        .post(path, {
          userEmail: localStorage.getItem("id"),
          answer1: this.answer1,
          answer2: this.answer2,
        })
        .then((res) => {
          this.backend = res.data;
        })
        .catch((err) => {
          this.$router.push({ name: "securityQuestionCheck" });
          console.error(err);
        });
      this.$router.push({ name: "resetPassword" });
    },
    logout() {
      localStorage.clear();
      this.$router.push({ name: "login" });
    },
  },
  created() {
    setTimeout(() => {
      this.checkLoggedIn();
    }, 200);
  },
};
</script>

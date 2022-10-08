<style scoped>
.addmargin {
  margin-top: 10px;
  margin-bottom: 10px;
}
.col-sm-12 {
  margin-right: 100px;
}
form {
  max-width: 30%;
  margin: 1% auto;
  background: #fff;
  text-align: left;
  padding: 1.25em;
  outline: 0.2em solid black;
}
label {
  color: rgb(128, 128, 128);
  display: inline-block;
  margin: 1.5em 0em 0.9375em;
  text-transform: uppercase;
}
input {
  display: block;
  padding: 0.625em 0.375em;
  width: 100%;
  box-sizing: border-box;
  border-bottom: 0.07em solid #ddd;
  color: #555;
}
button {
  background: #2c3e50;
  border: 0;
  padding: 10px 20px;
  color: white;
  border-radius: 20px;
}
.submit {
  margin-top: 1.5em;
  text-align: center;
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
              <a class="nav-link active" href="/login">Login</a>
            </li>
          </ul>
        </div>
      </div>
    </nav>
    <h1 class="large centeralign">Create an Account</h1>
    <form>
      <label>First name:</label>
      <input type="text" v-model="first" required />

      <label>Last name:</label>
      <input type="text" v-model="last" required />

      <label>Email:</label>
      <input type="email" v-model="email" required />

      <label>Password:</label>
      <input type="password" v-model="password" required />

      <div class="button">
        <button class="submit" type="submit">Submit</button>
      </div>
    </form>
    <!--
    <p>Name: {{ first }} {{ last }}</p>
    <p>Email: {{ email }}</p>
    <p>Password: {{ password }}</p>
    <p>{{ backend }}</p>
    -->
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      first: "",
      last: "",
      email: "",
      password: "",
      backend: "",
    };
  },
  methods: {
    getStats() {
      const path = "http://127.0.0.1:5000/home";
      axios
        .get(path)
        .then((res) => {
          this.backend = res.data;
        })
        .catch((err) => {
          console.error(err);
        });
    },
  },
  created() {
    this.getStats();
  },
};
</script>

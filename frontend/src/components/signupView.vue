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
        <a class="navbar-brand" href="http://localhost:8080/login">FitFam</a>
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
              <a class="nav-link active" href="/login">Login</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="/signup">Sign Up</a>
            </li>
          </ul>
        </div>
      </div>
    </nav>
    <h1 class="large centeralign">Create an Account</h1>
    <form @submit="submitInfo" method="post">
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
    };
  },
  methods: {
    submitInfo() {
      const path = "http://127.0.0.1:5000/signup";
      axios
        .post(path, {
          first: this.first,
          last: this.last,
          email: this.email,
          password: this.password,
        })
        .then((res) => {
          this.backend = res.data;
          localStorage.setItem("id", res.data);
        })
        .catch((err) => {
          this.$router.push({ name: "signup" });
          console.error(err);
        });
      this.$router.push({ name: "security_questions" });
    },
  },
};
</script>

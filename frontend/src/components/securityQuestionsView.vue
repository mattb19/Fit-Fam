<style scoped>
.addmargin {
  margin-top: 10px;
  margin-bottom: 10px;
}

.home {
  background-color: #383c44;
}
form {
  max-width: 30%;
  margin: 1% auto;
  background: #fff;
  text-align: left;
  padding: 1.25em;
  outline: 0.2em solid #488084;
}
label {
  color: #488084;
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
  background: #488084;
  border: 0;
  padding: 0.625em 1.25em;
  color: white;
  border-radius: 1.25em;
}
.submit {
  margin-top: 1.5em;
  text-align: center;
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
              <a class="nav-link" href="/login">Login</a>
            </li>
          </ul>
        </div>
      </div>
    </nav>
    <h1 class="large centeralign">Security Questions</h1>

    <form @submit="getStats">
      <label for="secQuestion1">Choose a security question:</label>

      <select name="secQuestion1" required v-model="secQuestion1" id="Question">
        <option value="Q1">In what city were you born?</option>
        <option value="Q2">What is the name of your favorite pet?</option>
        <option value="Q3">What is your mother's maiden name?</option>
        <option value="Q4">What high school did you attend?</option>
        <option value="Q5">What was the name of your elementary school?</option>
        <option value="Q6">What was the make of your first car?</option>
        <option value="Q7">What was your favorite food as a child?</option>
        <option value="Q8">Where did you meet your spouse?</option>
        <option value="Q9">What year was your father (or mother) born?</option>
      </select>
      <label for="answer1">Answer to Question1:</label>
      <input
        type="text"
        id="answer1"
        name="answer1"
        required
        v-model="answer1"
      /><br /><br required />
      <label for="secQuestion2">Choose a security question:</label>

      <select name="secQuestion2" required v-model="secQuestion2" id="Question">
        <option value="Q1">In what city were you born?</option>
        <option value="Q2">What is the name of your favorite pet?</option>
        <option value="Q3">What is your mother's maiden name?</option>
        <option value="Q4">What high school did you attend?</option>
        <option value="Q5">What was the name of your elementary school?</option>
        <option value="Q6">What was the make of your first car?</option>
        <option value="Q7">What was your favorite food as a child?</option>
        <option value="Q8">Where did you meet your spouse?</option>
        <option value="Q9">What year was your father (or mother) born?</option>
      </select>
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
    <p>secQuestion1 {{ secQuestion1 }}</p>
    <p>answer1 {{ answer1 }}</p>
    <p>secQuestion2 {{ secQuestion2 }}</p>
    <p>answer2 {{ answer2 }}</p>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      secQuestion1: "",
      answer1: "",
      secQuestion2: "",
      answer2: "",
      backend: "",
    };
  },
  methods: {
    getStats() {
      const path = "http://127.0.0.1:5000//security_questions";
      axios
        .post(path, {
          secQuestion1: this.secQuestion1,
          answer1: this.answer1,
          secQuestion2: this.secQuestion2,
          answer2: this.answer2,
        })
        .then((res) => {
          this.backend = res.data;
        })
        .catch((err) => {
          console.error(err);
        });
      this.$router.push({ name: "home" });
    },
  },
};
</script>

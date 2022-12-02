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
    <navBar></navBar>
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
        <option value="Q9">What year was your father born?</option>
        <option value="Q10">What year was your mother born?</option>
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
        <option value="Q9">What year was your father born?</option>
        <option value="Q10">What year was your mother born?</option>
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
    <!---
    <p>{{ userId }}</p>
    <p>secQuestion1 {{ secQuestion1 }}</p>
    <p>answer1 {{ answer1 }}</p>
    <p>secQuestion2 {{ secQuestion2 }}</p>
    <p>answer2 {{ answer2 }}</p>
    --->
  </div>
</template>

<script>
import axios from "axios";
import NavBarComponent from "./NavBarComponent.vue";

export default {
  // props: ["userEmail"],
  data() {
    return {
      //userEmail: "",
      secQuestion1: "",
      answer1: "",
      secQuestion2: "",
      answer2: "",
      userId: "",
      backend: "",
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
    getStats() {
      const path = "http://127.0.0.1:5000//security_questions";
      axios
        .post(path, {
          secQuestion1: this.secQuestion1,
          answer1: this.answer1,
          secQuestion2: this.secQuestion2,
          answer2: this.answer2,
          userId: localStorage.getItem("id"),
        })
        .then((res) => {
          this.backend = res.data;
        })
        .catch((err) => {
          console.error(err);
        });
      this.$router.push({ name: "home" });
    },
    logout() {
      localStorage.clear();
      this.$router.push({ name: "login" });
    },
  },
  created() {
    setTimeout(() => {
      this.checkLoggedIn();
    }, 300);
  },
};
</script>

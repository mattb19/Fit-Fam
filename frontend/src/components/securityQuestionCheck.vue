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
      backend: "",
      user: "",
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
      const path = "http://127.0.0.1:5000/securityQuestionCheck";
      axios
        .post(path, {
          userId: localStorage.getItem("id"),
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

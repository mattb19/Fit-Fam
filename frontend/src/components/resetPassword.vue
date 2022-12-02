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
    <h1 class="large centeralign">Reset Password</h1>

    <form @submit="getStats">
      <label for="passwordInput1">Please enter your new password</label>
      <input
        type="text"
        id="passwordInput1"
        name="passwordInput1"
        required
        v-model="passwordInput1"
      /><br /><br required />
      <label for="passwordInput2">Re-enter your new password</label>
      <input
        type="text"
        id="passwordInput2"
        name="passwordInput2"
        required
        v-model="passwordInput2"
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
      passwordInput1: "",
      passwordInput2: "",
      userId: "",
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
      const path = "http://127.0.0.1:5000/resetPassword";
      axios
        .post(path, {
          userId: localStorage.getItem("id"),
          passwordInput1: this.passwordInput1,
          passwordInput2: this.passwordInput2,
        })
        .then((res) => {
          this.backend = res.data;
        })
        .catch((err) => {
          this.$router.push({ name: "resetPassword" });
          console.error(err);
        });
      this.$router.push({ name: "profile" });
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

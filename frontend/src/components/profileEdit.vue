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
    <navBar></navBar>
    <p></p>
    <p></p>
    <form @submit="save" class="profile">
      <h1>this is the profile for: {{ backend.realName }}</h1>
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
import NavBarComponent from "./NavBarComponent.vue";

export default {
  data() {
    return {
      backend: "",
      nickName: "",
      aboutMe: "",
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
      this.$router.push({ name: "profile" });
    },
    cancel() {
      this.$router.push({ name: "profile" });
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

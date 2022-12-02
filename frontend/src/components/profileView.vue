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
  margin-left: 2%;
  padding-bottom: 1%;
}
</style>

<template>
  <div class="searchView">
    <navBar></navBar>
    <p></p>
    <p></p>
    <section class="profile">
      <h1>this is the profile for: {{ backend.realName }}</h1>
      <h1>{{ backend.nickName }}</h1>
      <h1>{{ backend.aboutMe }}</h1>
      <button @click="edit">Edit</button>
      <button @click="changePassword">Reset Password</button>
      <button @click="changeSec">Change Security Questions</button>
    </section>
    <div style="float: right; width: 100em"><feedViewObj /></div>
  </div>
</template>

<script>
import axios from "axios";
import feedViewObj from "./feedView.vue";
import NavBarComponent from "./NavBarComponent.vue";

export default {
  data() {
    return {
      backend: "",
    };
  },
  components: {
    feedViewObj,
    navBar: NavBarComponent,
  },
  methods: {
    checkLoggedIn() {
      if (localStorage.getItem("id") === null) {
        this.$router.push({ name: "login" });
      }
    },
    getStats() {
      const path = "http://127.0.0.1:5000/profile";
      axios
        .post(path, {
          userId: localStorage.getItem("id"),
        })
        .then((res) => {
          this.backend = res.data;
        })
        .catch(() => {});
    },
    logout() {
      localStorage.clear();
      this.$router.push({ name: "login" });
    },
    edit() {
      this.$router.push({ name: "profileEdit" });
    },
    changeSec() {
      this.$router.push({ name: "security_questions" });
    },
    changePassword() {
      this.$router.push({ name: "securityQuestionCheck" });
    },
    postFeedMeta() {
      // used to set the backend variables to what searches to look for
      const path = "http://127.0.0.1:5000/feedmeta";
      axios
        .post(path, {
          targetGroupTmp: "0",
          targetPersonsTmp: " AND poster = 1",
          /*Configure these strings to add targeting
          target persons assignment will be " AND poster = " + str(targetPersons)
          target group assignment will be str(groupId)*/
        })
        .then((res) => {
          this.dataPassLog = res.data;
        })
        .catch((err) => {
          console.error(err);
        });
    },
  },
  created() {
    this.getStats();
    this.postFeedMeta();
    setTimeout(() => {
      this.checkLoggedIn();
    }, 300);
  },
};
</script>

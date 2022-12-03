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

.butt {
  margin-right: 10px;
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
              <a class="nav-link active" @click="userProfile">Profile</a>
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
    <section class="profile">
      <h1>{{ backend.realName }} #{{ id }}</h1>
      <h1>{{ backend.realName }}</h1>
      <h1>{{ backend.nickName }}</h1>
      <h1>{{ backend.aboutMe }}</h1>
      <button class="butt" @click="edit">Edit</button>
      <button class="butt" @click="changePassword">Reset Password</button>
      <button class="butt" @click="changeSec">Change Security Questions</button>
    </section>
    <div class="posted"><feedViewObj /></div>
  </div>
</template>

<script>
import axios from "axios";
import feedViewObj from "./feedView.vue";

export default {
  props: ["id"],
  data() {
    return {
      backend: "",
    };
  },
  components: {
    feedViewObj,
  },
  methods: {
    checkLoggedIn() {
      if (localStorage.getItem("id") === null) {
        this.$router.push({ name: "login" });
      }
    },
    getStats() {
      const path = "http://127.0.0.1:5000/profile/" + this.$props.id;
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
    userProfile() {
      this.$router.push({
        name: "profile",
        params: { id: localStorage.getItem("id") },
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

<!-- eslint-disable prettier/prettier -->
<style scoped>
.addmargin {
  margin-top: 10px;
  margin-bottom: 10px;
}

.home {
  background-color: #383c44;
}

th,
td {
  padding-top: 10px;
  padding-bottom: 20px;
  padding-left: 30px;
  padding-right: 400px;
  size: 20px;
}

button {
  size: 15px;
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
              <a class="nav-link active" href="/groups">Groups</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" @click="userProfile">Profile</a>
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
    <div>
      <th class="groupsDisplay" align="left">
        Groups<button @click="createNewGroup">+</button>
      </th>
      <th>Group Info</th>
    </div>
    <p></p>
    <p></p>
    <p>
      <button @click="getGroupFeed">{{ backend }}</button>
    </p>
    <feedViewObj />
  </div>
</template>

<script>
import axios from "axios";
import feedViewObj from "./feedView.vue";

export default {
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
    createNewGroup() {
      this.$router.push({ name: "create_group" });
    },
    logout() {
      localStorage.clear();
      this.$router.push({ name: "login" });
    },
    getGroupFeed() {},
    postFeedMeta() {
      // used to set the backend variables to what searches to look for
      const path = "http://127.0.0.1:5000/feedmeta";
      axios
        .post(path, {
          targetGroupTmp: "0",
          targetPersonsTmp: "",
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
    getStats() {
      const path = "http://127.0.0.1:5000/groups";
      axios
        .get(path)
        .then((res) => {
          this.backend = res.data;
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

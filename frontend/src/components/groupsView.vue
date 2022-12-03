<!-- eslint-disable prettier/prettier -->
<style scoped>
li {
  display: block;
  float: left;
}

ul {
  max-width: 5px;
}

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
              <a class="nav-link" href="/profile">Profile</a>
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
    <div class="groups">
      <ul>
        <li>
          <button
            v-for="group in backend"
            :key="group.groupId"
            v-bind:gID="group.groupId"
            @click="postFeedMeta(group.groupId)"
          >
            {{ group.groupName }} <br />
          </button>
        </li>
      </ul>
    </div>
    <p></p>
    <p></p>
    <p></p>
    <feedViewObj />
  </div>
</template>

<script>
import axios from "axios";
import feedViewObj from "./feedView.vue";
import Vue from "vue";
/*global*/
Vue.prototype.$groupFeed = "1";

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
    postFeedMeta(groupTar) {
      // used to set the backend variables to what searches to look for
      this.$groupFeed = groupTar.toString();
      const path = "http://127.0.0.1:5000/feedmeta";
      axios
        .post(path, {
          targetGroupTmp: groupTar.toString(),
          targetPersonsTmp: "0",
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
  },
  created() {
    this.getStats();
    this.postFeedMeta(this.$groupFeed);
    setTimeout(() => {
      this.checkLoggedIn();
    }, 300);
  },
};
</script>

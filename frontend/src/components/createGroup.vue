<!-- eslint-disable prettier/prettier -->
<style scoped>
.addmargin {
  margin-top: 0.625em;
  margin-bottom: 0.625em;
}

.home {
  background-color: #383c44;
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
              <a class="nav-link active" href="/home">Global</a>
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
              <button @click="logout">Logout</button>
            </li>
          </ul>
        </div>
      </div>
    </nav>
    <div class="form-group">
      <div class="groupName">
        <input
          name="groupName"
          type="text"
          class="groupName"
          placeholder="Enter Group Name"
          required
          size="80"
          id="groupName"
          v-model="groupName"
        />
      </div>
    </div>
    <div class="button">
      <button
        @submit="passGroupInfo"
        type="button"
        class="btn btn-dark"
        href="/"
        v-on:click="passGroupInfo"
      >
        Create Group
      </button>
    </div>
    <p></p>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      groupName: "",
      userId: 1,
    };
  },
  methods: {
    checkLoggedIn() {
      if (localStorage.getItem("email") === null) {
        this.$router.push({ name: "login" });
      }
    },
    logout() {
      localStorage.clear();
      this.$router.push({ name: "login" });
    },
    passGroupInfo() {
      const path = "http://127.0.0.1:5000//create_group";
      axios
        .post(path, {
          userId: this.userId,
          groupName: this.groupName,
        })
        .then((res) => {
          this.backend = res.data;
        })
        .catch((err) => {
          console.error(err);
        });
      this.$router.push({ name: "groups" });
    },
    getStats() {
      const path = "http://127.0.0.1:5000/create_group";
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
    setTimeout(() => {
      this.checkLoggedIn();
    }, 300);
  },
};
</script>

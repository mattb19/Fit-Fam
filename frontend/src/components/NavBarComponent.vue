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
    <div class="fixed-top">
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
              <li class="nav-item" v-if="currentURL === '/home'">
                <a class="nav-link active" href="/home">Global</a>
              </li>
              <li class="nav-item" v-else>
                <a class="nav-link" href="/home">Global</a>
              </li>
              <li class="nav-item" v-if="currentURL === '/groups'">
                <a class="nav-link active" href="/groups">Groups</a>
              </li>
              <li class="nav-item" v-else>
                <a class="nav-link" href="/groups">Groups</a>
              </li>
              <li class="nav-item" v-if="currentURL === currentUser">
                <a class="nav-link active" @click="userProfile">Profile</a>
              </li>
              <li class="nav-item" v-else>
                <a class="nav-link" @click="userProfile">Profile</a>
              </li>
              <li class="nav-item" v-if="currentURL === '/search'">
                <a class="nav-link active" href="/search">Search</a>
              </li>
              <li class="nav-item" v-else>
                <a class="nav-link" href="/search">Search</a>
              </li>
              <li class="nav-item">
                <button @click="logout">Logout</button>
              </li>
            </ul>
          </div>
        </div>
      </nav>
    </div>
    <!---
    this is to make space so the feed will be properly displayed
    --->
    <h1>
      you have found the answer to the ultimate Question of Life, the Universe,
      and Everything it is:
    </h1>
    <h1>42</h1>
  </div>
</template>

<script>
export default {
  data() {
    return {
      currentURL: window.location.pathname,
      currentUser: "/profile/" + localStorage.getItem("id"),
    };
  },
  methods: {
    checkLoggedIn() {
      if (localStorage.getItem("id") === null) {
        this.$router.push({ name: "login" });
      }
    },
    logout() {
      localStorage.clear();
      this.$router.push({ name: "login" });
    },
    userProfile() {
      this.$router.push({
        name: "profile",
        params: { id: localStorage.getItem("id") },
      });
    },
  },
};
</script>

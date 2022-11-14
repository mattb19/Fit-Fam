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
        <a class="navbar-brand" href="http://localhost:8080/">FitFam</a>
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
              <a class="nav-link active" href="/">Global</a>
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
              <a class="nav-link" href="/signup">Sign Up</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="/post">Post</a>
            </li>
          </ul>
        </div>
      </div>
    </nav>
    <p></p>
    <postViewObj
      class="post"
      v-for="(postItem, i) in posts"
      :key="i"
      :postItem="postItem"
    />
  </div>
</template>

<script>
import axios from "axios";
import postViewObj from "./postView.vue";

export default {
  data() {
    return {
      post_list: [],
      posts: "",
      createdLog: null,
    };
  },
  components: {
    postViewObj,
  },
  methods: {
    getStats() {
      const path = "http://127.0.0.1:5000/home";
      axios
        .get(path)
        .then((res) => {
          this.backend = res.data;
        })
        .catch((err) => {
          console.error(err);
        });
    },
    getFeedMeta() {
      const path = "http://127.0.0.1:5000/feedmeta";
      axios
        .get(path)
        .then((res) => {
          this.createdLog = res.data;
        })
        .catch((err) => {
          console.error(err);
        });
    },
    getPost() {
      const path = "http://127.0.0.1:5000/posts";
      axios
        .get(path)
        .then((res) => {
          this.posts = res.data;
        })
        .catch((err) => {
          console.error(err);
        });
    },
    handleScroll() {
      if (
        window.scrollY + window.innerHeight >=
        document.body.scrollHeight - 50
      ) {
        const new_postItem = this.getPost();

        this.post_list = [...this.post_list, ...new_postItem];
      }
    },
  },
  created() {
    this.getStats();
    this.getFeedMeta();
  },
  async mounted() {
    await this.createdLog;
    this.post_list = this.getPost();
    window.addEventListener("scroll", this.handleScroll);
  },
};
</script>

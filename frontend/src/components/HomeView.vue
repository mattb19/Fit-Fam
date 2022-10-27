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
    <!--Bootstarp Template from Site
    <div class="card mb-3">
      <h3 class="card-header text-left">Profile Nickname</h3>
      <div class="card-body">
        <h5 class="card-title">Special title treatment</h5>
        <h6 class="card-subtitle text-muted">Support card subtitle</h6>
      </div>
      <div class="card-body">
        <p class="card-text">
          Some quick example text to build on the card title and make up the
          bulk of the card's content.
        </p>
      </div>
      <div class="card-footer text-muted">2 days ago</div>
    </div>
    Bootstrap Template from Site end-->
    <postViewObj
      class="post"
      v-for="(postItem, i) in post_list"
      :key="i"
      :postItem="postItem"
    />
    <p></p>
    <p>{{ backend }}</p>
  </div>
</template>

<script>
import axios from "axios";
import postViewObj from "./postView.vue";

export default {
  data() {
    return {
      post_list: [],
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
    getPost() {
      /*bellow should be replaced with axios post api once a retrieval mothod is implimented*/
      const post_userIds = [
        "John Doe",
        "Jane Doe",
        "Joe Schmo",
        "Thomas Tugman",
        "Jackson Pot",
        "Phil Smith",
      ];

      const postItem = [];

      for (let i = 0; i < 10; i++) {
        postItem.push({
          userId: post_userIds[Math.floor(Math.random() * post_userIds.length)],
          postText:
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. In odio mauris, sollicitudin ac consequat a, pretium non mauris. Nullam elit turpis, fringilla efficitur pellentesque sed, fermentum sed nulla. Donec vitae elit nec nisl luctus sodales nec porta turpis. Nunc pulvinar a mi at mattis. Nunc quis mi in arcu lobortis pellentesque non in dui. Mauris ut justo maximus, dignissim diam a, dignissim felis. Fusce efficitur accumsan ex id porta. Proin elementum convallis tellus id malesuada. Morbi et fermentum velit. In massa orci, iaculis tincidunt erat sed, rhoncus mattis erat. Aenean at tristique urna.",
        });
      }
      return postItem;
      /*End of substitute api*/
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
  mounted() {
    this.post_list = this.getPost();
    window.addEventListener("scroll", this.handleScroll);
  },
};
</script>

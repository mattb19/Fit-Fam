<template>
  <div class="card mb-3">
    <h3 class="card-header" style="text-align: left">
      {{ postItem.poster }}
      <span style="float: right"> {{ postItem.postDateTime }} </span>
    </h3>
    <!--<h5 class="card-title">{{ postItem.title }}</h5>-->
    <div>{{ postItem.postImage }}</div>
    <rect width="100%" height="100%" fill="#868e96"></rect>
    <text x="50%" y="50%" fill="#dee2e6" dy=".3em">Image cap</text>
    <div class="card-body">
      <p class="card-text">{{ postItem.description }}</p>
    </div>
    <div class="conatiner">
      <span class="badge bg-primary">{{ postItem.postTags }}</span>
    </div>
    <div class="like">
      <a class="like-button" href="#" v-on:click="like">
        <img src="../assets/like.jpg" alt="Image" height="20" />
      </a>
      <p class="numLikes">{{ postItem.likes }}</p>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  props: ["postItem"],
  data() {
    return {
      post_list: [],
      posts: "",
    };
  },
  methods: {
    getStats() {
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
    like() {
      const path = "http://127.0.0.1:5000/like";
      const formData = new FormData();
      formData.append("file", this.file);

      axios
        .post(path, {
          like: "yes",
        })
        .then((res) => {
          console.log(res);
        })
        .catch((error) => {
          console.log(error);
        });
      this.$router.push({ name: "home" });
      this.getStats();
    },
  },
};
</script>

<style>
article {
  background-color: #efefef;
  border-radius: 1rem;
  padding: 1rem 2rem;
  box-shadow: 0px 3px 6px rgba(0, 0, 0, 0.2);
  margin-bottom: 2rem;
  color: #2c3e50;
}

article h2 {
  margin-bottom: 1rem;
}

.container > * {
  display: inline-block;
}

#HASH {
  display: flex;
  justify-content: space-between;
}

.card-title {
  margin-top: 15px;
}
</style>

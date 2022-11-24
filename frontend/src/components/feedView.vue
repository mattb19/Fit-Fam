<template>
  <div>
    <a href="/post" class="float">
      <img src="../assets/post-button.png" alt="Image" height="60" />
    </a>
    <p></p>
    <postViewObj
      class="post"
      v-for="(postItem, i) in posts"
      :key="i"
      :postItem="postItem"
      :viewerId="viewerId"
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
      viewerId: localStorage.getItem("id"),
    };
  },
  components: {
    postViewObj,
  },
  methods: {
    getFeedMeta() {
      // used to set the position in the feed on page load
      const path = "http://127.0.0.1:5000/feedmeta";
      axios
        .get(path)
        .then((res) => {
          this.createdLog = res.data;
          return "OK";
        })
        .catch((err) => {
          console.error(err);
        });
    },
    getPost() {
      // used to retrieve posts dict list from backend
      const path = "http://127.0.0.1:5000/posts";
      axios
        .get(path)
        .then((res) => {
          this.posts = res.data;
          for (let i = 0; i < this.posts.length; i++) {
            let tempTagList = JSON.parse(this.posts[i].tagList);
            this.posts[i].tagList = tempTagList;
          }
        })
        .catch((err) => {
          console.error(err);
        });
    },
    // scroll window listener
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
    this.getFeedMeta();
    setTimeout(() => {
      this.post_list = this.getPost();
      window.addEventListener("scroll", this.handleScroll);
    }, 50);
    // if newest posts are not appearing at the top of the feed, increase the above value
  },
};
</script>

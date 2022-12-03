<!-- eslint-disable vue/require-v-for-key -->
<template>
  <div class="card mb-3">
    <h3
      v-if="postItem.postNickname != null"
      class="card-header"
      style="text-align: left"
    >
      <a class="nav-link" @click="userProfile">{{ postItem.postNickname }}</a>
      <span style="float: right"> {{ postItem.postDateTime }} </span>
    </h3>
    <h3
      v-else-if="postItem.postFirstName != null"
      class="card-header"
      style="text-align: left"
    >
      <a class="nav-link" @click="userProfile"
        >{{ postItem.postFirstName }} {{ postItem.postLastName }}</a
      >
      <span style="float: right"> {{ postItem.postDateTime }} </span>
    </h3>
    <h3 v-else class="card-header" style="text-align: left">Invalid Account</h3>
    <!--<h5 class="card-title">{{ postItem.title }}</h5>-->
    <rect width="100%" height="100%" fill="#868e96"></rect>
    <text x="50%" y="50%" fill="#dee2e6" dy=".3em">Image cap</text>
    <div v-if="postItem.postNickname == null && postItem.postFirstName == null">
      <div class="card-body">
        <p></p>
        <!-- <li>
          {{ postItem.poster }} {{ postItem.postFirstName }}
          {{ postItem.postLastName }}
        </li> -->
        <!-- to test failure cases -->
        <img src="../assets/removed.png" alt="Image" height="120" />
        <p></p>
      </div>
    </div>
    <div v-else>
      <div class="card-body">
        <h1>{{ postItem.postTitle }}</h1>
        <div v-if="postItem.postImage != null">
          <p></p>
          <img :src="postItem.postImage" width="270px" height="200px" />
          <p></p>
        </div>
        <p class="card-text">
          {{ postItem.description }}
        </p>
      </div>
      <div class="conatiner">
        <span class="badge bg-primary" v-for="tag in postItem.postTags">{{
          tag
        }}</span>
      </div>
      <div class="like">
        <a
          v-if="viewerId == postItem.poster"
          class="like-button"
          v-on:click="deletePost(postItem.postId)"
        >
          <img src="../assets/delete.png" alt="Image" height="20" />
        </a>
        <a
          class="like-button"
          href="#"
          v-on:click="like(postItem.postId, postItem.postLikes)"
        >
          <img src="../assets/like.png" alt="Image" height="20" />
        </a>
        <p class="numLikes">{{ postItem.postLikes }}</p>
      </div>
      <!-- start of delete button -->
      <!-- end of delete box -->
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  props: ["postItem", "viewerId"],
  data() {
    return {
      backend: "",
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
    blobToImg(image) {
      var img = new Image(img);
      img.src = image;
      return img;
    },
    like(postId, postLikes) {
      const path = "http://127.0.0.1:5000/like";
      const formData = new FormData();
      formData.append("file", this.file);
      const id = postId;
      const likes = postLikes;

      axios
        .post(path, {
          postId: id,
          postLikes: likes,
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
    deletePost(postId) {
      const path = "http://127.0.0.1:5000/delete_post";
      const id = postId;

      axios
        .post(path, {
          postId: id,
        })
        .then((res) => {
          console.log(res);
        })
        .catch((error) => {
          console.log(error);
        });
    },
    userProfile() {
      this.$router.push({
        name: "profile",
        params: { id: this.$props.postItem.poster },
      });
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

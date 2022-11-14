<template>
  <div class="card mb-3">
    <h3
      v-if="postItem.postNickname != null"
      class="card-header"
      style="text-align: left"
    >
      {{ postItem.postNickname }}
      <span style="float: right"> {{ postItem.postDateTime }} </span>
    </h3>
    <h3
      v-else-if="
        postItem.postFirstName != null && postItem.postLastName != null
      "
      class="card-header"
      style="text-align: left"
    >
      {{ postItem.postFirstName }} {{ postItem.postLastName }}
      <span style="float: right"> {{ postItem.postDateTime }} </span>
    </h3>
    <h3 v-else class="card-header" style="text-align: left">
      Account Removed
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
    <div>
      <button class="like" float:left>
        <img src="../assets/like.jpg" alt="Image" height="42" />
      </button>
    </div>
  </div>
</template>

<script>
export default {
  props: ["postItem"],
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

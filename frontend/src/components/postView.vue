<template>
  <div class="card mb-3">
    <h3 class="card-header" style="text-align: left">
      {{ postItem.userId }}
      <span style="float: right"> 2 Days Ago </span>
    </h3>
    <h5 class="card-title">{{ postItem.title }}</h5>
    <div>{{ postItem.image }}</div>
    <rect width="100%" height="100%" fill="#868e96"></rect>
    <text x="50%" y="50%" fill="#dee2e6" dy=".3em">Image cap</text>
    <div class="card-body">
      <p class="card-text">{{ postItem.postText }}</p>
    </div>
    <div class="conatiner">
      <span class="badge bg-primary">Legs</span>
      <span class="badge bg-primary">Chest</span>
      <span class="badge bg-primary">Cardio</span>
      <span class="badge bg-primary">Tricepts</span>
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

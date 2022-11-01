<!-- eslint-disable prettier/prettier -->
<template>
  <div class="card mb-3">
    <h3 class="card-header" style="text-align: left">
      {{ postItem["_Post__poster"] }}
      <span style="float: right"> {{ postItem["_Post__postDateTime"] }} </span>
    </h3>
    <svg
      xmlns="http://www.w3.org/2000/svg"
      class="d-block user-select-none"
      width="100%"
      height="200"
      aria-label="Placeholder: Image cap"
      focusable="false"
      role="img"
      preserveAspectRatio="xMidYMid slice"
      viewBox="0 0 318 180"
      style="font-size: 1.125rem; text-anchor: middle"
    >
      <rect width="100%" height="100%" fill="#868e96"></rect>
      <text x="50%" y="50%" fill="#dee2e6" dy=".3em">Image cap</text>
    </svg>
    <div class="card-body">
      <p class="card-text">{{ postItem["_Post__postText"] }}</p>
    </div>
    <div class="container">
      <span class="badge bg-primary">Legs</span>
      <span class="badge bg-primary">Chest</span>
      <span class="badge bg-primary">Cardio</span>
      <span class="badge bg-primary">Tricepts</span>
    </div>
  </div>
</template>
<!-- eslint-disable prettier/prettier -->
<script>
export default {
  props: ["postItem"],
};
</script>
<!-- eslint-disable prettier/prettier -->
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
</style>

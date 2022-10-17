<template>
  <article>
    <h2>{{ postItem.userId }}</h2>
    <p>
      <!-- Formating Test text
        
      Lorem ipsum dolor sit amet, consectetur adipiscing elit. In odio mauris,
      sollicitudin ac consequat a, pretium non mauris. Nullam elit turpis,
      fringilla efficitur pellentesque sed, fermentum sed nulla. Donec vitae
      elit nec nisl luctus sodales nec porta turpis. Nunc pulvinar a mi at
      mattis. Nunc quis mi in arcu lobortis pellentesque non in dui. Mauris ut
      justo maximus, dignissim diam a, dignissim felis. Fusce efficitur accumsan
      ex id porta. Proin elementum convallis tellus id malesuada. Morbi et
      fermentum velit.-->
      {{ postItem.postText }}
    </p>
  </article>
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
</style>

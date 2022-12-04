<style scoped>
.addmargin {
  margin-top: 10px;
  margin-bottom: 10px;
}

.home {
  background-color: #383c44;
}
label {
  display: inline-block;
  padding-left: 15px;
  text-indent: -15px;
}

input {
  width: 15px;
  height: 15px;
  padding: 0;
  margin: 0;
  position: relative;
  top: -1px;
}
.tags {
  display: flex;
  width: 100%;
  max-height: 10%;
  max-width: 80%;
}
</style>

<template>
  <div class="searchView">
    <navBar></navBar>
    <form class="tags">
      <label>
        <input type="checkbox" value="Arms" v-model="tag1" /> Arms
      </label>
      <label>
        <input type="checkbox" value="Back" v-model="tag2" /> Back
      </label>
      <label>
        <input type="checkbox" value="Back/Bicep" v-model="tag3" />
        Back/Bicep
      </label>
      <label>
        <input type="checkbox" value="Chest" v-model="tag4" /> Chest
      </label>
      <label>
        <input type="checkbox" value="Chest/Tricep" v-model="tag5" />
        Chest/Tricep
      </label>
      <label>
        <input type="checkbox" value="Legs" v-model="tag6" /> Legs
      </label>
      <label>
        <input type="checkbox" value="Full Body" v-model="tag7" /> Full Body
      </label>
      <button @click="searchTags">Search</button>
    </form>
    <h1>{{ tags }}</h1>
    <div><feedViewObj /></div>
  </div>
</template>

<script>
import axios from "axios";
import NavBarComponent from "./NavBarComponent.vue";
import feedViewObj from "./feedView.vue";

export default {
  data() {
    return {
      backend: "",
      checked: "",
      tag1: "",
      tag2: "",
      tag3: "",
      tag4: "",
      tag5: "",
      tag6: "",
      tag7: "",
      tags: "",
    };
  },
  components: {
    feedViewObj,
    navBar: NavBarComponent,
  },
  methods: {
    checkLoggedIn() {
      if (localStorage.getItem("id") === null) {
        this.$router.push({ name: "login" });
      }
    },
    getStats() {
      const path = "http://127.0.0.1:5000/search";
      axios
        .get(path)
        .then((res) => {
          this.backend = res.data;
        })
        .catch((err) => {
          console.error(err);
        });
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
    searchTags() {
      this.$router.push({ name: "search" });
    },
    postFeedMeta() {
      // used to set the backend variables to what searches to look for
      const path = "http://127.0.0.1:5000/feedmeta";
      axios
        .post(path, {
          targetGroupTmp: "0",
          targetPersonsTmp: "0",
          targetTagsTmp: "Legs",
          /*Configure these strings to add targeting
          target persons assignment will be str(UserId)
          target group assignment will be str(groupId)*/
        })
        .then((res) => {
          this.dataPassLog = res.data;
        })
        .catch((err) => {
          console.error(err);
        });
    },
  },
  created() {
    this.getStats();
    setTimeout(() => {
      this.checkLoggedIn();
    }, 300);
  },
};
</script>

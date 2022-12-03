<!-- eslint-disable prettier/prettier -->
<style scoped>
.addmargin {
  margin-top: 10px;
  margin-bottom: 10px;
}

.home {
  background-color: #383c44;
}

th,
td {
  padding-top: 10px;
  padding-bottom: 20px;
  padding-left: 30px;
  padding-right: 400px;
  size: 20px;
}

button {
  size: 15px;
}
</style>

<template>
  <div class="searchView">
    <navBar></navBar>
    <div>
      <th class="groupsDisplay" align="left">
        Groups<button @click="createNewGroup">+</button>
      </th>
      <th>Group Info</th>
    </div>
    <p></p>
    <p></p>
    <p>
      <button @click="getGroupFeed">{{ backend }}</button>
    </p>
    <feedViewObj />
  </div>
</template>

<script>
import axios from "axios";
import feedViewObj from "./feedView.vue";
import NavBarComponent from "./NavBarComponent.vue";

export default {
  data() {
    return {
      backend: "",
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
    createNewGroup() {
      this.$router.push({ name: "create_group" });
    },
    logout() {
      localStorage.clear();
      this.$router.push({ name: "login" });
    },
    getGroupFeed() {},
    postFeedMeta() {
      // used to set the backend variables to what searches to look for
      const path = "http://127.0.0.1:5000/feedmeta";
      axios
        .post(path, {
          targetGroupTmp: "0",
          targetPersonsTmp: "0",
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
    getStats() {
      const path = "http://127.0.0.1:5000/groups";
      axios
        .get(path)
        .then((res) => {
          this.backend = res.data;
        })
        .catch((err) => {
          console.error(err);
        });
    },
    userProfile() {
      this.$router.push({
        name: "profile",
        params: { id: localStorage.getItem("id") },
      });
    },
  },
  created() {
    this.getStats();
    this.postFeedMeta();
    setTimeout(() => {
      this.checkLoggedIn();
    }, 300);
  },
};
</script>

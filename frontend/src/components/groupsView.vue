<!-- eslint-disable prettier/prettier -->
<style scoped>
li {
  display: block;
  float: left;
}

ul {
  max-width: 5px;
}

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
    <div class="groups">
      <ul>
        <li>
          <button
            v-for="group in backend"
            :key="group.groupId"
            v-bind:gID="group.groupId"
            @click="changeGroup(group.groupId)"
          >
            {{ group.groupName }} <br />
          </button>
        </li>
      </ul>
    </div>
    <p></p>
    <p></p>
    <p></p>
    <div class="feed">
      <feedViewObj />
    </div>
  </div>
</template>

<script>
import axios from "axios";
import feedViewObj from "./feedView.vue";
import NavBarComponent from "./NavBarComponent.vue";
import Vue from "vue";
/*global*/
Vue.prototype.$groupFeed = "0";

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
    changeGroup(TarGroup) {
      this.$groupFeed = TarGroup;
      this.postFeedMeta();
      this.$forceUpdate();
    },
    postFeedMeta() {
      // used to set the backend variables to what searches to look for
      const path = "http://127.0.0.1:5000/feedmeta";
      axios
        .post(path, {
          targetGroupTmp: this.$groupFeed.toString(),
          targetPersonsTmp: "0",
          /*Configure these strings to add targeting 
          target persons assignment will be " AND poster = " + str(targetPersons)
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

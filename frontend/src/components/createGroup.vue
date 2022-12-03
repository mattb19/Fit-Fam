<!-- eslint-disable prettier/prettier -->
<style scoped>
.addmargin {
  margin-top: 0.625em;
  margin-bottom: 0.625em;
}

.home {
  background-color: #383c44;
}
</style>

<template>
  <div class="searchView">
    <navBar></navBar>
    <div class="form-group">
      <div class="groupName">
        <input
          name="groupName"
          type="text"
          class="groupName"
          placeholder="Enter Group Name"
          required
          size="80"
          id="groupName"
          v-model="groupName"
        />
      </div>
    </div>
    <div class="button">
      <button
        @submit="passGroupInfo"
        type="button"
        class="btn btn-dark"
        href="/"
        v-on:click="passGroupInfo"
      >
        Create Group
      </button>
    </div>
    <p></p>
  </div>
</template>

<script>
import axios from "axios";
import NavBarComponent from "./NavBarComponent.vue";

export default {
  data() {
    return {
      groupName: "",
      userId: 1,
    };
  },
  components: {
    navBar: NavBarComponent,
  },
  methods: {
    checkLoggedIn() {
      if (localStorage.getItem("id") === null) {
        this.$router.push({ name: "login" });
      }
    },
    logout() {
      localStorage.clear();
      this.$router.push({ name: "login" });
    },
    passGroupInfo() {
      const path = "http://127.0.0.1:5000//create_group";
      axios
        .post(path, {
          userId: this.userId,
          groupName: this.groupName,
        })
        .then((res) => {
          this.backend = res.data;
        })
        .catch((err) => {
          console.error(err);
        });
      this.$router.push({ name: "groups" });
    },
    getStats() {
      const path = "http://127.0.0.1:5000/create_group";
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
    setTimeout(() => {
      this.checkLoggedIn();
    }, 300);
  },
};
</script>

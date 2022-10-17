import VueRouter from "vue-router";
import Vue from "vue";
import HomeView from "../components/HomeView.vue";
import loginView from "../components/loginView.vue";
import searchView from "../components/searchView.vue";
import profileView from "../components/profileView.vue";
import groupsView from "../components/groupsView.vue";
import createPost from "../components/createPost.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/home",
    name: "home",
    component: HomeView,
  },
  {
    path: "/login",
    name: "login",
    component: loginView,
  },
  {
    path: "/search",
    name: "search",
    component: searchView,
  },
  {
    path: "/profile",
    name: "profile",
    component: profileView,
  },
  {
    path: "/groups",
    name: "groups",
    component: groupsView,
  },
  {
    path: "/post",
    name: "post",
    component: createPost,
  },
  {
    path: "/",
    redirect: "/home",
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;

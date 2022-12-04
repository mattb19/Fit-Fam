import VueRouter from "vue-router";
import Vue from "vue";
import HomeView from "../components/HomeView.vue";
import loginView from "../components/loginView.vue";
import signupView from "../components/signupView.vue";
import searchView from "../components/searchView.vue";
import profileView from "../components/profileView.vue";
import groupsView from "../components/groupsView.vue";
import createPost from "../components/createPost.vue";
import security_questions from "../components/securityQuestionsView.vue";
import groupPost from "../components/createGroupPost.vue";
import createGroup from "../components/createGroup.vue";
import profileEdit from "../components/profileEdit.vue";
import securityQuestionCheck from "../components/securityQuestionCheck.vue";
import resetPassword from "../components/resetPassword.vue";

// stylesheets
import "/src/assets/stylesheets/forms.css";
import "/src/assets/stylesheets/alaska.css";
//import { component } from "vue/types/umd";

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
    path: "/signup",
    name: "signup",
    component: signupView,
  },
  {
    path: "/search",
    name: "search",
    component: searchView,
  },
  {
    path: "/profile/:id",
    name: "profile",
    props: true,
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
    path: "/security_questions",
    name: "security_questions",
    component: security_questions,
  },
  {
    path: "/profileEdit/",
    name: "profileEdit",
    component: profileEdit,
  },
  {
    path: "/",
    redirect: "/login",
  },
  {
    path: "/create_group",
    name: "create_group",
    component: createGroup,
  },
  {
    path: "/create_groupPost",
    name: "create_groupPost",
    component: groupPost,
  },
  {
    path: "/securityQuestionCheck",
    name: "securityQuestionCheck",
    component: securityQuestionCheck,
  },
  {
    path: "/resetPassword",
    name: "resetPassword",
    component: resetPassword,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;

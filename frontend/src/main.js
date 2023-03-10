import Vue from "vue";
import App from "./App.vue";
import router from "./router";
console.log("Running on Vue.js version " + Vue.version);

Vue.config.productionTip = false;

new Vue({
  router,
  render: (h) => h(App),
}).$mount("#app");

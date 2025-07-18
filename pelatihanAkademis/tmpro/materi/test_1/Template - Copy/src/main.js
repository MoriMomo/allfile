import Vue from 'vue'
import App from './App.vue'
import VueResource from "vue-resource";
import { routes } from "./route.js";
import VueRouter from "vue-router";

Vue.use(VueResource)
Vue.use(VueRouter)

const router = new VueRouter({
  routes,
  mode: 'history'
})

new Vue({
  el: '#app',
  router,
  render: h => h(App)
})

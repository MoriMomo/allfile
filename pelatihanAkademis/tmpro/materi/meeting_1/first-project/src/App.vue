<template>
  <div>
    <header>
      <app-header></app-header>
    </header>
    <main>
      <div class="list-movie">
        <div class="buttons">
          <button
            v-for="(tab, index) in tabs"
            @click="currentTab = tab.components"
            :class="['tab-button', { active: currentTab === tab.components }]"
            :key="index"
          >
            {{ tab.buttonName }}
          </button>
        </div>
        <div class="container">
          <component :is="currentTab"></component>
        </div>
      </div>
      <app-detail></app-detail>
    </main>
    <footer>
      <app-footer></app-footer>
    </footer>
  </div>
</template>

<script>
import Header from "./components/Header.vue";
import Footer from "./components/Footer.vue";
import Detail from "./components/Detail.vue";

import NowShowing from "./components/NowShowing.vue";
import ComingSoon from "./components/Comingsoon.vue";

export default {
  data() {
    return {
      tabs: [
        { components: "app-now-showing", buttonName: "NOW SHOWING" },
        { components: "app-coming-showing", buttonName: "COOMING SOON" },
      ],
      currentTab: "app-now-showing",
    };
  },
  methods: {
    detail(data) {},
  },
  components: {
    "app-header": Header,
    "app-footer": Footer,
    "app-detail": Detail,
    "app-now-showing": NowShowing,
    "app-coming-showing": ComingSoon,
  },
};
</script>

<style>
body {
  margin: 0px;
  font-family: "Roboto", sans-serif;
}

a {
  text-decoration: none;
  color: black;
}

header {
  position: sticky;
  top: 0px;
  background-color: white;
}

.container {
  margin-left: 200px;
  margin-right: 200px;
}

/* Now Showing */
.movies {
  display: flex;
  justify-content: center;
}

.title h1 {
  font-size: 25px;
}

/* Movie List */
.list-movie {
  font-family: sans-serif;
  border: 1px solid #eee;
  border-radius: 2px;
  padding: 0px;
  margin-top: 50px;
  margin-bottom: 40px;
  margin-left: 165px;
  margin-right: 165px;
  position: relative;
}

.tab-button {
  padding: 6px 10px;
  border-top-left-radius: 5px;
  border-top-right-radius: 5px;
  border: none;
  cursor: pointer;
  background: #00afc1;
  margin-bottom: -1px;
  margin-right: -1px;
  color: white;
}

.buttons {
  position: absolute;
  top: -29px;
}

.tab-button:hover {
  background: #5f6f94;
}
.tab-button.active {
  background: #153462;
}
</style>

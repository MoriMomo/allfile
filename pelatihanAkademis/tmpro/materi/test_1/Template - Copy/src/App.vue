<template>
  <div>
    <Header></Header>
    <router-view></router-view>
  </div>
</template>

<script>
import Header from "./components/Header.vue";

export default {
  components: {
    Header,
  },
};
</script>

<style>
html,
body {
  height: 100%;
  font-family: "Cairo", sans-serif;
}

h2,
h5,
h6 {
  margin: 0;
  color: #111111;
  font-weight: 400;
  font-family: "Cairo", sans-serif;
}

h2 {
  font-size: 36px;
}

h5 {
  font-size: 18px;
}

h6 {
  font-size: 16px;
}

p {
  font-size: 16px;
  font-family: "Cairo", sans-serif;
  color: #6f6f6f;
  font-weight: 400;
  line-height: 26px;
  margin: 0 0 15px 0;
}

img {
  max-width: 100%;
}

input:focus,
select:focus,
button:focus,
textarea:focus {
  outline: none;
}

a:hover,
a:focus {
  text-decoration: none;
  outline: none;
  color: #ffffff;
}

ul,
ol {
  padding: 0;
  margin: 0;
}
</style>
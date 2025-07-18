<template>
  <div class="featured__controls">
    <ul>
      <li v-for="(item, index) in genre" :key="index" @click="genreClick(item)">
        {{ item }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      genre: [
        "all",
        "action",
        "sci-fi",
        "horror",
        "thriller",
        "comedy",
        "romance",
        "adventure",
        "fantasy",
      ],
    };
  },
  methods: {
    genreClick(inputGenre) {
      // console.log(inputGenre);
      this.$emit("genreReturn", inputGenre);
    },
  },
};
</script>

<style scoped>
.featured__controls {
  text-align: center;
  margin-bottom: 50px;
}

.featured__controls ul li {
  list-style: none;
  font-size: 18px;
  color: #1c1c1c;
  display: inline-block;
  margin-right: 25px;
  position: relative;
  cursor: pointer;
}

.featured__controls ul li.active:after {
  opacity: 1;
}

.featured__controls ul li:after {
  position: absolute;
  left: 0;
  bottom: -2px;
  width: 100%;
  height: 2px;
  background: #7fad39;
  content: "";
  opacity: 0;
}

.featured__controls ul li:last-child {
  margin-right: 0;
}
</style>
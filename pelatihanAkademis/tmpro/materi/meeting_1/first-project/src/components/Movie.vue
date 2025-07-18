<template>
  <div class="movie-detail" @click="showDetail">
    <img :src="movieImage" alt="Movie" />
    <div class="coming-soon">
      <slot></slot>
    </div>
    <p>{{ movieTtile }}</p>
  </div>
</template>

<script>
import { eventBus } from "../main.js";

export default {
  props: ["movie"],
  data() {
    return {
      movieTtile: this.movie.title,
      movieImage: require(`../assets/${this.movie.imageName}`),
    };
  },
  methods: {
    showDetail() {
      eventBus.$emit("showDetailMovie", this.movie);
    },
  },
};
</script>

<style>
.movie-detail img {
  border-radius: 20px;
  width: 230px;
  height: 350px;
}

.movie-detail {
  margin: 7px;
  position: relative;
}

.movie-detail p {
  margin-top: 15px;
  font-weight: 1000;
}

.movie-detail:hover {
  cursor: pointer;
}

.coming-soon {
  position: absolute;
  background-color: rgba(153, 153, 153, 0.82);
  top: 0;
  width: 100%;
  font-size: 13px;
  border-radius: 20px 20px 0px 0px;
  text-align: center;
  color: white;
  padding-top: 0px;
}
</style>
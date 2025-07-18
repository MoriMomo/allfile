<template>
  <div class="row featured__filter">
    <!-- Component Item Here -->
    <movie-item
      :movie="data"
      v-for="data in movieData"
      :key="data.id"
    ></movie-item>
    <!-- {{ dataGenre }} -->
  </div>
</template>

<script>
import MovieItem from "./MovieItem.vue";

export default {
  data() {
    return {
      allMovie: [],
      movieData: [],
    };
  },
  components: {
    MovieItem,
  },
  created() {
    this.$http
      .get(
        "https://movie-review-a9730-default-rtdb.firebaseio.com/movieList.json"
      )
      .then((res) => {
        return res.json();
      })
      .then((data) => {
        const movieArray = [];
        for (let key in data) {
          movieArray.push({ ...data[key], id: key });
        }
        this.movieData = movieArray;
        this.allMovie = movieArray;
      });
  },
  props: {
    dataGenre: String,
  },
  watch: {
    dataGenre(newGenre) {
      if (newGenre !== "all") {
        const filterData = this.allMovie.filter((item) => {
          // console.log(item.genre == newGenre);
          return item.genre === newGenre;
        });
        this.movieData = filterData;
      } else {
        this.movieData = this.allMovie;
      }
    },
  },
};
</script>

<style>
</style>
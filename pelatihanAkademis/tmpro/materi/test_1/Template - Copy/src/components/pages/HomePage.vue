<template>
  <!-- Header Component -->
  <section class="featured">
    <div class="container">
      <div class="row">
        <div class="col-lg-12">
          <div class="section-title">
            <h2>Movie List</h2>
          </div>
          <!-- Genre Component -->
          <movie-genre @genreReturn="genre = $event"></movie-genre>
        </div>
      </div>
      <!-- Movie List Component -->
      <movie-list :dataGenre="genre"></movie-list>
    </div>
  </section>
</template>

<script>
import MovieGenre from "../MovieGenre.vue";
import MovieList from "../MovieList.vue";

export default {
  components: {
    MovieGenre,
    MovieList,
  },
  data() {
    return {
      genre: "",
    };
  },
  props: {},
};
</script>

<style>
.featured {
  padding-top: 30px;
  padding-bottom: 40px;
}
.section-title {
  margin-bottom: 20px;
  text-align: center;
}

.section-title h2 {
  color: #1c1c1c;
  font-weight: 700;
  position: relative;
}
</style>
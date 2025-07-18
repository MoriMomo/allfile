<template>
  <router-link
    :to="{
      name: 'Detail',
      params: { id: movie.id },
      query: {
        namaMovie: movie.namaMovie,
        image: movie.image,
        genre: movie.genre,
        release: movie.release,
        review: movie.review,
      },
    }"
    class="col-lg-3 col-md-4 col-sm-6"
  >
    <div class="featured__item">
      <img class="featured__item__pic" :src="movie.image" />
      <div class="featured__item__text">
        <h5>{{ movie.namaMovie }}</h5>
      </div>
    </div>
  </router-link>
</template>

<script>
export default {
  props: {
    movie: Object,
  },
};
</script>

<style>
.featured__item {
  margin-bottom: 50px;
}

.featured__item__pic {
  height: 330px;
  width: 270px;
  position: relative;
  overflow: hidden;
  background-position: center center;
}

.featured__item__text {
  text-align: center;
  padding-top: 15px;
}

.featured__item__text h6 {
  margin-bottom: 10px;
}

.featured__item__text h6 a {
  color: #252525;
}

.featured__item__text h5 {
  color: #252525;
  font-weight: 700;
}
</style>
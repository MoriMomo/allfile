<template>
  <div>
    <!-- Header -->
    <section class="blog-details-hero">
      <div class="container">
        <div class="row">
          <div class="col-lg-12">
            <div class="blog__details__hero__text">
              <h2>{{ getNamaMovie }}</h2>
              <ul>
                <li>{{ getGenre }}</li>
                <li>Rerelease: {{ getRelease }}</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </section>
    <!-- Blog Details Hero End -->

    <!-- Blog Details Section Begin -->
    <section class="blog-details">
      <div class="container">
        <div class="row">
          <div class="col-lg-8 col-md-4 blog__details__content">
            <div class="blog__details__text">
              <div class="blog__details__text__img">
                <img :src="getImage" alt="" />
              </div>
              <p>
                {{ getReview }}
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  computed: {
    getNamaMovie() {
      return this.$route.query.namaMovie;
    },
    getImage() {
      return this.$route.query.image;
    },
    getGenre() {
      return this.$route.query.genre;
    },
    getRelease() {
      return this.$route.query.release;
    },
    getReview() {
      return this.$route.query.review;
    },
  },
};
</script>

<style scoped>
.blog-details-hero {
  height: 350px;
  display: flex;
  align-items: center;
}

.blog__details__hero__text {
  text-align: center;
}

.blog__details__hero__text h2 {
  font-size: 46px;
  font-weight: 700;
  margin-bottom: 10px;
}

.blog__details__hero__text ul li {
  font-size: 16px;
  list-style: none;
  display: inline-block;
  margin-right: 45px;
  position: relative;
}

.blog__details__hero__text ul li:after {
  position: absolute;
  right: -26px;
  top: 0;
  content: "|";
}

.blog__details__hero__text ul li:last-child {
  margin-right: 0;
}

.blog__details__hero__text ul li:last-child:after {
  display: none;
}

.blog-details {
  padding-bottom: 75px;
  border-bottom: 1px solid #e1e1e1;
}

.blog__details__text {
  margin-bottom: 45px;
}

.blog__details__content {
  margin: 0px auto;
}

.blog__details__text__img {
  display: flex;
  justify-content: center;
  margin-bottom: 30px;
}

.blog__details__text__img img {
  width: 400px;
  height: 430px;
}

.blog__details__text p {
  font-size: 18px;
  line-height: 30px;
}

.blog__details__text h3 {
  color: #333333;
  font-weight: 700;
  line-height: 30px;
  margin-bottom: 30px;
}
</style>
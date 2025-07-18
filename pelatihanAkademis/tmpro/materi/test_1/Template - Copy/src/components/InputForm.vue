<template>
  <form>
    <div class="row">
      <div class="col-lg-4 col-md-4">
        <input
          type="text"
          placeholder="Movie Name"
          v-model="newMovie.namaMovie"
        />
      </div>
      <div class="col-lg-4 col-md-4">
        <input type="text" placeholder="Image Link" v-model="newMovie.image" />
      </div>
      <div class="col-lg-4 col-md-4">
        <input
          type="text"
          placeholder="Release Year"
          v-model="newMovie.release"
        />
      </div>
      <div class="genre__input__checkbox">
        <label>
          <input
            type="radio"
            name="genre"
            v-model="newMovie.genre"
            value="action"
          />
          Action
        </label>
        <label>
          <input
            type="radio"
            name="genre"
            v-model="newMovie.genre"
            value="sci-fi"
          />
          Science Fiction
        </label>
        <label>
          <input
            type="radio"
            name="genre"
            v-model="newMovie.genre"
            value="horror"
          />
          Horror
        </label>
        <label>
          <input
            type="radio"
            name="genre"
            v-model="newMovie.genre"
            value="thriller"
          />
          Thriller
        </label>
        <label>
          <input
            type="radio"
            name="genre"
            v-model="newMovie.genre"
            value="comedy"
          />
          Comedy
        </label>
        <label>
          <input
            type="radio"
            name="genre"
            v-model="newMovie.genre"
            value="romance"
          />
          Romance
        </label>
        <label>
          <input
            type="radio"
            name="genre"
            v-model="newMovie.genre"
            value="adventure"
          />
          Adventure
        </label>
        <label>
          <input
            type="radio"
            name="genre"
            v-model="newMovie.genre"
            value="fantasy"
          />
          Fantasy
        </label>
      </div>
      <div class="col-lg-12 text-center">
        <textarea
          placeholder="Your Review"
          v-model="newMovie.review"
        ></textarea>
        <button type="submit" v-on:click.prevent="newData" class="site-btn">
          Add Review
        </button>
      </div>
    </div>
  </form>
</template>

<script>
export default {
  data() {
    return {
      newMovie: {
        namaMovie: "",
        image: "",
        release: "",
        genre: "action",
        review: "",
      },
    };
  },
  methods: {
    newData() {
      this.$http
        .post(
          "https://movie-review-a9730-default-rtdb.firebaseio.com/movieList.json",
          this.newMovie
        )
        .then((res) => {
          this.$router.push("/");
        });
    },
  },
};
</script>
<!-- https://movie-review-a9730-default-rtdb.firebaseio.com/ -->
<style>
.genre__input input.genre__input__add {
  margin-bottom: 20px;
}

.genre__input input::placeholder {
  color: #b2b2b2;
}

.genre__input__checkbox {
  margin-bottom: 10px;
}

.genre__input__checkbox label {
  position: relative;
  font-size: 16px;
  color: #1c1c1c;
  padding-left: 30px;
  cursor: pointer;
}

.genre__input__checkbox label input {
  width: 20px;
  height: 20px;
}
</style>
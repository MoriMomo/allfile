<template>
  <div
    class="movie-list-detail"
    v-if="isDetailStatus"
    :style="{ backgroundImage: detailBackgroundImage }"
  >
    <div class="detail-img">
      <img :src="require(`../assets/${detailData.imageName}`)" alt="Movie" />
    </div>
    <div>
      <h1>{{ detailData.title }}</h1>
      <p>{{ detailData.synopsis }}</p>
    </div>
  </div>
</template>

<script>
import { eventBus } from "../main";
export default {
  data() {
    return {
      detailData: "",
      isDetailStatus: false,
      detailBackgroundImage: "",
    };
  },
  created() {
    eventBus.$on("showDetailMovie", (data) => {
      this.isDetailStatus = true;
      this.detailData = data;
      this.detailBackgroundImage = `linear-gradient(rgba(0,0,0,0.7),
            rgba(0,0,0,0.7)), url(${require("../assets/" +
              this.detailData.backgroundName)})`;
    });
  },
};
</script>

<style>
.movie-list-detail {
  height: 400px;
  color: white;
  margin-top: 50px;
  margin-bottom: 50px;
  padding: 100px 200px;
  display: flex;
  align-items: center;
}

.bg-movie-list-detail {
  display: flex;
  align-items: center;
}

.detail-img img {
  width: 280px;
  height: 400px;
  border-radius: 20px;
}

.detail-img {
  margin-right: 50px;
}
</style>
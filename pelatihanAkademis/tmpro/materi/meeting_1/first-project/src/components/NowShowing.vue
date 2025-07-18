<template>
  <div class="movies">
    <app-movie
      v-for="(data, index) in dataMovie"
      :movie="data"
      :key="index"
    ></app-movie>
  </div>
</template>

<script>
import Movie from "./Movie.vue";

export default {
  data() {
    return {
      dataMovie: [
        {
          title: "INANG",
          imageName: "movie1.jpg",
          backgroundName: "background-movie1.jpg",
          synopsis:
            "Wulan, seorang kasir supermarket ditinggalkan oleh pacarnya setelah mengetahui soal kehamilannya yang di luar rencana.Wulan yang enggan mengambil jalur aborsi, membuatnya harus bertanggung jawab atas kandungannya sendirian. Kurangnya wawasan yang dimiliki Wulan membuat pencarian solusi dimulai secara online. Pencarian Wulan membawanya ke sebuah grup di sosial media yang mengaku sebagai kelompok relawan pro-life yang fokus membantu ibu hamil yang mengalami situasi kurang beruntung.",
        },
        {
          title: "KALIAN PANTAS MATI",
          imageName: "movie2.jpg",
          backgroundName: "background-movie2.jpg",
          synopsis:
            "Seorang pemuda yang memiliki kemampuan untuk berkomunikasi dengan orang yang sudah meninggal. Dia harus menggunakan kemampuannya untuk menghentikan roh jahat yang dipenuhi dendam terhadap teman sekolahnya. Sementara itu dia bertekad untuk membantu sesosok hantu cantik untuk mengembalikan ingatannya.",
        },
        {
          title: "HALOWEEN ENDS",
          imageName: "movie3.jpg",
          backgroundName: "background-movie3.jpg",
          synopsis:
            "Berlatar 4 tahun dari Halloween Kills, Laurie yang tinggal bersama cucunya Allyson akan menghadapi Michael Myers untuk terakhir kalinya.",
        },
        {
          title: "PAMALI",
          imageName: "movie4.jpg",
          backgroundName: "background-movie4.jpg",
          synopsis:
            "Jaka Sunarya (Marthino Lio) yang baru saja kehilangan pekerjaan, bersama dengan sang istri, Rika (Putri Ayudya) ingin menjual rumah peninggalan orang tuanya untuk memulai hidup baru. Di desa tersebut, mereka tanpa sengaja melanggar adat yang telah menjadi tradisi, sehingga menghadapi keberadaan makhluk halus yang mengancam nyawa mereka.",
        },
      ],
    };
  },
  components: {
    "app-movie": Movie,
  },
};
</script>

<style>
</style>






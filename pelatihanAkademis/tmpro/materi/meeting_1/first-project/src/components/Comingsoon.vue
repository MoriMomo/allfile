<template>
  <div class="movies">
    <app-movie
      v-for="(data, index) in comingSoonMovie"
      :movie="data"
      :key="index"
    >
      <p>Cooming Sooon</p>
    </app-movie>
  </div>
</template>

<script>
import Movie from "./Movie.vue";

export default {
  data() {
    return {
      comingSoonMovie: [
        {
          title: "BLACK PANTHER: WAKANDA FOREVER",
          imageName: "coming-movie1.jpg",
          backgroundName: "background-coming-movie1.jpg",
          synopsis:
            "Rakyat Wakanda kali ini akan berjuang untuk melindungi negerinya dari campur tangan kekuatan dunia setelah kematian sang Raja T'Challa.",
        },
        {
          title: "SRI ASIH",
          imageName: "coming-movie2.jpg",
          backgroundName: "background-coming-movie2.jpg",
          synopsis:
            "Alana tidak mengerti mengapa dia selalu dikuasai oleh kemarahan. Tapi dia selalu berusaha untuk melawannya. Dia lahir saat letusan gunung berapi yang memisahkan dia dan orang tuanya. Dia kemudian diadopsi oleh seorang wanita kaya yang berusaha membantunya menjalani kehidupan normal. Tapi saat dewasa, Alana menemukan kebenaran tentang asalnya. Dia bukan manusia biasa. Dia bisa menjadi kebaikan untuk kehidupan. Atau menjadi kehancuran bila ia tidak dapat mengendalikan amarahnya.",
        },
        {
          title: "THE BANISHING",
          imageName: "coming-movie3.jpg",
          backgroundName: "background-coming-movie3.jpg",
          synopsis:
            "Kisah rumah paling berhantu di Inggris. Pada 1930-an, seorang pendeta muda, istri dan putrinya pindah ke rumah bangsawan dengan rahasia yang sangat mengerikan.",
        },
        {
          title: "KERAMAT 2: CARUBAN LARANG",
          imageName: "coming-movie4.jpg",
          backgroundName: "background-coming-movie4.jpg",
          synopsis:
            "Sekumpulan anak muda dari Jakarta berangkat menuju Cirebon. Arla, Jojo, Maura melakukan riset tugas akhir dibantu oleh Umay yang sedang membuat dokumenter. Sementara Ajil dan Keanu adalah YouTuber mistis yang sedang membuat konten untuk mempertahankan eksistensi. Perjalanan mereka menjadi liar dan tak terkendali setelah bertemu dengan Lutesha, seorang indigo yang mempunyai agenda rahasia.",
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






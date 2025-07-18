<template>
  <div>
    <nav></nav>
    <router-view />
  </div>
</template>

<script>
import axios from "axios";
import db from "./firebase/firebaseinit";
export default {
  name: "App",
  data() {
    return {
      APIkey: "7e813b6413f1d0386d8eba4e31fedca7", // Note: Exposing API keys in client-side code is not secure
      city: "Jakarta",
      cities: [],
      weather: null,
      error: null,
    };
  },
  created() {
    this.getCity();
  },
  methods: {
    async getCity() {
      let firebaseDB = db.collection("cities");

      firebaseDB.onSnapshot((snapshot) => {
        snapshot.docChanges().forEach(async (doc) => {
          await console.log(doc);
        });
      });
    },
    async getWeather() {
      const lat = 0.7893;
      const lon = 113.9213;

      try {
        const response = await axios.get(
          "https://api.openweathermap.org/data/2.5/weather",
          {
            params: {
              lat: lat,
              lon: lon,
              appid: this.APIkey,
              units: "metric",
            },
          }
        );
        this.weather = response.data;
        this.city = response.data.name;
      } catch (err) {
        console.error("Error:", err);
        this.error = "Failed to fetch weather data. Please try again later.";
      }
    },
  },
};
</script>
<style scoped>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: Arial, Helvetica, sans-serif;
}
</style>
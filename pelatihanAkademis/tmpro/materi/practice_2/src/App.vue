<template>
  <div>
    <!-- <app-input-form></app-input-form>
    <app-book-list></app-book-list> -->
    <router-view></router-view>
  </div>
</template>

<script>
import InputForm from "./components/InputForm.vue";
import BookList from "./components/BookList.vue";
export default {
  components: {
    "app-input-form": InputForm,
    "app-book-list": BookList,
  },
};
</script>

<style>
</style>
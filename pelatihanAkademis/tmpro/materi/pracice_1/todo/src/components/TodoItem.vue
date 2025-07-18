<template>
  <div class="todo">
    <h2 class="todo_description">{{ item.todo }}</h2>
    <p>{{ item.description }}</p>
    <a><i class="fa-regular fa-circle-check"></i></a>
    <a><i class="fa-solid fa-trash"></i></a>
  </div>
</template>

<script>
export default {
  props: ["item"],
};
</script>

<style>
</style>
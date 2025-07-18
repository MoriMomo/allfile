<template>
  <div>
    <input-todo> </input-todo>
    <todo-list :todoData="todos"> </todo-list>
  </div>
</template>

<script>
import InputTodo from "./components/InputTodo.vue";
import Todolist from "./components/TodoList.vue";
import { eventBus } from "./main.js";
export default {
  data() {
    return {
      todos: [],
    };
  },
  components: {
    "input-todo": InputTodo,
    "todo-list": Todolist,
  },
  created() {
    this.$http
      .get("https://todovue-d463a-default-rtdb.firebaseio.com/toDoList.json")
      .then((res) => {
        return res.json();
      })
      .then((ext) => {
        const resultArray = [];
        for (let key in ext) {
          resultArray.push(ext[key]);
        }
        this.todos = resultArray.reverse();
      });

    eventBus.$on("dataWasAdded", (data) => {
      console.log(data);
      this.todos.unshift(data);
    });
  },
};
</script>

<style>
/** Body Style **/
body {
  font-family: "Open Sans", sans-serif;
}
/** Form Style **/

/** Start Todo List **/

/** End Todo List*/
</style>
<template>
  <div class="todos_container">
    <div class="todo_list">
      <div class="todo-title">
        <h1>{{ todoTitle[0] }}</h1>
        <h1>5</h1>
      </div>
      <div class="todos">
        <TodoItem
          v-for="(todoStuff, index) in statusTodo"
          :key="index"
          :item="todoStuff"
        ></TodoItem>
      </div>
    </div>

    <div class="todo_list todo_center">
      <div class="todo-title">
        <h1>{{ todoTitle[1] }}</h1>
        <h1>5</h1>
      </div>
      <div class="todos">
        <TodoItem
          v-for="(todoStuff, index) in statusInProgress"
          :key="index"
          :item="todoStuff"
        >
        </TodoItem>
      </div>
    </div>

    <div class="todo_list">
      <div class="todo-title">
        <h1>{{ todoTitle[2] }}</h1>
        <h1>5</h1>
      </div>
      <div class="todos">
        <TodoItem
          v-for="(todoStuff, index) in statusComplete"
          :key="index"
          :item="todoStuff"
        ></TodoItem>
      </div>
    </div>
  </div>
</template>

<script>
import TodoItem from "../components/TodoItem.vue";
export default {
  components: {
    TodoItem,
  },
  data() {
    return {
      todoTitle: ["Todo", "In Progress", "Completed"],
    };
  },
  props: ["todoData"],
  computed: {
    statusComplete() {
      return this.todoData.filter((todo) => todo.status === "completed");
    },
    statusInProgress() {
      return this.todoData.filter((todo) => todo.status === "ongoing");
    },
    statusTodo() {
      return this.todoData.filter((todo) => todo.status === "todo");
    },
  },
};
</script>

<style>
.todos {
  display: flex;
  flex-direction: column;
}

.todo {
  width: 210px;
  border: 1px solid #aaa;
  height: 180px;
  border-radius: 5px;
  margin: 15px;
  padding: 5px 20px;
  position: relative;
}

.todo_description {
  margin-top: 0px;
  margin-bottom: 2px;
}

.fa-circle-check {
  position: absolute;
  bottom: 20px;
  right: 20px;
}

.fa-circle-check:hover {
  cursor: pointer;
  color: green;
}

.fa-trash {
  position: absolute;
  bottom: 20px;
  right: 45px;
}

.fa-trash:hover {
  color: red;
  cursor: pointer;
}

.todos_container {
  display: flex;
  justify-content: center;
  margin-top: 35px;
  margin-bottom: 35px;
}

.todo_list {
  border: 0;
  box-shadow: 0 0 15px 4px rgba(0, 0, 0, 0.06);
  padding-left: 10px;
  padding-right: 10px;
  border-radius: 15px;
}

.todo_center {
  margin-right: 40px;
  margin-left: 40px;
}

.todo-title {
  display: flex;
  justify-content: space-between;
  margin: 15px 20px 0px 20px;
  color: #3f51b5;
}

.todo-title h1 {
  font-size: 20px;
  margin: 0px;
}

.todo-title h1:last-child {
  color: white;
  background-color: #3f51b5;
  padding-left: 9px;
  padding-right: 9px;
  padding-top: 4px;
  border-radius: 50px;
  font-size: 13px;
}
</style>
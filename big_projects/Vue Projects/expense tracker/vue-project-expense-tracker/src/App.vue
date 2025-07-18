<template>
  <div id="app">
    <Header />
    <Balance :total="total" />
    <IncomeExp :income="income" :expenses="expense" />
    <TransactList
      :transactions="transactions"
      @transactionDeleted="handleTransactionDeleted"
    />
    <AddTransact @transactionSubmitted="handleTransactionSubmitted" />
  </div>
</template>

<script setup>
import Header from "./components/Header.vue";
import Balance from "./components/Balance.vue";
import IncomeExp from "./components/IncomeExp.vue";
import AddTransact from "./components/AddTransact.vue";
import TransactList from "./components/TransactList.vue";

import { ref, computed } from "vue";
import { useToast } from "vue-toastification";

const toast = useToast();

const transactions = ref([
  { id: 1, text: "Income", amount: 500 },
  { id: 2, text: "flower", amount: -500 },
  { id: 3, text: "book", amount: 500 },
  { id: 4, text: "camera", amount: -500 },
  { id: 5, text: "expense", amount: 500 },
]);

// Get total
const total = computed(() => {
  return transactions.value.reduce((acc, transaction) => {
    return acc + transaction.amount;
  }, 0);
});

// Income
const income = computed(() => {
  return transactions.value
    .filter((transaction) => transaction.amount > 0)
    .reduce((acc, transaction) => {
      return acc + transaction.amount;
    }, 0);
});

// Expenses
const expense = computed(() => {
  return transactions.value
    .filter((transaction) => transaction.amount < 0)
    .reduce((acc, transaction) => {
      return acc + transaction.amount;
    }, 0);
});

const handleTransactionSubmitted = (transactionData) => {
  transactions.value.push({
    id: generateUniqueId(),
    text: transactionData.text,
    amount: transactionData.amount,
  });

  // saveTransactionsToLocalStorage();

  toast.success("Transaction added.");
};

// Generate unique ID
const generateUniqueId = () => {
  return Math.floor(Math.random() * 1000000);
};

// Delete transaction
const handleTransactionDeleted = (id) => {
  transactions.value = transactions.value.filter(
    (transaction) => transaction.id !== id
  );

  // saveTransactionsToLocalStorage();
  toast.success("Transaction deleted.");
};
</script>

<style>
/* Your styles here */
</style>
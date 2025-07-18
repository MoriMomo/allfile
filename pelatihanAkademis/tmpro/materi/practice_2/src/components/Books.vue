<template>
    <div>
        <app-book-list>
            <h1>Selesai Dibaca</h1>
        </app-book-list>

        <app-book-list>
            <h1>Belum Selesai Dibaca</h1>
        </app-book-list>
    </div>
</template>

<script>
    import BookList from './BookList.vue'
    export default {
        components: {
            'app-book-list': BookList
        }
    }
</script>

<style>

</style>
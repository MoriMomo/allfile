import Home from "./components/pages/HomePage.vue";
import AddBookPage from './components/pages/AddBookPage.vue';
import DetailPage from "./components/pages/DetailPage.vue"


export const routes = [
    { path: '/', name: 'home', component: Home },
    { path: '/add', name: 'add', component: AddBookPage },
    { path: '/detail/:id', name: 'detailPage', component: DetailPage }
]
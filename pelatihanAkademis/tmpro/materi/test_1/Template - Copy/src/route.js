import Home from "./components/pages/HomePage.vue";
import NewMovie from "./components/pages/NewMoviePage.vue"
import Detail from "./components/pages/MovieDetailPage.vue";

export const routes = [
    { path: '/', name: 'home', component: Home },
    { path: '/NewMovie', name: 'NewMovie', component: NewMovie },
    { path: '/NewMovie/:id', name: 'Detail', component: Detail }
]
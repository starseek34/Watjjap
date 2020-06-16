import Vue from 'vue'
import VueRouter from 'vue-router'

import Home from '../views/Home.vue'
import Modal from '../components/Modal.vue'

// movies
import RecommendMovieView from '../views/movies/RecommendMovieView.vue'
import MovieSearchListView from '../views/movies/MovieSearchListView.vue'
import MovieDetailView from '../views/movies/MovieDetailView.vue'

// accounts
import MyPageView from '../views/accounts/MyPageView.vue'

Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/home',
    name: 'Home2',
    component: Home,
  },
  {
    path: '/modal',
    name: 'Modal',
    component: Modal,
  },
  {
    path: '/movies/recommend',
    name: 'RecommendMovie',
    component: RecommendMovieView,
  },
  {
    path: '/accounts/mypage',
    name: 'MyPage',
    component: MyPageView,
  },
  {
    path: '/movies/search/:inputValue',
    name: 'MovieSearchList',
    component: MovieSearchListView,
  },
  {
    path: '/movies/detail',
    name: 'MovieDetail',
    component: MovieDetailView,
    props: {movie: false}
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

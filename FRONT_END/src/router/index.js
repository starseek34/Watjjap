import Vue from 'vue'
import VueRouter from 'vue-router'

import Home from '../views/Home.vue'

// movies
import RecommendMovieView from '../views/movies/RecommendMovieView.vue'
import MovieSearchListView from '../views/movies/MovieSearchListView.vue'

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
    path: '/movies/search',
    name: 'MovieSearchList',
    component: MovieSearchListView,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router

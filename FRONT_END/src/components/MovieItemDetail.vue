<template>
  <div class="card" style="width: 12rem;">
    <img :src="poster" class="card-img-top" alt="...">
    <div class="card-body">
      <h5 class="card-title">{{ title }}</h5>
      <h6 class="card-subtitle mb-2 text-muted">{{ movie.director }} {{ movie.pubDate }}</h6>
      <p class="card-text"> Naver 평점 : {{movie.userRating}}</p>
      <button class="btn btn-primary" @click='detail'>Detail</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = 'http://127.0.0.1:8000/movies/save_movie/'


export default {
  name: 'MovieItemDetail',
  props: {
    movies: Array,
    movie: Object,
  },
  data() {
    return{
      movieId: ''
    }
  },
  methods: {
    detail() {
      axios.post(SERVER_URL, this.movie)
        .then(res =>{
          this.movieId = res.data['id']
          console.log('movies/detail/'+this.movieId)
          this.$router.push('/movies/detail/'+this.movieId)
        })
    },
  },
  computed: {
    poster(){
      return this.movie.image
    },
    title(){
      return this.movie.title.replace(/(<([^>]+)>)/ig,"")
    }
  }
}
</script>

<style>

</style>
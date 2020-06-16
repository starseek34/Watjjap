<template>
  <div>
    <div>
      <p class="text-center">"어디에서, 어떻게, 누구와 보는가가 영화의 완성이다." -왕가위</p>
      <RecommendSelectBox />
    </div>
        <MovieItem :movies='movies'/>
  </div>
</template>

<script>
import axios from 'axios'

import RecommendSelectBox from '../../components/RecommendSelectBox.vue'
import MovieItem from '../../components/MovieItem.vue'

const SERVER_URL = 'http://127.0.0.1:8000/movies/search_genre/rand/'

export default {
  name: 'RecommendMovieView',
  components: {
    RecommendSelectBox,
    MovieItem
  },
  data(){
    return{
      movies: []
    }
  },
  mounted (){
    axios.get(SERVER_URL)
      .then(res => this.movies = res.data)
      .catch(err => console.error(err))
  },
}
</script>

<style>

</style>
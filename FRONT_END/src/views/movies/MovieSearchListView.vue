<template>
  <div>
    <h2>검색 결과</h2>
    <MovieItem :movies='movies'/>
  </div>
</template>

<script>
import axios from 'axios'

import MovieItem from '../../components/MovieItem.vue'

const SERVER_URL = 'http://127.0.0.1:8000/movies/search/'

export default {
  name: 'MovieSearchListView',
  components: {
    MovieItem,
  },
  props:{
    inputValue: String
  },
  data(){
    return {
      inputValue : '',
      movies: []
    }
  },
  mounted (){
    axios.get(SERVER_URL+this.$route.params.inputValue)
      .then(res => this.movies = res.data)
      .catch(err => console.error(err))
  },
  watch:{
    '$route'(to, from){
      console.log(to, from)
      axios.get(SERVER_URL+this.$route.params.inputValue)
        .then(res => this.movies = res.data)
        .catch(err => console.error(err))
    }
  },
  computed:{
    movies(inputValue){
      this.searchValue = inputValue
      axios.get(SERVER_URL+this.searchValue)
        .then(res => this.movies = res.data)
        .catch(err => console.error(err))
      return this.movies
    }
  }

}
</script>

<style>

</style>
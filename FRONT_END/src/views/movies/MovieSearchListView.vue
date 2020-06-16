<template>
  <div>
    <h2>검색 결과</h2>
    <!-- <SearchBar @input-change='search' /> -->
    <MovieItem :movies='movies'/>
  </div>
</template>

<script>
import axios from 'axios'

import MovieItem from '../../components/MovieItem.vue'
import SearchBar from '../../components/SearchBar.vue'

const SERVER_URL = 'http://127.0.0.1:8000/movies/search/'

export default {
  name: 'MovieSearchListView',
  components: {
    MovieItem,
    SearchBar,
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
  methods: {
    search(inputText){
      this.inputValue = inputText
      axios.get(SERVER_URL+this.inputValue)
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
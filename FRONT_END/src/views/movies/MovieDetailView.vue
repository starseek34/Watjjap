<template>
  <div>
    <MovieDetailItem :movieInfo='movieInfo'/>
  </div>
</template>

<script>
import axios from 'axios'

import MovieDetailItem from '../../components/MovieDetailItem.vue'

const SERVER_URL = 'http://127.0.0.1:8000/movies/save_movie/'

export default {
  name: 'MovieDetailView',
  components:{
    MovieDetailItem,
  },
  data(){
    return{
      apiInfo : this.$route.params.movie,
      movieInfo : {},
    }
  },
  mounted(){
    axios.post(SERVER_URL, this.apiInfo, )
      .then(res => this.movieInfo = res.data)
      .catch(err => console.error(err))
  }
}
</script>

<style>

</style>
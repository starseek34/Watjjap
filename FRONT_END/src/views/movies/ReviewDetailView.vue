<template>
  <div>
    <h2>{{review}}</h2>
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = 'http://127.0.0.1:8000/movies/'

export default {
  name: 'ReviewDetailView',
  data() {
    return {
      review: {},
    }
  },
  mounted(){
    axios.get(SERVER_URL + this.$route.params.movieId + '/reviews/' + this.$route.params.reviewId + '/')
      .then(res => {
        this.review = res.data
      })
      .catch(err => console.error(err))
  },

}
</script>

<style>

</style>
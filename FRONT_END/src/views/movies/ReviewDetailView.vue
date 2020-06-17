<template>
  <div class="row">
    <div class="col m-3 bg-light">
      <i class="fa fa-user-circle-o" style="font-size:40px;" aria-hidden="true"></i>
      <h5>{{ review.user.username }}</h5>
      <hr>
      <p>{{ review.content }}</p>
      <hr>
      <div>
        <i class="fa fa-thumbs-up m-1" aria-hidden="true">3143</i>
        <i class="fa fa-comments m-1" aria-hidden="true">30</i>
      </div>
      <hr>
      <p class="m-2 stretched-link font-weight-bold" style="position: relative; color:#f71972; cursor:pointer;">좋아요</p>
    </div>
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
<template>
  <div class="row">
    <div @click="reviewDetail" class="col m-3 bg-light">
      <i class="fa fa-user-circle-o" style="font-size:40px;" aria-hidden="true"></i>
      <h5>{{ review.user.username }}</h5>
      <p class="font-weight-bold">{{ review.title }}</p>
      
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
export default {
  name: 'MovieReview',
  props: {
    review: Object,
  },
  data() {
    return {
      reviewId: '',
    }
  },
  methods: {
    reviewDetail() {
      this.reviewId = this.review.id
      this.$router.push('/movies/detail/'+this.$route.params.movieId+'/'+this.reviewId)
    }
  }
}
</script>

<style>

</style>
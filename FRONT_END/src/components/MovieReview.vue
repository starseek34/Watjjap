<template>
  <div class="col-6">
    <h5>{{ review.user.nickname }}</h5>
    <hr>
    <p>{{ review.content }}</p>
    <hr>
    <p>
      <i class="fa fa-thumbs-up" aria-hidden="true">3143</i>
      <i class="fa fa-comments" aria-hidden="true">30</i>
  </p>
    <hr>
    <p>좋아요</p>
  </div>
</template>

<script>
export default {
  name: 'MovieReview',
  props: {
      review: Object,
  },
}
</script>

<style>

</style>
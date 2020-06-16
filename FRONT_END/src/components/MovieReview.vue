<template>
  <div class="col-6">
    <h5>{{ review.user.nickname }}</h5>
    <hr>
    <p>{{ review.content }}</p>
    <hr>
    <p>엄지 3143 댓글 30</p>
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
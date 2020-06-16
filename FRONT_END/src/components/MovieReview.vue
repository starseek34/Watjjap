<template>
  <div class="col-6">
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
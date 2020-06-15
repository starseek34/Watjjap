<template>
  <div>
    <h2>코멘트 20000+</h2>
    <p>더보기</p>
    <div v-for="review in reviews" :key="review.id">
      {{ review }}
    </div>
  </div>
</template>

<script>
export default {
  name: 'MovieReview',
  props: {
      reviews: Array,
  },
}
</script>

<style>

</style>
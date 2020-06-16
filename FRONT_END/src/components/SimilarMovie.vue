<template>
  <div class="col-2">
    <img :src="poster" alt="영화포스터_비슷한작품">
    <h5>{{ similarMovie.title }}</h5>
    <p>평점 - {{ similarMovie.userRating }}</p>
  </div>
</template>

<script>
export default {
  name: 'SimilarMovie',
  props: {
    similarMovie : Object,
  },
  computed: {
    poster(){
      return this.similarMovie.image
    },
    // title(){
    //   return this.movie.title.replace(/(<([^>]+)>)/ig,"")
    // }
  }
}
</script>

<style>

</style>
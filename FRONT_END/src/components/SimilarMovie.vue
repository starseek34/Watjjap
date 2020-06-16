<template>
  <div class="col-2">
    <img :src="poster" @error='imageError = true' alt="영화포스터_비슷한작품">
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
  data(){
    return{
      imageError : false,
      defaultImage : require('../assets/movie_poster_default.jpg')
    }
  },
  computed: {
    poster(){
      return this.imageError ? this.defaultImage : this.similarMovie.image
    },
    // title(){
    //   return this.movie.title.replace(/(<([^>]+)>)/ig,"")
    // }
  }
}
</script>

<style>

</style>
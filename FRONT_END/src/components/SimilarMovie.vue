<template>
  <div class="col-2 m-3 p-2 card">
    <img :src="poster" @error='imageError = true' alt="영화포스터_비슷한작품">
    <div class="card-body">
      <h5 class="card-title">{{ title }}</h5>
      <p class="card-text">평점 - {{ similarMovie.userRating }}</p>
    </div>
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
    title(){
      return this.similarMovie.title.replace(/(<([^>]+)>)/ig,"")
    }
  }
}
</script>

<style>

</style>
<template>
  <div>
    <img :src='poster' alt="poster of movie">
    {{ movie.title|safe }} ( {{ movie.pubDate }} ) : {{ movie.director }} : {{ movie.actor }} 평점 : {{ movie.userRating }}
  </div>
</template>

<script>
export default {
  name: 'MovieItemDetail',
  props: {
    movie: Object,
  },
  computed:{
    poster(){
      return this.movie.image
    },
    naverLink(){
      return this.movie.link
    }
  }
}
</script>

<style>

</style>
<template>
  <div class="card" style="width: 18rem;">
    <img :src="poster" class="card-img-top" alt="...">
    <div class="card-body">
      <h5 class="card-title">{{ movie.title }}</h5>
      <h6 class="card-subtitle mb-2 text-muted">{{ movie.director }} {{ movie.pubDate }}</h6>
      <p class="card-text">{{movie.userRating}}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MovieItemDetail',
  props: {
    movie: Object,
  },
  computed: {
    poster(){
      return this.movie.image
    }
  }
}
</script>

<style>

</style>
<template>
  <div class="card" style="width: 18rem;">
    <img :src="poster" class="card-img-top" alt="...">
    <div class="card-body">
      <h5 class="card-title">{{ newTitle }}</h5>
      <h6 class="card-subtitle mb-2 text-muted">{{ newDirector }} {{ movie.pubDate }}</h6>
      <p class="card-text"> Naver 평점 : {{movie.userRating}}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MovieItemDetail',
  props: {
    movie: Object,
  },
  data(){
    return{
      newTitle : this.movie.title.replace(/(<([^>]+)>)/ig,""),
    }
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
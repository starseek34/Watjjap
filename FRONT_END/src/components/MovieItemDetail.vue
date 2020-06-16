<template>
  <div class="card" style="width: 12rem;">
    <img :src="poster" class="card-img-top" alt="...">
    <div class="card-body">
      <h5 class="card-title">{{ title }}</h5>
      <h6 class="card-subtitle mb-2 text-muted">{{ movie.director }} {{ movie.pubDate }}</h6>
      <p class="card-text"> Naver 평점 : {{movie.userRating}}</p>
      <button class="btn btn-primary" @click='detail'>Detail</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MovieItemDetail',
  props: {
    movies: Array,
    movie: Object,
  },
  methods: {
    detail() {
      this.$router.push({name:'MovieDetail', params:{movie: this.movie}})
    },
  },
  computed: {
    poster(){
      return this.movie.image
    },
    title(){
      return this.movie.title.replace(/(<([^>]+)>)/ig,"")
    }
  }
}
</script>

<style>

</style>
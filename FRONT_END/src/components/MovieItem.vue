<template>
  <div class="row m-3">
    <MovieItemDetail :movie='movie' v-for='movie in movies' :key='movie.id' />
  </div>
</template>

<script>
import MovieItemDetail from './MovieItemDetail.vue'

export default {
  name: 'MovieItem',
  components: {
    MovieItemDetail
  },
  props: {
    movies: Array,
  },
  methods: {}
}
</script>

<style>

</style>
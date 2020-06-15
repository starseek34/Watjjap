<template>
  <div>
    <ul class="class">
      <MovieItemDetail :movie='movie' v-for='movie in movies' :key='movie.id' />
    </ul>
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
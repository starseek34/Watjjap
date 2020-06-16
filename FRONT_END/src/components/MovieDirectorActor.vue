<template>
  <div class="row">
    <div class="col-6">
      <h3>{{ director }}</h3>
      <p>감독</p>
    </div>
    <div class="col-6" v-for="actor in actors" :key="actor.id">
      <h3>{{ actor }}</h3>
      <p>주연</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MovieDirectorActor',
  props: {
    movieInfo: Object,
  },
  computed: {
    director() {
      return this.movieInfo.director.replace('|', '')
    },
    actors() {
      return this.movieInfo.actor.split('|', 5)
    }
  }
}
</script>

<style>

</style>
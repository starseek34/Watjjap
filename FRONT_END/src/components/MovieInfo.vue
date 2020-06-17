<template>
  <div class="m-1">
    <h2 class="m-3">기본정보</h2>
    <div class="m-3">
      <h4>{{ title }}</h4>
      <h5>{{ movieInfo.pubDate }} {{ country }} {{ genre }}</h5>
      <h5>{{ movieInfo.runningTime }}</h5>
    </div>
    <div class="m-3">
      <p>{{ plot }}</p>
    </div>
  </div>

</template>

<script>
export default {
  name: 'MovieInfo',
  props: {
    movieInfo: Object,
  },
  computed: {
    title() {
      return this.movieInfo.title.replace(/(<([^>]+)>)/gi,"")
    },
    plot() {
      return this.movieInfo.plot.replace(/(<([^>]+)>)/gi,"")
    },
    genre() {
      return this.movieInfo.genre.slice(0, -1)
    },
    country() {
      return this.movieInfo.country.replace(/[^가-힣]/gi, "")
    },
  }
}
</script>

<style>

</style>
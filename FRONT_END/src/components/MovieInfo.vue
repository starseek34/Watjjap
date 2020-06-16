<template>
  <div>
    <h2>기본정보</h2>
    <h3>{{ title }}</h3>
    <h4>{{ movieInfo.pubDate }} {{ country }} {{ genre }}</h4>
    <h4>{{ movieInfo.runningTime }}</h4>
    <p>{{ plot }}</p>
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
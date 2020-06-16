<template>
  <div>
    <h2>기본정보</h2>
    <h3>{{ title }}</h3>
    <h4>{{ movieInfo.pubDate }} {{ movieInfo.country }} {{ movieInfo.genre }}</h4>
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
    }
  }
}
</script>

<style>

</style>
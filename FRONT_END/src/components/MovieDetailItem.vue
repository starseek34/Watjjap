<template>
  <div>
    MovieDetail
    {{ movieInfo }}
  </div>

</template>

<script>
export default {
  name: 'MovieDetailItem',
  props:{
    movieInfo: Object,
  }
}
</script>

<style>

</style>
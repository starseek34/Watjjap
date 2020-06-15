<template>
  <div>
    <h2>검색 결과</h2>
    <SearchBar @input-change='search' />
    <MovieItem />
  </div>
</template>

<script>
export default {
  name: 'MovieSearchListView'
}
</script>

<style>

</style>
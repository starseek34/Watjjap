<template>
  <div>
    <h2>검색 결과</h2>
    <router-link :to="{ name: 'MovieDetail' }">
      <div>
        <img src="../../assets/logo.png" alt="영화포스터_검색결과">
        <h4>기생충</h4>
        <p>2019 - 한국</p>
        <p>감독 - 봉준호</p>
        <p>평점 - 4.5</p>
      </div>
    </router-link>
  </div>
</template>

<script>
export default {
  name: 'MovieSearchListView'
}
</script>

<style>

</style>
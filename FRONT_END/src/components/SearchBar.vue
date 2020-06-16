<template>
  <div>
    <input @keypress.enter="onInput" type="text"  class="form-control" placeholder="작품 제목을 검색해보세요.">
  </div>
</template>

<script>
export default {
  name: 'SearchBar',

  methods: {
    onInput(event) {
      this.$router.push('/movies/search/'+event.target.value)
    },
  },
  
}
</script>

<style>

</style>
<template>
  <div>
    <input @keypress.enter="onInput" type="text"  class="form-control" placeholder="작품 제목, 배우, 감독을 검색해보세요.">
  </div>
</template>

<script>
export default {
  name: 'SearchBar',

  methods: {
    onInput(event) {
      this.$emit('input-change', event.target.value)
      this.$router.push({ name: 'MovieSearchList' })
    },
  },
  
}
</script>

<style>

</style>
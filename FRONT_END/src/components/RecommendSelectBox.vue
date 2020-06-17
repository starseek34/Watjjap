<template>
  <div class="row m-3">
    <select @change='search_genre' id='genre' class="custom-select">
      <option selected>당신을 위한 랜덤추천!</option>
      <option value="드라마">드라마</option>
      <option value="판타지">판타지</option>
      <option value="서부">서부</option>
      <option value="공포">공포</option>
      <option value="로맨스">로맨스</option>
      <option value="모험">모험</option>
      <option value="스릴러">스릴러</option>
      <option value="느와르">느와르</option>
      <option value="컬트">컬트</option>
      <option value="다큐멘터리">다큐멘터리</option>
      <option value="코미디">코미디</option>
      <option value="가족">가족</option>
      <option value="미스터리">미스터리</option>
      <option value="전쟁">전쟁</option>
      <option value="애니메이션">애니메이션</option>
      <option value="범죄">범죄</option>
      <option value="SF">SF</option>
      <option value="액션">액션</option>
      <option value="무협">무협</option>
      <option value="에로">에로</option>
      <option value="서스펜스">서스펜스</option>
    </select>
  </div>

</template>

<script>
export default {
  name: 'RecommendSelectBox',
  methods : {
    search_genre(){
      console.log(document.getElementById('genre').value)      
      this.$emit('search_genre', document.getElementById('genre').value)
    }
  }
}
</script>

<style>

</style>
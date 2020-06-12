<template>
  <div>
    <a href="#">설정</a>
    <h3>프로필 사진</h3>
    <h4>닉네임</h4>
    <p>프로필이 없습니다.</p>
    <hr>
    <h5>취향분석</h5>
    <hr>
    <router-link :to="{ name: 'RecommendMovie'}">
      <div class="btn btn-success">
        <h5>영화</h5>
        <p>*</p>
        <p>304</p>
      </div>
    </router-link>

  </div>
</template>

<script>
export default {
  name: 'MyPageView',
}
</script>

<style>

</style>
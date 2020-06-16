<template>
  <div>
    <div>
      <h3 class="text-center">304</h3>
      <p class="text-center">"어디에서, 어떻게, 누구와 보는가가 영화의 완성이다." -왕가위</p>
      <RecommendSelectBox />
    </div>
    <div>
      <img src="" alt="영화포스터_추천영화">
      <p>신과 함께: 인과 연</p>
      <p>2017-한국</p>
      <p>***</p>
    </div>
  </div>
</template>

<script>
import RecommendSelectBox from '../../components/RecommendSelectBox.vue'

export default {
  name: 'RecommendMovieView',
  components: {
    RecommendSelectBox,
  },
}
</script>

<style>

</style>
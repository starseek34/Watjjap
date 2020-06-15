<template>
  <div>
    <div class="row">
      <img src="" alt="영화포스터_헤더">
    </div>
    <MovieInfo />

    <div class="row">
      <CreateReview />
      <div>
        <h2>기본정보</h2>
        <h3>기생충</h3>
        <p>이 영화는 ~~~ 영화 줄거리</p>
        <p>러닝타임</p>
      </div>
      <div>
        영화 예고편 동영상
      </div>
      <div>
        <hr>
        <h2>기본정보</h2>
        <p>더보기</p>
        <p>기생충</p>
        <p>2019 한국 드라마</p>
        <p>2시간 11분</p>
        <p>줄거리~~</p>
        <hr>
        <h2>출연/제작</h2>
        <p>감독 배우 프사들</p>
      </div>
      <div>
        영화 예고편 동영상
      </div>
      <hr>
      <div>
        <h2>코멘트 20000+</h2>
        <p>더보기</p>
        <div>
          리뷰들
        </div>
      </div>
      <hr>
      <div>
        포스터 사진들
      </div>
    </div>
  </div>
</template>

<script>
import MovieInfo from '../../components/MovieInfo.vue'
import CreateReview from '../../components/CreateReview.vue'

export default {
  name: 'MovieDetailView',
  components: {
    MovieInfo, CreateReview,
  },
  data() {
    return {
      
    }
  },
  // props: {
  //   movie: Object,
  // },
  computed: {
    poster() {
      return this.movie.poster_url
    }
  }

}
</script>

<style>

</style>
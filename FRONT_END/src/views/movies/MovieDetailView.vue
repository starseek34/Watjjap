<template>
  <div>
    <div class="row">
      <img src="" alt="영화포스터_헤더">
    </div>
    <div class="row">
      <div class="col">
        <img src="" alt="영화포스터_상세보기">
      </div>
      <div class="col">
        <h2>기생충</h2>
        <h3>2019 - 드라마 - 한국</h3>
        <p>평점 * 4.3점</p>
        <hr>
        <h4>당신의 평점 ****</h4>
      </div>
    </div>

    <div>
      <CreateReview />
      <MovieInfo />
      <MovieDirectorActor />
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
// import axios from 'axios'

import MovieInfo from '../../components/MovieInfo.vue'
import CreateReview from '../../components/CreateReview.vue'
import MovieDirectorActor from '../../components/MovieDirectorActor.vue'

// const SERVER_URL = 'http://127.0.0.1:8000/movies/1'

export default {
  name: 'MovieDetailView',
  components: {
    MovieInfo, CreateReview, MovieDirectorActor,
  },
  data() {
    return {
      inputValue: '',
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
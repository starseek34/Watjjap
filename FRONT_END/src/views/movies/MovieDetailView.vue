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

    <!-- <div>
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
    </div> -->
    <MovieDetailItem :movieInfo='movieInfo'/>
  </div>
</template>

<script>
import axios from 'axios'

import MovieDetailItem from '../../components/MovieDetailItem.vue'

const SERVER_URL = 'http://127.0.0.1:8000/movies/save_movie/'

export default {
  name: 'MovieDetailView',
  components:{
    MovieDetailItem,
  },
  data(){
    return{
      apiInfo : this.$route.params.movie,
      movieInfo : {},
    }
  },
  mounted(){
    axios.post(SERVER_URL, this.apiInfo, )
      .then(res => this.movieInfo = res.data)
      .catch(err => console.error(err))
  }
}
</script>

<style>

</style>
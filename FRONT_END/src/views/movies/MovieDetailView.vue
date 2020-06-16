<template>
  <div>
    <div>
      <div class="row">
        <div class="col-4 d-flex justify-content-end m-3">
          <img :src="poster" @error='imageError = true' alt="영화포스터_상세보기">
        </div>
        <div class="col-6 m-3">
          <h2>{{ title }}</h2>
          <h3>{{ movieInfo.pubDate }} - {{ genre }} - {{ country }}</h3>
          <h5>평점 ★ {{ movieInfo.userRating }}점</h5>
        </div>
      </div>
    </div>
    <div>
      <div class="row">
        <div class="col-8">
          <CreateReview :movieInfo='movieInfo' />
          <hr>
          <MovieInfo :movieInfo='movieInfo' />
          <hr>
          <h2>출연/제작</h2>
          <MovieDirectorActor :movieInfo='movieInfo' />
        </div>
        <div class="col-4">
          <MovieTrailer :video="video" v-for="video in videos" :key="video.etag" />
        </div>
      </div>
      <hr>
      <div class="row">
        <h2 class="col-11">코멘트</h2>
        <h5 @click="isTotalReviews" class="col-1 stretched-link font-weight-bold" style="position: relative; color:#f71972; cursor:pointer;">더보기</h5>
        <h4 class="col-2">총 {{ reviewCount }}개</h4>
      </div>
      <div class="row">
        <MovieReview :review="review" v-for="review in changeReviews" :key="review.id"/>
      </div>
      <hr>
      <h2>비슷한 작품</h2>
      <div class="row">
        <SimilarMovie :similarMovie="similarMovie" v-for="similarMovie in similarMovies" :key="similarMovie.title" />
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

import CreateReview from '../../components/CreateReview.vue'
import MovieInfo from '../../components/MovieInfo.vue'
import MovieDirectorActor from '../../components/MovieDirectorActor.vue'
import MovieTrailer from '../../components/MovieTrailer.vue'
import MovieReview from '../../components/MovieReview.vue'
import SimilarMovie from '../../components/SimilarMovie.vue'

const SERVER_URL = 'http://127.0.0.1:8000/movies/'

const API_KEY = 'AIzaSyDOcU2YV3kprnZTh1piCpd1PJdiAN1i8vc'
const API_URL = 'https://www.googleapis.com/youtube/v3/search'

export default {
  name: 'MovieDetailView',
  components:{
    CreateReview, MovieInfo, MovieDirectorActor, MovieTrailer, MovieReview, SimilarMovie, 
  },
  data(){
    return{
      similarMovies : [],
      movieInfo : {},
      videos : [],
      reviews : [],
      imageError : false,
      defaultImage: require('../../assets/movie_poster_default.jpg'),
      reviewFlag : false,
    }
  },
  methods:{
    more_review(){
      this.$router.push('/movies/detail/'+this.movieInfo.id+'/review')
    },
    isTotalReviews() {
      this.reviewFlag = !this.reviewFlag
    }
  },
  mounted(){
    axios.get(SERVER_URL + this.$route.params.movieId + '/')
      .then(res => {
        this.movieInfo = res.data

        const movieTitle = this.movieInfo.title.replace(/(<([^>]+)>)/gi,"")

        axios.get(API_URL, {
            params: {
                key: API_KEY,
                part: "snippet",
                type: "video",
                q: movieTitle + " trailer"
            }
        })
          .then(res => {
            this.videos = res.data.items
          })
          .catch(err => console.error(err))

        const oneGenre = this.movieInfo.genre.split('/')[0]

        axios.get(SERVER_URL + 'search_genre/' + oneGenre + '/')
          .then(res => {
            this.similarMovies = res.data
          })
          .catch(err => console.error(err))
      })
      .catch(err => console.error(err))

    axios.get(SERVER_URL + this.$route.params.movieId + '/reviews/')
      .then(res => {
        this.reviews = res.data
      })
      .catch(err => console.error(err))
  },
  computed: {
    poster(){
      return this.imageError ? this.defaultImage : this.movieInfo.image
    },
    title(){
      return this.movieInfo.title.replace(/(<([^>]+)>)/gi,"")
    },
    genre() {
      return this.movieInfo.genre.slice(0, -1)
    },
    country() {
      return this.movieInfo.country.replace(/[^가-힣]/gi, "")
    },
    reviewCount() {
      return this.reviews.length
    },
    changeReviews() {
      if (this.reviewFlag) {
        return this.reviews.slice(0, 2)
      } else {
        return this.reviews
      }
    }
  },
}
</script>
  
<style>

</style>
<template>
  <div class="m-3">
    <div class="row m-3 bg-white">
      <div class="col-4 d-flex justify-content-end m-3">
        <img :src="poster" @error='imageError = true' alt="영화포스터_상세보기">
      </div>
      <div class="col-6 m-3">
        <h2>{{ title }}</h2>
        <h3>{{ movieInfo.pubDate }} - {{ genre }} - {{ country }}</h3>
        <h5>평점 ★ {{ movieInfo.userRating }}점</h5>
        <CreateReview :movieInfo='movieInfo' />
      </div>
    </div>
    <div class="m-3 bg-white">
      <div class="row p-3">
        <div class="col-8">
          <hr>
          <MovieInfo :movieInfo='movieInfo' />
          <hr>
          <h2>출연/제작</h2>
          <MovieDirectorActor :movieInfo='movieInfo' />
        </div>
        <div class="col-4 p-3">
          <h2>예고편</h2>
          <MovieTrailer :video="video" v-for="video in videos" :key="video.etag" />
        </div>
      </div>
      <div class="m-3">
        <hr>
        <div class="d-flex justify-content-between">
          <div>
            <h2>코멘트</h2>
          </div>
          <div>
            <h5 v-if="isReviewFlag" @click="isTotalReviews" class="stretched-link font-weight-bold" style="position: relative; color:#f71972; cursor:pointer;">접기</h5>
            <h5 v-if="!isReviewFlag" @click="isTotalReviews" class="stretched-link font-weight-bold" style="position: relative; color:#f71972; cursor:pointer;">더보기</h5>
          </div>
        </div>
          <h5>총 {{ reviewCount }}개</h5>
      </div>
      <div class="m-3 list-group">
        <MovieReview :review="review" v-for="review in changeReviews" :key="review.id"/>
      </div>
      <div class="m-3">
        <hr>
        <h2>비슷한 작품</h2>
        <div class="row p-3">
          <SimilarMovie :similarMovie="similarMovie" v-for="similarMovie in similarMovies" :key="similarMovie.title" />
        </div>
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

const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
const API_URL = process.env.VUE_APP_YOUTUBE_API_URL


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
    isTotalReviews() {
      this.reviewFlag = !this.reviewFlag
    },
  },
  mounted(){
    console.log('hihi')
    console.log(process.env)
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
      if (!this.reviewFlag) {
        return this.reviews.slice(0, 1)
      } else {
        return this.reviews
      }
    },
    isReviewFlag() {
      return this.reviewFlag
    }
  },
}
</script>
  
<style>
  body {
    background-color: rgb(236, 236, 236);
  }
</style>
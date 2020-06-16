<template>
  <div class="m-3 d-flex justify-content-center">
    <span class="m-3">당신의 생각을 리뷰로 남겨보세요</span>
    <!-- Review Button trigger modal -->
    <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#reviewModal">
      리뷰작성
    </button>

    <!-- Review Modal -->
    <div class="modal fade" id="reviewModal" tabindex="-1" role="dialog" aria-labelledby="reviewModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="reviewModalLabel">{{ title }}</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <div class="form-group">
              <label for="reviewTitle">제목</label>
              <input v-model="reviewData.title" id="reviewTitle" class="form-control" type="text" placeholder="제목을 입력해주세요.">
            </div>
            <div class="form-goup">
              <label for="reviewContent">내용</label>
              <textarea v-model="reviewData.content" class="form-control" name="" id="reviewContent" cols="30" rows="10" placeholder="이 작품에 대한 생각을 자유롭게 표현해주세요."></textarea>
            </div>
          </div>
          <div class="modal-footer">
            <button @click="createReview" type="button" class="btn btn-primary">코멘트 작성</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'


const SERVER_URL = 'http://127.0.0.1:8000/movies/'

export default {
  name: 'CreateReview',
  props: {
    movieInfo: Object,
  },

  data() {
    return {
      reviewData: {
        movie: this.movieInfo.id,
        title: null,
        content: null,
      }
    }
  },
  methods: {
    createReview() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }

      axios.post(SERVER_URL + this.movieInfo.id + '/new_review/', this.reviewData, config)
        .then(res => { 
          console.log(res.data)
          this.$router.go()
        })
        .catch(err => console.log(err.response.data))
    },
  },
  computed: {
    title(){
      return this.movieInfo.title.replace(/(<([^>]+)>)/gi,"")
    },
  }

}
</script>

<style>

</style>
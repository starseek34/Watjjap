<template>
  <div>
    <div class="row">
      <img src="../../assets/logo.png" alt="영화포스터_헤더">
    </div>
    <div class="row">
      <div class="col">
        <img src="../../assets/logo.png" alt="영화포스터_상세보기">
      </div>
      <div class="col">
        <h3>기생충</h3>
        <h4>2019 - 드라마 - 한국</h4>
        <p>평점 * 4.3점</p>
        <hr>
        <p>당신의 평점 ****</p>
      </div>
    </div>
    <div class="row">
      <div>
        <p>당신의 생각을 리뷰로 남겨보세요</p>
        <!-- Review Button trigger modal -->
        <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#reviewModal">
          리뷰작성
        </button>

        <!-- Review Modal -->
        <div class="modal fade" id="reviewModal" tabindex="-1" role="dialog" aria-labelledby="reviewModalLabel" aria-hidden="true">
          <div class="modal-dialog">
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title" id="reviewModalLabel">기생충</h5>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                  <span aria-hidden="true">&times;</span>
                </button>
              </div>
              <div class="modal-body">
                <textarea class="form-control" name="" id="" cols="30" rows="10" placeholder="이 작품에 대한 생각을 자유롭게 표현해주세요."></textarea>
              </div>
              <div class="modal-footer">
                <button type="button" class="btn btn-primary">코멘트 작성</button>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div>
        <h4>기본정보</h4>
        <h4>기생충</h4>
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
export default {
  name: 'MovieDetailView',
}
</script>

<style>

</style>
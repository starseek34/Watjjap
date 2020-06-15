<template>
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
</template>

<script>
export default {

}
</script>

<style>

</style>
<template>
  <div>
    <!-- Login Button trigger modal -->
    <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#loginModal">
      로그인
    </button>

    <!-- Login Modal -->
    <div class="modal fade" id="loginModal" tabindex="-1" role="dialog" aria-labelledby="loginModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content m-auto" style="width:380px;">
          <div class="modal-body">
            <h2 class="font-weight-bolder m-3" style="color:#f71972" >WATCHA</h2>
              <h6 class="font-weight-bold m-4">로그인</h6>
              <div class="form-group w-100 mx-auto mb-2">
                <input type="email" class="form-control border-0" style="background-color:#f5f5f5;" id="email" aria-describedby="emailHelp" placeholder="이메일">
              </div>
              <div class="form-group w-100 mx-auto">
                <input type="password" class="form-control border-0" style="background-color:#f5f5f5;" id="password" placeholder="비밀번호">
              </div>
              <div>
                <button type="submit" class="btn w-100 text-white font-weight-bolder" style="background-color:#f71972">로그인</button>
              </div>
              <div class="mt-3">
                <a href="#" class="stretched-link" style="position: relative; color:#f71972;" data-dismiss="modal" data-toggle="modal" data-target="#signupModal">
                <span class="font-weight-bold" style="font-size:15px;">비밀번호를 잊어버리셨나요?</span>
                </a>
              </div>
              <div class="mt-3">
                <small>
                <p style="display:inline; font-size:15px; color:#9c9c9c" class="font-weight-bold">계정이 없으신가요?</p>
                </small>
                <a href="#" class="stretched-link" style="position: relative;  color:#f71972;" data-dismiss="modal" data-toggle="modal" data-target="#signupModal">
                <span class="font-weight-bold ml-1" style="font-size:15px;">회원가입</span></a>
              </div> 
              <div style="margin-top:35px;">
                <hr style="position:relative;">
                <div style="position:relative; top:-26px; z-index:2; width:60px; font-size:15px; color:#bdbebf; " class="bg-white mx-auto font-weight-bold">OR</div>
              </div>
                  <button type="button" style="background-color:#3b5998;" class="btn w-100 text-white mb-4">
                    <i style="position:relative; left: -65px; top:3px; font-size:27px; display:inline;" class="fa fa-facebook-square" aria-hidden="true"></i>
                    <span  class="font-weight-bold">Facebook으로 로그인</span></button>
          </div>
        </div>
      </div>
    </div>

    <!-- Signup Button trigger modal -->
    <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#signupModal">
      회원가입
    </button>

    <!-- Signup Modal -->
    <div class="modal fade" id="signupModal" tabindex="-1" role="dialog" aria-labelledby="signupModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="loginModalLabel">WAJJAB</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <h6>회원가입</h6>
            <input type="text" placeholder="이름">
            <input type="email" placeholder="이메일">
            <input type="password" placeholder="비밀번호">
            <button>회원가입</button>
            <p>이미 가입하셨나요?</p>
            <a href="#" class="stretched-link text-danger" style="position: relative;" data-dismiss="modal" data-toggle="modal" data-target="#loginModal">
              로그인
            </a>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-primary">Facebook으로 로그인</button>
          </div>
        </div>
      </div>
    </div>

    <router-link :to="{ name: 'RecommendMovie' }">즐겨찾기</router-link>
    <router-link :to="{ name: 'MyPage' }">마이페이지</router-link>
    <h1>WAJJAB</h1>

    <SearchBar />

  </div>
</template>

<script>
import SearchBar from '../components/SearchBar.vue'

export default {
  name: 'Home',
  components: {
    SearchBar
  }
}
</script>

<style>

</style>

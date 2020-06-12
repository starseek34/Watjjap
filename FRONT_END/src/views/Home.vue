<template>
  <div>
<!-- Login Button trigger modal -->
    <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#loginModal">
      로그인
    </button>

    <!-- Login Modal -->
    <div class="modal fade" id="loginModal" tabindex="-1" role="dialog" aria-labelledby="loginModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="loginModalLabel">WAJJAB</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <h6>로그인</h6>
            <input type="email" placeholder="이메일">
            <input type="password" placeholder="비밀번호">
            <button>로그인</button>
            <a href="#" class="stretched-link text-danger" style="position: relative;" data-dismiss="modal" data-toggle="modal" data-target="#signupModal">
              비밀번호를 잊어버리셨나요?
            </a>
            <p>계정이 없으신가요?</p>
            <a href="#" class="stretched-link text-danger" style="position: relative;" data-dismiss="modal" data-toggle="modal" data-target="#signupModal">
              회원가입
            </a>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-primary">Facebook으로 로그인</button>
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
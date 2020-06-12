<template>
  <div id="app" class="container">
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
            <input type="email">
            <input type="password">
            <button>로그인</button>
            <p>비밀번호를 잊어버리셨나요?</p>
            <p>계정이 없으신가요?</p> <p>회원가입</p>
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
            <h5 class="modal-title" id="signupModalLabel">Modal title</h5>
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            ...
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
            <button type="button" class="btn btn-primary">Save changes</button>
          </div>
        </div>
      </div>
    </div>

    <h1>WAJJAB</h1>

    <SearchBar />

  </div>
</template>

<script>
import SearchBar from './components/SearchBar.vue'

export default {
  name: 'App',
  components: {
    SearchBar
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>

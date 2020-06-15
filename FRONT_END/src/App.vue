<template>
  <div id="app">
    <nav class="navbar navbar-expand-lg navbar-light">
      <a class="navbar-brand" href="#" >
      <router-link :to="{ name: 'Home' }" class="font-weight-bold" style="color:#f71972">WAJJAB</router-link>
      </a> 
  
      <div class="w-100" id="navbarNavAltMarkup">
        <div class="d-flex justify-content-end">
            <!-- search -->
            <a class="nav-item nav-link m-auto" style="width: 50%;" href="#">
              <SearchBar v-if="true"  />
            </a>                
            <a class="nav-item nav-link" href="#">
            <button type="button" class="border-0 bg-transparent text-white" data-toggle="modal" data-target="#loginModal">
              로그인
            </button>
          </a>
          <a class="nav-item nav-link" href="#">
            <button type="button" class="border-0 text-white rounded" style="background-color:#f71972" data-toggle="modal" data-target="#signupModal">
              회원가입
            </button>
          </a>
          <a class="nav-item nav-link" href="#">
            <router-link :to="{ name: 'RecommendMovie' }"><i class="fa fa-star"  style="font-size:40px;" aria-hidden="true"></i></router-link>
          </a>
          <a class="nav-item nav-link " href="#">
            
          <router-link :to="{ name: 'MyPage' }"><i class="fa fa-user-circle-o" style="font-size:40px;" aria-hidden="true"></i></router-link>
          </a>
      
        </div>
      </div>
    </nav>

    
    <div class="container">
      <router-view />
    </div>
    
  </div>
</template>

<script>
import SearchBar from './components/SearchBar.vue'

export default {
  name: 'App',
  components: {
    SearchBar,
  }
}
</script>

<style>
html, body{
  height:100%;
}
#app {
  /* background-image: url('./assets/background.jpg'); */
  background-size: cover;
  height: 400px;
  margin: 0;
}
#nav a {
  font-weight: bold;
  color: #2c3e50;
}
</style>
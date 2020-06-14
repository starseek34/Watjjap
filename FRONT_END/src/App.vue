<template>
  <div id="app">
    <nav class="navbar navbar-expand-lg navbar-light bg-dark d-flex">
      <a class="navbar-brand" href="#">
      <router-link :to="{ name: 'Home' }">WAJJAB</router-link>
      </a> 
      <!-- search -->
      <div class="">
      <a class="nav-item nav-link" href="#">
        <SearchBar v-if="true" />
      </a>
      </div>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
      </button>
  
      <div class="" id="navbarNavAltMarkup">
        <div class="navbar-nav ">          
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
            <router-link :to="{ name: 'RecommendMovie' }"><i class="fa fa-star" aria-hidden="true"></i></router-link>
          </a>
          <a class="nav-item nav-link " href="#">
            
          <router-link :to="{ name: 'MyPage' }"><i class="fa fa-user-circle-o" aria-hidden="true"></i></router-link>
          </a>
      
        </div>
      </div>
    </nav>

    <SearchBar v-if="true" />    
    <router-view />
    <div id="h">
      hi
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
#app {
  height: 400px;
  background-color:green;
  /*background-image: url('./assets/background.jpg');
  background-size: cover;
  height: 400px;
  margin: 0; */
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}
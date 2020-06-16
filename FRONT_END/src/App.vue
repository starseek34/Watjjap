<template>

  <div id="app" :style="{ 'background-image': 'url('+bg_img+');' }">
    <nav class="navbar navbar-expand-lg navbar-light bg-dark">
      <a class="navbar-brand" href="#" >
      <router-link :to="{ name: 'Home' }" class="font-weight-bold" style="color:#f71972">WAJJAB</router-link>
      </a>   
      <div class="w-100" id="navbarNavAltMarkup">
        <div class="d-flex justify-content-end">
            <!-- search -->
            <a class="nav-item nav-link m-auto" style="width: 50%;" href="#">
              <SearchBar v-if="true"  />
            </a>                
            <a class="nav-item nav-link" href="#" v-if="!isLoggedIn">
              
            <button type="button" class="border-0 bg-transparent text-white" data-toggle="modal" data-target="#loginModal">
              로그인
            </button>
          </a>
          
          <a class="nav-item nav-link" href="#" v-if="!isLoggedIn">
            <button type="button" class="border-0 text-white rounded" style="background-color:#f71972" data-toggle="modal" data-target="#signupModal">
              회원가입
            </button>
          </a>
          <a  @click="logout"  class="nav-item nav-link" href="#" v-if="isLoggedIn">
            <button  type="button" class="border-0 bg-transparent text-white">
              로그아웃
            </button>
          </a>
          <a class="nav-item nav-link" href="#" v-if="isLoggedIn">
            <router-link v-if="isLoggedIn" :to="{ name: 'RecommendMovie' }"><i class="fa fa-star"  style="font-size:40px;" aria-hidden="true"></i></router-link>
          </a>
          <a class="nav-item nav-link " href="#" v-if="isLoggedIn">            
          <router-link v-if="isLoggedIn" :to="{ name: 'MyPage' }"><i class="fa fa-user-circle-o" style="font-size:40px;" aria-hidden="true"></i></router-link>
          </a>
        </div>
      </div>
    </nav>
    <Modal  @submit-login-data="login" @submit-signup-data="signup" :iserr="iserr" :errMsg="errMsg"/>
    
    <div class="container">
      <router-view  />
    </div>
    
  </div>
</template>

<script>
import SearchBar from './components/SearchBar.vue'
import Modal from './components/Modal.vue'
import axios from 'axios'

const SERVER_URL = 'http://localhost:8000'

export default {
  name: 'App',
  components: {
    SearchBar,
    Modal,
  },
  data(){
    return{
      iserr: false,
      errMsg: '',
      isLoggedIn: false,
      bg_img: "./assets/background.jpg",
      //bg_img:'https://images.mypetlife.co.kr/content/uploads/2019/09/06150205/cat-baby-4208578_1920-1024x683.jpg',
    }
  },
  methods: {
  
     setCookie(token){
      this.$cookies.set('auth-token',token)
      this.isLoggedIn = true
     },    
    login(loginData){
      axios.post(SERVER_URL + '/rest-auth/login/', loginData)
      .then(res => {
        this.iserr = false
        this.setCookie(res.data.key)
        this.$router.go()
        })
      .catch(err => {
        console.log(err.response.data)
        this.errMsg = "아이디 또는 비밀번호를 확인해주세요."
        this.iserr = true
      })
       //completed
     },
     
    signup(signupData){
      axios.post(SERVER_URL + '/rest-auth/signup/', signupData)
      .then(res => {
        this.setCookie(res.data.key)
        this.$router.go()        
      })
      .catch(err => this.errorMessages=err.response.data)
    },
    logout(){
      const requestHeaders = {
        headers: {
          'Authorization': `Token ${this.$cookies.get('auth-token')}`
        }
      }
        axios.post(SERVER_URL + '/rest-auth/logout/', null, requestHeaders)
        .then(() => {
          this.$cookies.remove('auth-token')
          this.isLoggedIn = false
          this.$router.push({name: 'Home' })
        })
        .catch(err=> console.log(err.response.data))
    },

  },
  mounted(){
     this.isLoggedIn = this.$cookies.isKey('auth-token')
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
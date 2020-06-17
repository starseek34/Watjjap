<template>

<div id="app" v-bind:style="{ 'background-image': 'url(' + bg_img + ')' }">
    <nav id="mynav" class="navbar navbar-expand-lg navbar-light navbar-fixed-bottom">
      <a class="navbar-brand" href="#" >
      <router-link :to="{ name: 'Home' }" class="font-weight-bold" style="color:#f71972">WAJJAB</router-link>
      </a>   
      <div class="w-100" id="navbarNavAltMarkup">
        <div class="d-flex justify-content-end">
            <!-- search -->
            <a class="nav-item nav-link m-auto" style="width: 50%;" href="#">
              <SearchBar v-if="isvisible"  />
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
              <i style="font-size:40px;" class="fa fa-sign-out" aria-hidden="true"></i>
            </button>
          </a>
          <a class="nav-item nav-link" href="#" v-if="isLoggedIn">
            <router-link v-if="isLoggedIn" :to="{ name: 'RecommendMovie' }"><i class="fa fa-star"  style="font-size:40px;" aria-hidden="true"></i></router-link>
          </a>
          <a  @click="mypage" class="nav-item nav-link " href="#" v-if="isLoggedIn">            
          <router-link v-if="isLoggedIn" :to="{ name: 'MyPage' }"><i class="fa fa-user-circle-o" style="font-size:40px;" aria-hidden="true"></i></router-link>
          </a>
        </div>
      </div>
    </nav>
    <Modal  @submit-login-data="login" @submit-signup-data="signup" :iserr="iserr" :errMsg="errMsg"/>
    
    <div class="container">
      <router-view  :img1="img1" :img2="img2" :img3="img3"/>
    </div>
    
  </div>
</template>

<script>
import SearchBar from './components/SearchBar.vue'
import Modal from './components/Modal.vue'
import axios from 'axios'

const SERVER_URL = 'http://127.0.0.1:8000'

export default {
  name: 'App',
  components: {
    SearchBar,
    Modal,
  },
  data(){
    return{
      img1: require('./assets/vue.png'),
      img2: require('./assets/django.png'),
      img3: require('./assets/rest.png'),
      userinfo: '',
      isvisible: false,
      iserr: false,
      errMsg: '',
      isLoggedIn: false,
      bg_img: require('./assets/header.jpg'),
      username: '',
      password: '',
      // bg_img:'https://images.mypetlife.co.kr/content/uploads/2019/09/06150205/cat-baby-4208578_1920-1024x683.jpg',
    }
  },
  methods: {
    mypage(){
      const id = this.$cookies.get('username')
      console.log('what')
      //요청보내고
      axios.post(SERVER_URL + '/accounts/user/mypage/', {'id':id})
      .then(res=>{
        //유저정보를 얻었음.
         this.$cookies.set('userinfo',res.data)
      })
      .catch(err => {
        
        console.log(err.response.data)
      })
      //받아온값을 props로 내려보내주기.
    },
  
     setCookie(token){
      this.$cookies.set('auth-token',token)
      this.isLoggedIn = true
     },    
    login(loginData){
      axios.post(SERVER_URL + '/rest-auth/login/', loginData)
      .then(res => {
        console.log('abcdef')
        this.$cookies.set('username',loginData.username)
        this.$cookies.set('password', loginData.password)
        
        this.iserr = false
        this.setCookie(res.data.key)

        //현재페이지가 home이면 뒤로가기, 아니면 home으로 가라
        const cur_url = document.location.href;
        console.log(cur_url)
            if (cur_url == 'http://localhost:8080/#'){
              this.$router.go()

            }else{
              this.$router.go()
              this.$router.push({name: 'Home' })          
              
            }

        })
      .catch(err => {
        console.log(err.response.data)
        this.errMsg = "아이디 또는 비밀번호를 확인해주세요."
        this.iserr = true
      })
       
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
     this.mytoken = this.$cookies.get('auth-token')
     this.username = this.$cookies.get('username')
     this.password = this.$cookies.get('password')
     if (this.$route.path == "/"){
       this.isvisible = false
       this.bg_img = require('./assets/header.jpg')
        document.getElementById('mynav').classList.remove("bg-dark")
     }else{
       this.isvisible = true       
        this.bg_img = ""
        document.getElementById('mynav').classList.add("bg-dark")
     }
  },
   watch:{
    '$route'(to){
      
    console.log(to.path)
      if (to.path=='/'){
        this.isvisible = false
         this.bg_img = require('./assets/header.jpg')
        document.getElementById('mynav').classList.remove("bg-dark")

      }else{
        this.isvisible = true  
        this.bg_img = ""
        document.getElementById('mynav').classList.add("bg-dark")


      }
      
    }
  }

}
</script>

<style>
html, body{
  height:100%;
}
#app {
  /* background-image: url('./assets/header.jpg'); */
  background-size: cover;
  height: 400px;
  margin: 0;
}
#nav a {
  font-weight: bold;
  color: #2c3e50;
}
</style>
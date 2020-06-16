<template>
    <!-- Login Button trigger modal -->
  
    
  <div id="home"> 
    <!-- Login Button trigger modal -->
    <!-- Login Modal -->
    <div class="modal fade" id="loginModal" tabindex="-1" role="dialog" aria-labelledby="loginModalLabel" aria-hidden="true">
      <div v-if="iserr" class="alert alert-danger w-100 text-center m-0" role="alert" style="position: absolute; bottom:0px; left:0px; z-index: 2;">
      {{ errMsg }}
      <!-- <button type="button" class="close" data-dismiss="alert" aria-label="Close">
        <span aria-hidden="true">&times;</span>
      </button> -->
    </div>
    
      <div class="modal-dialog">
        <div class="modal-content m-auto" style="width:380px;">
          <div class="modal-body">
            <h2 class="font-weight-bolder m-3" style="color:#f71972" >WATCHA</h2>
              <h6 class="font-weight-bold m-4">로그인</h6>
              <div class="form-group w-100 mx-auto mb-2">
                <input v-model="loginData.username" type="email" class="form-control border-0" style="background-color:#f5f5f5;" id="username" aria-describedby="emailHelp" placeholder="이메일">
              </div>
              <div class="form-group w-100 mx-auto">
                <input v-model="loginData.password" type="password" class="form-control border-0" style="background-color:#f5f5f5;" id="password" placeholder="비밀번호">
              </div>
                
                <a id="a" href="#" @click="login" role="button" class="btn w-100 text-white font-weight-bolder" style="background-color:#f71972">로그인</a>
              
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
                <div style="position:relative; top:-26px; z-index:2; width:60px; font-size:15px; color:#bdbebf; " class="text-center bg-white mx-auto font-weight-bold">OR</div>
              </div>
              <button type="button" style="background-color:#3b5998;" class="btn w-100 text-white mb-4">
                  <i style="position:relative; left: -65px; top:3px; font-size:27px; display:inline;" class="fa fa-facebook-square" aria-hidden="true"></i>
                  <span  class="font-weight-bold">Facebook으로 로그인</span>
              </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Signup Button trigger modal -->
    

    <!-- Signup Modal -->
    <div class="modal fade" id="signupModal" tabindex="-1" role="dialog" aria-labelledby="signupModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content m-auto" style="width:380px;">
          <div class="modal-body">
            <h2 class="font-weight-bolder m-3" style="color:#f71972" >WATCHA</h2>
              <h6 class="font-weight-bold m-4">회원가입</h6>
              <div class="form-group w-100 mx-auto mb-2">
                <input type="text" class="form-control border-0" style="background-color:#f5f5f5;" id="name" aria-describedby="emailHelp" placeholder="이름">
              </div>
              <div class="form-group w-100 mx-auto mb-2">
                <input v-model="signupData.username" type="email" class="form-control border-0" style="background-color:#f5f5f5;" id="email" aria-describedby="emailHelp" placeholder="이메일">
              </div>
              <div class="form-group w-100 mx-auto">
                <input v-model="signupData.password1" type="password" class="form-control border-0" style="background-color:#f5f5f5;" id="password" placeholder="비밀번호">
              
              </div>
              <div class="form-group w-100 mx-auto">
                <input v-model="signupData.password2" type="password" class="form-control border-0" style="background-color:#f5f5f5;" id="password2" placeholder="비밀번호">
              
              </div>
              
              
                <a href="#" @click="signup" role="button" class="btn w-100 text-white font-weight-bolder" style="background-color:#f71972">회원가입</a>
              
              <div class="mt-3">
                <small>
                <p style="display:inline; font-size:15px; color:#9c9c9c" class="font-weight-bold">이미 가입하셨나요?</p>
                </small>
                <a href="#" class="stretched-link" style="position: relative;  color:#f71972;" data-dismiss="modal" data-toggle="modal" data-target="#loginModal">
                <span class="font-weight-bold ml-1" style="font-size:15px;">로그인</span></a>
              </div> 
              <div style="margin-top:35px;">
                <hr style="position:relative;">
                <div style="position:relative; top:-26px; z-index:2; width:60px; font-size:15px; color:#bdbebf; " class="text-center bg-white mx-auto font-weight-bold">OR</div>
              </div>
              <button type="button" style="background-color:#3b5998;" class="btn w-100 text-white mb-4">
                  <i style="position:relative; left: -65px; top:3px; font-size:27px; display:inline;" class="fa fa-facebook-square" aria-hidden="true"></i>
                  <span  class="font-weight-bold">Facebook으로 로그인</span>
              </button>
          </div>
          
        </div>
      </div>
    </div>

  </div>
</template>

<script>

export default {
  name: 'Modal',
  components: {
   },
  props: {
    iserr: null,
    errMsg: String,

  },
   data(){
     return {
       loginData: {
         username: null,
         password: null,
       },
       signupData: {
          //nickname: null,
          username: null,
          password1: null,
          password2: null,
        }
     }
   },
   
   methods: {
     login(){
      this.$emit('submit-login-data', this.loginData)
     },
     signup(){
        this.$emit('submit-signup-data', this.signupData)     
      },
   },
 
}
</script>

<style>

</style>

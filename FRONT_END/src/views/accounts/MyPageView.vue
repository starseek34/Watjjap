<template>
  <div class="m-3 alert card">
  <!-- <div class="container alert card" style="background-color: rgba(237,237,237,0.5)"> -->
      <a href="#" class="d-flex justify-content-end"><i class="fa fa-cog" style="font-size: 40px;" aria-hidden="true"></i></a>

      <i class="fa fa-user"  style="font-size:100px; color:gray" aria-hidden="true"></i>
    <hr>
    <!-- <div v-if="this.$parent.authenticated"> -->
    <p>Welcome , {{ userinfo.nickname }}!</p>
    <!-- </div> -->
    <h3>프로필</h3>
    <hr>
    <h4>{{ userinfo.nickname }}</h4>
    <p>{{ userinfo.username }} </p>
    <hr>
    <h5>취향분석</h5>
    <hr>
    <div class="btn btn-success">
        <h5>영화</h5>
        <p>지금까지 평가한 영화</p>
        <p>304</p>
    </div>
  </div>
</template>

<script>

export default {
  name: 'MyPageView',
  data(){
    return{
      userinfo: this.$cookies.get('userinfo')
    }
  },
 methods:{
 }
     
}

</script>
<!-- 해당유저것만 가져오는 -->
<style>

</style>
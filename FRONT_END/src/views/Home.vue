<template>
    <!-- Login Button trigger modal -->
  
  <div id="home" class="w-100">

    <div style="font-size:90px; margin-top:50px;" class="text-center text-white">WAJJAB</div>
    <SearchBar  class="w-50" style="position:fixed; top:380px; left:25%" v-if="true" />    
    
    <div class="d-flex" style="margin-top:250px;">
      <div class="card m-auto" style="width: 18rem;">
            <div class="card-body">
            <img class="card-img-top" :src="img1" alt="Card image cap">
              <a href="#" class="btn btn-primary w-100 mt-2">ssafy3 대전 1반 김고냥</a>
            </div>
        </div>
        <div class="card m-auto" style="width: 18rem;">
            <div class="card-body">
            <img class="card-img-top" :src="img1" alt="Card image cap">
              <a href="#" class="btn btn-primary w-100 mt-2">ssafy3 대전 1반 배고냥</a>
            </div>
        </div>
        <div class="card m-auto" style="width: 18rem;">
            <div class="card-body">
            <img class="card-img-top" :src="img1" alt="Card image cap">
              <a href="#" class="btn btn-primary w-100 mt-2">ssafy3 대전 1반 최고냥</a>
            </div>
        </div>

    </div>
      
  </div>
</template>

<script>
import SearchBar from '../components/SearchBar.vue'

export default {
  name: 'Home',
  components: {
    SearchBar,
   },
  data(){
    return{
       img1: 'https://contents.creators.mypetlife.co.kr/content/uploads/2019/12/14193807/thumb-20191204125140_8db6d8271452bd269c55ea22eea401f1_mn17_700x698.jpg',
       img2: './assets/bg_cat.png',
      // img3: require('./assets/bg_cat.png'),
    }
  },
   methods: {
     
   },
 
}
</script>

<style>

</style>

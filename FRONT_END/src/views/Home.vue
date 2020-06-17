<template>
    <!-- Login Button trigger modal -->
  
  <div id="home" class="w-100 container">

    <div style="font-size:90px; margin-top:50px;" class="text-center text-white">WAJJAB</div>
    <SearchBar  class="w-50 m-auto" style="position:relative; top:120px;" />    
    
    <div class="d-flex" style="margin-top:250px;">
      <div class="card m-auto" style="width: 18rem;">
            <div class="card-body">
              <img class="card-img-top" :src="img1" alt="Card image cap">
               
                </div>
            </div>
                  <div class="card m-auto" style="width: 18rem;">
                    <div class="card-body">
                    <img class="card-img-top" :src="img2" alt="Card image cap">
                     </div>
                </div>
                <div class="card m-auto" style="width: 18rem;">
                    <div class="card-body">
                    <img class="card-img-top" :src="img3" alt="Card image cap">
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
   props: {
     img1: String,
     img2: String,
     img3: String,
   },
 
}
</script>

<style>

</style>

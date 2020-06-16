<template>
    <!-- Login Button trigger modal -->
  
  <div id="home">

    <hr>
    <div style="font-size:90px; color:#f71972; margin-top:50px;" class="text-center">WAJJAB</div>
    <div class="w-100" style="position:fixed; top:380px;" >  
      <SearchBar  class="w-50 ml-auto mr-auto" v-if="true" />    
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
     
   methods: {
     
   },
 
}
</script>

<style>

</style>

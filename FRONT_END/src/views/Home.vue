<template>
    <!-- Login Button trigger modal -->
  
  <div id="home" class="w-100">

    <div style="font-size:90px; margin-top:50px;" class="text-center text-white">WAJJAB</div>
    <SearchBar  class="w-50" style="position:fixed; top:380px; left:25%" v-if="true" />    
    
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

<template>
  <div id="app" class="container">
    <div id="nav" v-if="true">
      <router-link :to="{ name: 'Home' }">WAJJAB</router-link>
      <SearchBar />
      <router-link :to="{ name: 'RecommendMovie' }">즐겨찾기</router-link>
      <router-link :to="{ name: 'MyPage' }">마이페이지</router-link>
    </div>
    <router-view />
  </div>
</template>

<script>
import SearchBar from './components/SearchBar.vue'

export default {
  name: 'App',
  components: {
    SearchBar
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>

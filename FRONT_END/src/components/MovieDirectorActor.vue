<template>
  <div class="row m-5">
    <div class="col-6 p-2" v-for="director in directors" :key="director.id">
      <i class="fa fa-user"  style="font-size:100px; color:gray" aria-hidden="true"></i>
      <h4>{{ director }}</h4>
      <span>감독</span>
    </div>
    <div class="col-6 p-2" v-for="actor in actors" :key="actor.id">
      <i class="fa fa-user"  style="font-size:100px; color:gray" aria-hidden="true"></i>
      <h4>{{ actor }}</h4>
      <span>주연</span>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MovieDirectorActor',
  props: {
    movieInfo: Object,
  },
  computed: {
    directors() {
      return this.movieInfo.director.slice(0, -1).split('|', 2)
    },
    actors() {
      return this.movieInfo.actor.slice(0, -1).split('|', 4)
    }
  }
}
</script>

<style>

</style>
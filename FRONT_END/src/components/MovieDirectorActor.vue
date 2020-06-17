<template>
  <div class="row">
    <div class="col-6 p-2 d-flex justify-content-center" v-for="director in directors" :key="director.id">
      <i class="fa fa-user" style="font-size:100px; color:gray" aria-hidden="true"></i>
      <div class="d-flex flex-column p-3">
        <h4>{{ director }}</h4>
        <p>감독</p>
      </div>
    </div>
    <div class="col-6 p-2 d-flex justify-content-center" v-for="actor in actors" :key="actor.id">
      <i class="fa fa-user"  style="font-size:100px; color:gray" aria-hidden="true"></i>
      <div class="d-flex flex-column p-3">
        <h4>{{ actor }}</h4>
        <p>주연</p>
      </div>
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
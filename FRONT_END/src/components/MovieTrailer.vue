<template>
  <div class="list-group-item embed-responsive embed-responsive-16by9">
    <iframe class="p-3 embed-responsive-item" :src="videoUrl" allowfullscreen></iframe>
  </div>
</template>

<script>
export default {
  name: 'MovieTrailer',
  props: {
      video: Object,
  },
  computed: {
      videoUrl(){
          return `https://youtube.com/embed/${this.video.id.videoId}`
      }
  }  
}
</script>

<style>

</style>
<template>
  <div id="app">
    <PasteArea />
  </div>
</template>

<script>
import PasteArea from './components/PasteArea.vue'

export default {
  name: 'App',
  components: {
    PasteArea
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
  margin-top: 60px;
}
</style>

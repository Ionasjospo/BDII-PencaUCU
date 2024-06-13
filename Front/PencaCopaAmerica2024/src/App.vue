<template>
  <router-view />
  <AppFooter />
</template>

<script>
import AppFooter from '@/components/AppFooter.vue'

export default {
  name: 'App',
  components: {
    AppFooter
  }
}
</script>

<style>

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #fff;
  margin-top: 60px;
  background: linear-gradient(20deg, rgb(4, 70, 63), #052b41);

}

html {
  background: linear-gradient(20deg, rgb(4, 70, 63), #052b41);
}

</style>

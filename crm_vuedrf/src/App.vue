<template>
  <div>
    <Navbar />
    <section class="section">
      <router-view/>
    </section>
  </div>
</template>

<script>
  import Navbar from './components/layout/Navbar.vue'
  export default {
    name: 'App',
    components: {
      Navbar
    },
    beforeCreate() {
      this.$store.commit('initializeStore')

      if (this.$store.state.token) {
        this.axios.defaults.headers.common['Authorization'] = "Token ${this.$store.state.token}"
      }
      else {
        this.axios.defaults.headers.common['Authorization'] = ""
      }
    }
  }
</script>

<style lang="scss">
  @import '~bulma';
</style>

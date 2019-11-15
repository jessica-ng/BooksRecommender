<template>
    <div id="nav" align = "left">
        <router-link to="/">   Home   </router-link> |  
        <router-link to="/about">   Profile   </router-link> |  
        <router-link to="/login">   Login   </router-link>  |
        <router-link to="/signup">   Sign Up   </router-link>
    </div>
</template>

<script>
export default {
  name: 'NavBar',
  props: {
    
  }
}
</script>

<style>
  @import url(NavBar.css);
</style>
<template>
  <div id="app">
    <NavBar ref="nav" />

    <router-view />
  </div>
</template>

<script>
import NavBar from "@/components/NavBar/NavBar.vue";

export default {
  components: {
    NavBar
  },
  updated() {
    this.$refs.nav.update_nav();
  },
  created() {
    //this.initiate()
  },
  methods: {
    initiate: function() {
      const path = "http://localhost:5000/initiate";
      axios
        .get(path, {})
        .then(function(response) {
          console.log(response);
        })

        .catch(function(error) {
          console.log(error);
        });
    }
  }
};
</script>

<style screen>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 10px;
}

#nav a {
  font-weight: bold;
  color: #ffffff;
}

#nav a.router-link-exact-active {
  color: #23d6b8;
}
</style>

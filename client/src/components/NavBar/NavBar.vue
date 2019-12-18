<template>
  <div id="nav">
    <b-row>
      <b-col
        ><div align="centre">
          <b-row>
            <b-col align="centre" md="2"
              ><router-link to="/"> Home </router-link></b-col
            >
            <b-col align="centre" md="2" id="profile" style="display:inline"
              ><router-link to="/profile"> Profile </router-link>
            </b-col>
            <b-col
              align="centre"
              md="2"
              id="recommendations"
              style="display:inline"
              ><router-link to="/recommendations">
                Recommendations
              </router-link>
            </b-col>
          </b-row>
        </div></b-col
      >
      <b-col
        ><div align="right">
          <router-link
            to="/signup"
            align="right"
            id="signup"
            style="display:none"
          >
            Sign Up
          </router-link>
          |
          <router-link to="/login" style="display:none" id="login">
            Login
          </router-link>
          <router-link @click.native= "logout" to="/" id="logout" style="display:inline">
            Logout
          </router-link>
          |
        </div></b-col
      >
    </b-row>
  </div>
</template>

<script>
export default {
  name: "NavBar",
  props: {},
  data: function() {
    return {
      userId: sessionStorage.userId
    };
  },
  methods: {
    update_nav: function() {
      if (sessionStorage.userId == "") {
        document.getElementById("login").style.display = "inline";
        document.getElementById("signup").style.display = "inline";
        document.getElementById("logout").style.display = "none";
        document.getElementById("profile").style.display = "none";
        document.getElementById("recommendations").style.display = "none";
      } else {
        document.getElementById("login").style.display = "none";
        document.getElementById("signup").style.display = "none";
        document.getElementById("logout").style.display = "inline";
        document.getElementById("profile").style.display = "inline";
        document.getElementById("recommendations").style.display = "inline";
      }
    },
    logout: function() {
      sessionStorage.userId = "";
      this.userId = "";
      this.update_nav();
    }
  }
};
</script>

<style>
@import url(NavBar.css);
</style>

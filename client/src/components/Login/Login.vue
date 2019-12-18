<template>
  <div id="login" align="centre">
    <div>
      <b-form id="username">
        <label for="feedback-user">User ID</label>
        <b-input
          v-model="userId"
          :state="validation"
          id="feedback-user"
        ></b-input>
        <b-form-invalid-feedback :state="validation">
          Your user ID must be 1-5 characters long.
        </b-form-invalid-feedback>
        <b-form-valid-feedback :state="validation">
          Looks Good.
        </b-form-valid-feedback>
      </b-form>
    </div>

    <div>
      <b-form>
        <label for="text-password">Password</label>
        <b-input
          v-model="user_password"
          type="password"
          id="text-password"
          aria-describedby="password-help-block"
        ></b-input>
      </b-form>
    </div>

    <div style="padding-top:1%">
      <b-button v-on:click="OnSubmit" variant="primary" >Submit</b-button>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Login",
  data() {
    return {
      userId: "",
      user_password: "",
      current_userid : ""
    };
  },
  computed: {
    validation() {
      return this.userId.length > 0 && this.userId.length < 6;
    }
  },
  methods: {
    validate: function(userId) {
      const path = "http://localhost:5000/validate";
      console.log(userId);
      axios
        .post(path, {
          username: this.userId,
          password: this.user_password
        })
        .then(function(response) {
          console.log(response.data)
          if (response.data == true) {
            sessionStorage.userId = userId;
            document.location.href = '/profile'
          }
        })

        .catch(function(error) {
          console.log(error);
        });
    },

    OnSubmit: function() {
      alert("Submit!");
      console.log(this.userId);
      console.log(this.user_password);
      this.validate(this.userId);
      return;
    }
  }
};
</script>

<style>
@import url(Login.css);
</style>

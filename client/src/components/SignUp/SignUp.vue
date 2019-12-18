<template>
  <div id="signup">
    <b-form id="username">
      <label for="feedback-user">New User ID {{ userId[0].new }}</label>
      <!-- <b-input
        v-model="userId"
        :state="validation"
        id="feedback-user"
        :value="userId"
      ></b-input> -->

      <b-form-valid-feedback :state="validation">
        Looks Good.
      </b-form-valid-feedback>
    </b-form>

    <div>
      <b-form>
        <label for="text-password">Password: </label>
        <b-input
          v-model="user_password"
          type="password"
          id="text-password"
          aria-describedby="password-help-block"
        ></b-input>
      </b-form>
    </div>

    <!-- <div>
            <b-form>
                <label for="text-password-check">Password</label>
                <b-input v-model= "user_password_check" type="password-check" id="text-password-check" aria-describedby="password-help-block"></b-input>
            </b-form>
        </div> -->
    <div class="button" style="padding-top:1%">
      <router-link to="/confirm_signup">
        <b-button v-on:click="signup(userId)" variant="primary" 
          >Submit</b-button
        >
      </router-link>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "SignUp",
  data() {
    return {
      userId: [],
      user_password: ""
    };
  },
  created() {
    this.userId = this.getNewid(this.userId)
    console.log(this.userId)
    console.log(this.userId.new)
  },
  computed: {
    validation() {
      console.log(this.userId.new)
      return this.userId.length > 4 && this.userId.length < 13;
    }
  },
  methods: {
    getNewid: function(userId) {
      const path = "http://localhost:5000/new_userid";
      axios
        .get(path, {})
        .then(function(response) {
          console.log(response.data);
          userId.push({
            new: parseInt(response.data)})
          console.log(userId)
        })
        .catch(function(error) {
          console.log(error);
        });
        return userId
    },
    signup: function(userId) {
      const path = "http://localhost:5000/sign_up";
      console.log(userId);
      axios
        .post(path, {
          username: this.userId[0].new,
          password: this.user_password
        })
        .then(function(response) {
          console.log(response.data);
          if (response.data == true) {
            sessionStorage.userId = userId;
            //document.cookie = "userid=" + 69
          }
        })

        .catch(function(error) {
          console.log(error);
        });
    }
  }
};
</script>

<style>
@import url(SignUp.css);
</style>

<template>
    <div id = "signup">       
        <b-form id="username">
        <label for="feedback-user">User ID</label>
        <b-input v-model="userId" :state="validation" id="feedback-user"></b-input>
        <b-form-invalid-feedback :state="validation">
            Your user ID must be 5-12 characters long.
        </b-form-invalid-feedback>
        <b-form-valid-feedback :state="validation">
            Looks Good.
        </b-form-valid-feedback>
        </b-form>
        

         <div>
            <b-form>
                <label for="text-password">Password</label>
                <b-input v-model= "user_password" type="password" id="text-password" aria-describedby="password-help-block"></b-input>
            </b-form>
        </div>

         <div>
            <b-form>
                <label for="text-password-check">Password</label>
                <b-input v-model= "user_password_check" type="password-check" id="text-password-check" aria-describedby="password-help-block"></b-input>
            </b-form>
        </div>

        <b-button v-on:click="OnSubmit" variant="primary">Submit</b-button>
        </div>
</template>

<script>
export default {
    name: 'SignUp',
    data() {
      return {
        userId: '',
        user_password: ''
      }
    },
    computed: {
      validation() {
        return this.userId.length > 4 && this.userId.length < 13
      }
    }
}
</script>

<style>
  @import url(SignUp.css);
</style>
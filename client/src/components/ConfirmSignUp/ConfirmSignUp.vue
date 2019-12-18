<template>
    <div class = "onboarding_cont">
        <p> You have completed the sign up process, now you can further personalise your book recommendations with onboarding </p>
        <img class="image" src="../../assets/SplashImages/complete_onboarding.png" alt="">

        <div class="button">
            <router-link to= "/onboarding1">
                <b-button class= "b-button" variant="primary">To onboarding!</b-button>
            </router-link>
        </div>
    </div>
</template>

<script>
export default {
    name: "ConfirmSignUp"
}
</script>

<style lang="css" scoped>
  @import url("ConfirmSignUp.css");
</style>
<template>
  <div>
    <div style="padding-top:7%; margin: auto;">
      <b-card title="Card Title" no-body style="width:80%; margin: auto;">
        <b-card-header header-tag="nav">
          <b-nav card-header tabs>
            <b-nav-item id="pastrating" active v-on:click="past_ratings()">Past ratings</b-nav-item>
            <b-nav-item id="newrating" v-on:click="new_ratings()">New ratings</b-nav-item>
          </b-nav>
        </b-card-header>

        <b-card-body class="text-center">
            
          <b-card-text>
            
            <PastRatings id="past_rating" button_text="Next" route="" msg="Past Ratings" style="display:inline"> </PastRatings>
            <SubmitRatings id = "submit_ratings" style="display:none"/>
          </b-card-text>
        </b-card-body>
      </b-card>
      
    </div>
  </div>
</template>

<script>
import axios from "axios";
import PastRatings from "@/components/PastRatings/PastRatings.vue";
import SubmitRatings from '@/components/SubmitRatings/SubmitRatings.vue';

export default {
  name: "Profile",
  components: {
    PastRatings,
    SubmitRatings
  },
  created() {
    // this.get_recommendations()
  },
  methods: {
    new_ratings: function(){
        var rating_nav = document.getElementById("newrating").getElementsByTagName("a");
        var past_rating = document.getElementById("pastrating").getElementsByTagName("a");

        past_rating[0].classList.remove("active")
        rating_nav[0].classList.add("active");

        document.getElementById("submit_ratings").style.display = "inline"
        document.getElementById("past_rating").style.display = "none"
    },
    past_ratings: function(){
        var rating_nav = document.getElementById("newrating").getElementsByTagName("a");
        var past_rating = document.getElementById("pastrating").getElementsByTagName("a");

        past_rating[0].classList.add("active")
        rating_nav[0].classList.remove("active");

        document.getElementById("submit_ratings").style.display = "none"
        document.getElementById("past_rating").style.display = "inline"
    }
  }
};
</script>

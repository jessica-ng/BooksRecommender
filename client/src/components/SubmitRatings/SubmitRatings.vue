<template>
    <div class='ratings'>
        <b-form-group
        id="input-group-1"
        label="Book Id:"
        label-for="input-1"
        description="Book."
      >
      <b-form-input
          id="input-1"
          v-model="bookid"
          required
          placeholder="Enter bookid"
        ></b-form-input>
      </b-form-group>

      <b-form-select
      class="mb-2 mr-sm-2 mb-sm-0"
      v-model="rating"
      :value="null"
      :options="{ '1': '1', '2': '2', '3': '3', '4': '4', '5': '5' }"
      id="rating"
    >
      <template v-slot:first>
        <option :value="null">Choose...</option>
      </template>
    </b-form-select>

    <b-button v-on:click="submitRating(bookid, rating)" variant="primary">Submit</b-button>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'SubmitRatings',
    data: function(){
        return {
            bookid: '',
            rating : 0
        }
    },
    methods: {
        submitRating: function(bookid, rating){
            const path = 'http://localhost:5000/sumbitrating';
            axios.post(path, {
                userid: sessionStorage.userId,
                bookid: bookid,
                rating: rating
            })
                .then(function (response) {
                console.log(response.data);
                })

                .catch(function (error) {
                    console.log(error);
                });
            console.log("lol")
            
        }
    }
}
</script>

<style scoped>
    @import url("SubmitRatings.css");
</style>
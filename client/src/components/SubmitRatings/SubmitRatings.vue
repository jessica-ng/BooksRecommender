<template>
  <div>
    <div class="ratings">
      <b-form-group
        id="input-group-1"
        label="Book:"
        label-for="input-1"
        description=""
      >
      
      <b-form-select
        class="mb-2 mr-sm-2 mb-sm-0"
        v-model="book"
        :value="book_ids"
        :options='books'
        id="book_id"
      >
      </b-form-select>
      </b-form-group>
      Rating:
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
      <div style="padding-top:5%">
        <b-button
          v-on:click="submitRating(book, rating, books, book_ids)"
          variant="primary"
          style="padding-top:1%"
          >Submit</b-button
        >
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "SubmitRatings",
  data: function() {
    return {
      book: "",
      rating: 0,
      books: [],
      book_ids : []
    };
  },
  created() {
    this.getBooks(this.books, this.book_ids)
  },
  methods: {
    submitRating: function(book, rating, books, book_ids) {
      const path = "http://localhost:5000/sumbitrating";
      var bookid = books.indexOf(book)
      bookid = book_ids[bookid]
      axios
        .post(path, {
          userid: sessionStorage.userId,
          bookid: bookid,
          rating: rating
        })
        .then(function(response) {
          console.log(response.data);
        })

        .catch(function(error) {
          console.log(error);
        });
    },
    getBooks: function(books, book_ids) {
      const path = "http://localhost:5000/get_all_books";
      axios.post(path, {
          user_id : sessionStorage.userId
      }).then(function(response) {
        
        var data = response.data;
        for (let key in response.data.id) {
          //key = response.data.id[key] - 1;
          var book_id = key + 1;
          books.push(data.title[key])
          book_ids.push(data.id[key])
          
        }
      })
      

        .catch(function(error) {
          console.log(error);
        })
    return books
    },
  }
}

</script>

<style scoped>
@import url("SubmitRatings.css");
</style>

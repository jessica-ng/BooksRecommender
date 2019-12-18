<template>
  <div>
    <div class="description">
      <p>{{ msg }}</p>
      <div class="button">
        <router-link :to="route">
          <b-button v-on:click="submitRating(selection)" variant="primary">{{
            button_text
          }}</b-button>
        </router-link>
      </div>
    </div>
    <div class="book_selection">
      <div
        v-b-tooltip.hover
        :title="
          'By ' +
            book.author +
            '\n' +
            '. Average rating: ' +
            book.average_rating
        "
        @click="logState($event.target.parentElement.id, selection)"
        class="books"
        v-for="book in books"
        :id="book.id"
        :key="book.name"
      >
        <img class="books_img" :src="book.image" alt="" />

        <div class="book_names">
          <h6>{{ book.name }}</h6>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "BookCard",
  props: {
    rating: 0,
    button_text: String,
    route: String,
    msg: String
  },
  data: function() {
    return {
      rating: 0,
      books: [],
      selection: []
    };
  },
  created() {
    this.getbooks(this.books);
  },
  methods: {
    logState: function(id, selection) {
      if (
        document.getElementById(id).classList.contains("booksActive") == false
      ) {
        document.getElementById(id).classList.add("booksActive");
        selection.push(id);
      } else {
        document.getElementById(id).classList.remove("booksActive");
        selection.splice(selection.indexOf(id), 1);
      }
    },
    submitRating: function(selection) {
      var i;
      for (i = 0; i < selection.length; i++) {
        const path = "http://localhost:5000/sumbitrating";
        axios
          .post(path, {
            userid: sessionStorage.userId,
            bookid: selection[i],
            rating: this.rating
          })
          .then(function(response) {})

          .catch(function(error) {
            console.log(error);
          });
      }
    },
    getbooks: function(books) {
      const path = "http://localhost:5000/get_books";
      axios
        .get(path, {})
        .then(function(response) {
          var data = response.data;
          for (let key in response.data.id) {
            key = response.data.id[key] - 1;
            books.push({
              id: data.id[key],
              name: data.title[key],
              image: data.image_url[key],
              average_rating: data.average_rating[key],
              author: data.authors[key]
            });
          }
        })

        .catch(function(error) {
          console.log(error);
        });
    }
  }
};
</script>

<style lang="css" scoped>
@import url("BookCard.css");
</style>

<template>
  <div>
    <div class="description">
      <p>{{ msg }}</p>
      <div class="button">
        <!-- <router-link :to=route>
                <b-button v-on:click="submitRating(selection)" variant="primary">{{ button_text }}</b-button>
            </router-link> -->
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
  name: "Recommendations",
  props: {
    button_text: String,
    route: String,
    msg: String
  },
  data: function() {
    return {
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
    getbooks: function(books) {
      const path = "http://localhost:5000/get_recommendations";
      axios
        .post(path, {
          user_id: sessionStorage.userId
        })
        .then(function(response) {
          console.log(response);
          var data = response.data;

          Object.keys(data).forEach(function(key) {
            books.push({
              id: data[key].book_id_x,
              name: data[key].title_x,
              image: data[key].image_url_x,
              average_rating: data[key].average_rating_x,
              author: data[key].authors_x
            });
          });
        })

        .catch(function(error) {
          console.log(error);
        });
    }
  }
};
</script>

<style lang="css" scoped>
@import url("Recommendations.css");
</style>

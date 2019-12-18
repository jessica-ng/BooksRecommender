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
      <b-modal id="modal1" size="lg" centered :title="selectedBook.name">
        <b-card
          :title="selectedBook.name"
          :img-src="selectedBook.image"
          img-alt="Image"
          img-left
          class="mb-3"
        >
          <b-card-text>
            <p class="my-4">{{ selectedBook.author }}</p>
            Some quick example text to build on the card title and make up the
            bulk of the card's content.

            <p class="my-4">
              Your current rating: {{ selectedBook.user_rating }} / 5
            </p>

            Update rating:
            <b-form-select
              class="mb-2 mr-sm-2 mb-sm-0"
              v-model="new_rating"
              :value="null"
              :options="{ '1': '1', '2': '2', '3': '3', '4': '4', '5': '5' }"
              id="rating"
            >
              <template v-slot:first>
                <option :value="null">Choose...</option>
              </template>
            </b-form-select>
          </b-card-text>
          <b-button
          v-on:click="updateRating(selectedBook.id, selectedBook.user_rating, new_rating)"
          variant="primary"
          style="padding-top:1%"
          >Submit</b-button
        >
        </b-card>
      </b-modal>
      <div
        v-b-tooltip.hover
        :title="
          'By ' +
            book.author +
            '\n' +
            '. Average rating: ' +
            book.average_rating
        "
        class="books"
        v-for="book in books"
        :id="book.id"
        :key="book.name"
        @click="sendInfo(book)"
      >
        <img v-b-modal.modal1 class="books_img" :src="book.image" alt="" />

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
  name: "PastRatings",
  props: {
    button_text: String,
    route: String,
    msg: String
  },
  data: function() {
    return {
      books: [],
      selection: [],
      selectedBook: "",
      new_rating : 0
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
      console.log(selection);
    },
    getbooks: function(books) {
      console.log(window.sessionStorage.userId);
      const path = "http://localhost:5000/get_ratings";
      axios
        .post(path, {
          user_id: window.sessionStorage.userId
        })
        .then(function(response) {
          console.log(response);
          var data = response.data;
          var rating = sessionStorage.userId;
          console.log(rating);
          for (let key in response.data.id) {
            // key = response.data.id[key]
            books.push({
              id: data.id[key],
              name: data.title[key],
              image: data.image_url[key],
              average_rating: data.average_rating[key],
              author: data.authors[key],
              user_rating: data[rating][key]
            });
          }

          console.log(books);
        })

        .catch(function(error) {
          console.log(error);
        });
    },
    sendInfo: function(item) {
      this.selectedBook = item;
    },
    updateRating: function(book_id, old_rating, new_rating){
        console.log(book_id, old_rating, new_rating)
        const path = "http://localhost:5000/update_ratings";
      axios
        .post(path, {
          user_id: window.sessionStorage.userId,
          book_id: book_id,
          old_rating: old_rating,
          new_rating: new_rating
        })
        .then(function(response) {
            console.log(response)
        })
        .catch(function(error) {
          console.log(error);
        });

    }
  }
};
</script>

<style lang="css" scoped>
@import url("PastRatings.css");
</style>

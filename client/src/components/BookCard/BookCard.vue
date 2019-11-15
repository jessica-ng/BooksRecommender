<template>
    <div class="book_selection">
        <div @click="logState($event.target.parentElement.id, selection)" class="books" v-for="book in books" :id="book.id" :key="book.name">
                <img class="books_img" :src="book.image" alt="">
                <h4> {{ book.name }} </h4>
        </div>
        <div>
            <b-button v-on:click="submitRating(selection)" variant="primary">Submit</b-button>
        </div>
    </div>
    
</template>

<script>
import axios from 'axios';

export default {
    name: 'BookCard',
    data: function(){
    return {
        rating : '',
        books: [
            { name: "To kill a Mocking Bird", image: require("../../assets/bookcovers/tkam.jpg"), id: "1"},
            { name: "To kill a Mocking Bird", image: require("../../assets/bookcovers/tkam.jpg"), id: "2"},
            { name: "To kill a Mocking Bird", image: require("../../assets/bookcovers/tkam.jpg"), id: "3"},
            { name: "To kill a Mocking Bird", image: require("../../assets/bookcovers/tkam.jpg"), id: "4"},
            { name: "To kill a Mocking Bird", image: require("../../assets/bookcovers/tkam.jpg"), id: "5"},
            { name: "To kill a Mocking Bird", image: require("../../assets/bookcovers/tkam.jpg"), id: "6"},
            { name: "To kill a Mocking Bird", image: require("../../assets/bookcovers/tkam.jpg"), id: "7"},
            { name: "To kill a Mocking Bird", image: require("../../assets/bookcovers/tkam.jpg"), id: "8"},
        ],
        selection : []
    }
    },
    methods : {
        logState: function(id, selection){
            if (document.getElementById(id).classList.contains('booksActive') == false) {               
                document.getElementById(id).classList.add("booksActive");
                selection.push(id)
            }
            else{
                document.getElementById(id).classList.remove("booksActive");
                selection.splice( selection.indexOf(id), 1 );
            }
        console.log(selection)        
        },
        submitRating: function(selection){
            var i;
            for (i=0; i < selection.length; i++){
                const path = 'http://localhost:5000/sumbitrating';
                axios.post(path, {
                    userid: sessionStorage.userId,
                    bookid: selection[i],
                    rating: 5
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
    
}
</script>

<style lang="css" scoped>
  @import url("BookCard.css");
</style>
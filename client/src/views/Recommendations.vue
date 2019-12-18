<template>
    <div>
        <Recommendations button_text = "Next" route = "" msg = "Recommendations"> </Recommendations>
    </div>
</template>

<script>
import axios from 'axios';
import Recommendations from '@/components/Recommendations/Recommendations.vue'

export default {
    name: "MyRecommendations",
    components: {
        Recommendations
    },
    created() {
        // this.get_recommendations()
    },
    methods: {
        // get_recommendations: function(){
        //     const path = 'http://localhost:5000/get_recommendations';
        //     axios.post(path, {
        //         user_id: sessionStorage.userId,
        //     })
        //     .then(function (response) {
        //         console.log(response.data);
        //     })
        //     .catch(function (error) {
        //         console.log(error);
        //         });
        }
    
}
</script>
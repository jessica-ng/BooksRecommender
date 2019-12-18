<template>
    <div>
        <BookCard :rating = rating button_text = "Next" route = "/onboarding2" msg = "Please select your all time favourites from the list below"> </BookCard>
    </div>
</template>

<script>
import BookCard from '@/components/BookCard/BookCard.vue'

export default {
    name : 'Onboarding1',
    components: {
        BookCard
    },
    data: function () {
        return {
            rating : 5
        }
    }
}
</script>
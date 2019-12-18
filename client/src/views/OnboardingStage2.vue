<template>
    <div>
        <BookCard :rating = rating button_text = "Next" route = "/onboarding3" msg = "Please select books you like from below"> </BookCard>
    </div>
</template>

<script>
import BookCard from '@/components/BookCard/BookCard.vue'

export default {
    name : 'Onboarding2',
    components: {
        BookCard
    },
    data: function () {
        return {
            rating : 3
        }
    }
}
</script>
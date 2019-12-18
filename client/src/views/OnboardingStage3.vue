<template>
    <div>
        <BookCard :rating = rating button_text = "Complete" route = "/about" msg = "Please select books you dislike"> </BookCard>
    </div>
</template>

<script>
import BookCard from '@/components/BookCard/BookCard.vue'

export default {
    name : 'Onboarding3',
    components: {
        BookCard
    },
    data: function () {
        return {
            rating : 0
        }
    }
}
</script>
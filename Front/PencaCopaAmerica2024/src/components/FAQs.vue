<template>
    <div class="faq-page">
        <div class="header">
            <button @click="showIndex" class="back-button">
                <img :src="require('@/assets/Icons/white_back_arrow.svg')" alt="Back to Index" />
            </button>
            <h1 class="title">FAQs</h1>
        </div>
        <div class="faq-item" v-for="(faq, index) in faqs" :key="index">
            <div class="faq-question" @click="toggle(index)">
                <span>{{ faq.question }}</span>
                <span v-if="faq.open">-</span>
                <span v-else>+</span>
            </div>
            <div class="faq-answer" v-if="faq.open">
                <p>{{ faq.answer }}</p>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'FAQPage',
    data() {
        return {
            faqs: [
                {
                    question: 'What is a Penca?',
                    answer: 'A Penca is a prediction game where participants try to predict the outcome of each match in the tournament.',
                    open: false
                },
                {
                    question: 'How can I join a Penca?',
                    answer: 'You can join a Penca by signing up on our website and selecting the "Join Penca" option.',
                    open: false
                },
                {
                    question: 'Is there a prize for the winner?',
                    answer: 'Yes, there is a prize for the participant with the most accurate predictions at the end of the tournament.',
                    open: false
                },
                {
                    question: 'Can I change my predictions?',
                    answer: 'You can change your predictions until one hour before of each match. After that, predictions are locked.',
                    open: false
                },
                {
                    question: 'How are points awarded?',
                    answer: 'Points are awarded based on the accuracy of your predictions. The exact scoring system is detailed in the rules section.',
                    open: false
                },
                {
                    question: 'What happens in case of a tie?',
                    answer: 'In case of a tie, the participant who submitted their predictions first will be declared the winner.',
                    open: false
                }
            ]
        };
    },
    methods: {
        toggle(index) {
            this.faqs[index].open = !this.faqs[index].open;
        },
        showIndex() {
            this.$router.push('/index')
        }
    }
};
</script>

<style scoped>
.faq-page {
    padding: 20px;
}

.title {
    font-size: 700%;
    font-family: 'Impact', sans-serif;
    margin: 10px;
    color: #FBEFEF;
}

.card {
    background-color: #f8f9fa;
}

.back-button {
    position: fixed;
    top: 10px;
    left: 10px;
    padding: 5px;
    background-color: transparent;
    border: none;
}

.back-button img {
    width: 24px;
    height: 24px;
}


.faq-item {
    margin-bottom: 10px;
    border: 1px solid #ddd;
    border-radius: 5px;
}

.faq-question {
    background-color: #1abc9c;
    color: white;
    padding: 10px;
    cursor: pointer;
    display: flex;
    justify-content: space-between;
}

.faq-answer {
    padding: 10px;
    background-color: #f9f9f9;
    border-top: 1px solid #ddd;
    color: #047d65;
}

.button {
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    background-color: #1abc9c;
    color: white;
    cursor: pointer;
}
</style>
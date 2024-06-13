<template>
  <button @click="showIndex" class="back-button">
                <img :src="require('@/assets/Icons/white_back_arrow.svg')" alt="Back to Index" />
            </button>
  <div class="container mt-4">
    <div class="card">
      <div class="card-body">
        <h1 class="card-title">Rules</h1>
        <p class="card-text">Points are calculated based on the result of the 90-minute match (including stoppage time). (does not include extra time or penalties)</p>
        <p class="card-text">In case of a tie in points between users, the one with the highest number of exact results will win.</p>
        <p class="card-text">The ranking of each group will be updated a few minutes after the end of the match.</p>
        <p class="card-text">Points are awarded based on the following rules:</p>
        <ul class="card-text">
          <li>4 points for guessing the exact result!</li>
          <li>2 points for guessing the winning team or a draw!</li>
          <li>10 points for Champion</li>
          <li>5 points for Sub-Champion</li>
        </ul>
        <p class="card-text">The prediction can be entered up to 60 minutes before the start of each match.</p>
        
      </div>
    </div>
  </div>
</template>

<script>
/* eslint-disable vue/multi-word-component-names */
export default {
  name: 'Rules',
    methods: {
        showIndex() {
            this.$router.push('/index')
        }
    }
}
</script>

<style scoped>
h1 {
  color: #bebebe;
}

.card-text {
  text-align: justify;
  color: #bebebe;
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

.card {
  border-radius: 30px;
  background: #e0e0e000;
  box-shadow: 15px 15px 30px #bebebe,
             -15px -15px 30px #ffffff;
}
</style>

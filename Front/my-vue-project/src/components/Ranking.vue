<template>
  <div>
    <header>
      <img :src="logo" alt="UCU Logo" class="logo" />
      <h1>Ranking bro</h1>
    </header>
    <main class="main-frame">
      <div class="ranking-frame">
        <h2>Ranking</h2>
        <button @click="showIndex" class="button">Back to Index</button>
      </div>
    </main>
  </div>
</template>

<script>
export default {
  name: 'RankingPage',
  props: ['username'],
  data() {
    return {
      logo: require('@/assets/ucu_white_logo.png')
    }
  },
  methods: {
    showIndex() {
      this.$router.push({ path: '/index', query: { username: this.username } });
    }
  }
}
</script>

<style scoped>
.logo {
  width: 250px;
  height: 150px;
  margin: 10px auto;
}

h1 {
  text-align: center;
}

.main-frame {
  padding: 20px;
  display: flex;
  justify-content: center;
}

.ranking-frame {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.button {
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  background-color: #1abc9c;
  color: white;
  cursor: pointer;
  margin-top: 20px;
}
</style>

<template>
  <header>
    <button @click="backToPredict" class="back-button">
      <img :src="require('@/assets/Icons/white_back_arrow.svg')" />
    </button>
    <h1 class="title">PREDICTIONS STATS</h1>
  </header>
    <div class="container d-flex justify-content-center align-items-center">
      <div class="card mt-3">
        <div class="card-body row align-items-center">
          <div class="col-4 d-flex justify-content-center align-items-center">
            <img :src="getFlagImage(match['Home team'])" alt="Home Flag" class="flag me-2" />
          </div>
          <div class="col-4 text-center">
            <p class="vs mb-0">vs</p>
          </div>
          <div class="col-4 d-flex justify-content-center align-items-center">
            <img :src="getFlagImage(match['Away team'])" alt="Away Flag" class="flag" />
          </div>
        </div>
        <div class="row text-center mt-3">
          <div class="col-md-4">
            <p class="team mb-0">{{ match['Home team'] }} wins</p>
            <p class="percentage" v-if="stats.Home_Win != null">{{ stats.Home_Win }}%</p>
            <p v-else class="percentage">0%</p>
          </div>
          <div class="col-md-4">
            <p class="team mb-0">Draw</p>
            <p class="percentage" v-if="stats.Tie != null">{{ stats.Tie }}%</p>
            <p v-else class="percentage">0%</p>
          </div>
          <div class="col-md-4">
            <p class="team mb-0">{{ match['Away team'] }} wins</p>
            <p class="percentage" v-if="stats.Away_Win != null">{{ stats.Away_Win }}%</p>
            <p v-else class="percentage">0%</p>
          </div>
        </div>
        <div class="card-footer text-center py-2 custom-card-footer">
          {{ formatDate(match.Date) }}
        </div>
      </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'PredictStats',
  data() {
    return {
      match: {},
      stats: {
        Home_Win: 0,
        Away_Win: 0,
        Tie: 0
      }
    };
  },
  methods: {
    async fetchMatchDetails() {
      try {
        const matchId = this.$route.params.id;
        const token = localStorage.getItem('token');
        const response = await axios.get(`http://localhost:5000/match?id=${matchId}`, {
          headers: {
            Authorization: `Bearer ${token}`
          }
        });
        this.match = response.data;
      } catch (error) {
        console.error('Error fetching match details:', error);
      }
    },
    async fetchStats() {
      try {
        const matchId = this.$route.params.id;
        const token = localStorage.getItem('token');
        const response = await axios.get(`http://localhost:5000/stats?id=${matchId}`, {
          headers: {
            Authorization: `Bearer ${token}`
          }
        });
        if (response.data && response.data.length > 0) {
          this.stats = response.data[0];
        }
      } catch (error) {
        console.error('Error fetching match stats:', error);
      }
    },
    getFlagImage(team) {
      if (!team) return '';
      return require(`@/assets/Flags/Flag_of_${team}.png`);
    },
    backToPredict() {
      this.$router.push('/predict');
    },
    formatDate(date) {
      if (!date) return 'Fecha no disponible';
      const matchDatetime = new Date(date.replace(' GMT', ''));

      const day = matchDatetime.getDate();
      const month = matchDatetime.toLocaleString('es-ES', { month: 'long' });
      const hours = matchDatetime.getHours();
      const minutes = matchDatetime.getMinutes().toString().padStart(2, '0');

      return `${day} de ${month.charAt(0).toUpperCase() + month.slice(1)} | ${hours}:${minutes} hs`;
    }
  },
  created() {
    this.fetchMatchDetails();
    this.fetchStats();
  }
};
</script>
<style scoped>
.stats-container {
  padding: 20px;
  background-color: #f4f4f9;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
.header {
  position: relative;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  margin-bottom: 20px;
}
.back-button {
  position: absolute;
  top: 10px;
  left: 10px;
  background-color: transparent;
  border: none;
  cursor: pointer;
}
.back-button img {
  width: 30px;
  height: auto;
  filter: invert(0%);
}
.title {
  font-size: 700%;
  font-family: 'Impact', sans-serif;
  margin: 10px;
  color: #FBEFEF;
}
.container {
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}
.card {
  width: 90%;
  max-width: 800px;
  background-color: #fff;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  overflow: hidden;
}
.card-body {
  padding: 20px;
}
.flag {
  width: 60px;
  height: auto;
}
.team {
  font-size: 18px;
  font-weight: bold;
  color: #333;
}
.vs {
  font-size: 24px;
  font-weight: bold;
  color: #888;
}
.percentage {
  font-size: 20px;
  font-weight: bold;
  color: #12997e;
}
.custom-card-footer {
  background-color: #12997e;
  color: #fff;
  padding: 10px;
}
</style>

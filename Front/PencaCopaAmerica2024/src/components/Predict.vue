<template>
  <header>
    <button @click="backToIndex" class="back-button">
      <img :src="require('@/assets/Icons/white_back_arrow.svg')" alt="Back to Index" />
    </button>
    <h1 class="title">PREDICTIONS</h1>
  </header>

  <div class="container">
    <div v-for="match in matches" :key="match.id_match" class="mb-4 position-relative">
      <div class="card">
        <div class="card-body row align-items-center">
          <div class="col-4 d-flex justify-content-center align-items-center">
            <img :src="getFlagImage(match['Home team'])" alt="Home Flag" class="flag me-2" />
            <p class="team mb-0">{{ match['Home team'] }}</p>
          </div>

          <div class="col-1 text-center">
            <input type="number" :value="getHomeScore(match)" @input="updateHomeScore(match, $event.target.value)" class="form-control score w-15" min="0" />
          </div>

          <div class="col-2 text-center">
            <p class="team mb-0">vs</p>
          </div>

          <div class="col-1 text-center">
            <input type="number" :value="getAwayScore(match)" @input="updateAwayScore(match, $event.target.value)" class="form-control score w-15" min="0" />
          </div>

          <div class="col-4 d-flex justify-content-center align-items-center">
            <p class="team mb-0 me-2">{{ match['Away team'] }}</p>
            <img :src="getFlagImage(match['Away team'])" alt="Away Flag" class="flag" />
          </div>
        </div>

        <div class="card-footer text-center py-2 custom-card-footer">
          {{ formatDate(match.Date) }}
        </div>

        <button @click="goToMatchStats(match.id_match)" class="details-button">
          <img :src="require('@/assets/Icons/chart-line-.svg')" alt="Details" class="details-icon"/>
        </button>
      </div>
    </div>

    <div class="row">
      <div class="col-12">
        <button @click="submitPredictions" class="button">Submit predictions</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { reactive } from 'vue'

export default {
  name: 'PredictPage',
  data() {
    return {
      matches: [],
      predictions: reactive({})
    }
  },
  computed: {
    groupedMatches() {
      const sortedMatches = [...this.matches].sort((a, b) => new Date(a.Date) - new Date(b.Date))
      return sortedMatches.reduce((groups, match) => {
        const date = new Date(match.Date.replace(' GMT', '')).toISOString().split('T')[0]
        if (!groups[date]) {
          groups[date] = []
        }
        groups[date].push(match)
        return groups
      }, {})
    }
  },
  methods: {
    async fetchMatches() {
      try {
        const token = localStorage.getItem('token')
        const response = await axios.get('http://localhost:5000/matches?predictable=true', {
          headers: {
            'Authorization': `Bearer ${token}`
          }
        })
        if (response.status === 200) {
          this.matches = response.data
          this.initializePredictions()
        } else {
          alert('Failed to fetch matches')
        }
      } catch (error) {
        alert(`Failed to fetch matches: ${error}`)
      }
      // Ordenar los partidos por fecha y hora
      this.matches.sort((a, b) => new Date(a.Date) - new Date(b.Date))
    },
    initializePredictions() {
      this.matches.forEach(match => {
        if (!this.predictions[match.id_match]) {
          this.predictions[match.id_match] = {
            home_score: match.home_score ?? '',
            away_score: match.away_score ?? '',
            id_home_country: match.id_home_country,
            id_away_country: match.id_away_country
          }
        }
      })
    },
    formatTime(date) {
      const matchDatetime = new Date(date.replace(' GMT', ''))
      return matchDatetime.toLocaleTimeString('en-GB', { hour: '2-digit', minute: '2-digit' })
    },
    formatDate(date) {
      const matchDatetime = new Date(date.replace(' GMT', ''))

      const day = matchDatetime.getDate()
      const month = matchDatetime.toLocaleString('es-ES', { month: 'long' })
      const hours = matchDatetime.getHours()
      const minutes = matchDatetime.getMinutes().toString().padStart(2, '0')

      return `${day} de ${month.charAt(0).toUpperCase() + month.slice(1)} | ${hours}:${minutes} hs`
    },
    getFlagImage(team) {
      try {
        return require(`@/assets/Flags/Flag_of_${team}.png`)
      } catch {
        return null
      }
    },
    getHomeScore(match) {
      return this.predictions[match.id_match]?.home_score ?? ''
    },
    getAwayScore(match) {
      return this.predictions[match.id_match]?.away_score ?? ''
    },
    updateHomeScore(match, value) {
      if (value < 0) value = 0
      if (!this.predictions[match.id_match]) {
        this.predictions[match.id_match] = {
          id_home_country: match.id_home_country,
          id_away_country: match.id_away_country
        }
      }
      this.predictions[match.id_match].home_score = value
    },
    updateAwayScore(match, value) {
      if (value < 0) value = 0
      if (!this.predictions[match.id_match]) {
        this.predictions[match.id_match] = {
          id_home_country: match.id_home_country,
          id_away_country: match.id_away_country
        }
      }
      this.predictions[match.id_match].away_score = value
    },
    async submitPredictions() {
      try {
        const token = localStorage.getItem('token')
        const formattedPredictions = Object.keys(this.predictions).map(matchId => ({
          id_match: parseInt(matchId),
          home_score: this.predictions[matchId].home_score,
          away_score: this.predictions[matchId].away_score,
          id_home_country: this.predictions[matchId].id_home_country,
          id_away_country: this.predictions[matchId].id_away_country
        }))

        const response = await axios.post('http://localhost:5000/predictions', {
          predictions: formattedPredictions
        }, {
          headers: {
            'Authorization': `Bearer ${token}`
          }
        })

        if (response.status === 200) {
          alert('Predictions submitted successfully')
        } else {
          alert('Failed to submit predictions')
        }
      } catch (error) {
        alert(`Failed to submit predictions: ${error}`)
      }
    },
    backToIndex() {
      this.$router.push('/index')
    },
    goToMatchStats(id) {
      this.$router.push(`/predictStats/${id}`)
    }
  },
  mounted() {
    this.fetchMatches()
  }
}
</script>

<style scoped>
.title {
  font-size: 700%;
  font-family: 'Impact', sans-serif;
  margin: 10px;
  color: #FBEFEF;
}

.button {
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  background-color: #1abc9c;
  color: white;
  cursor: pointer;
  margin: 10px;
}

input {
  background-color: #FBEFEF;
}

.custom-card-footer {
  background-color: #12997e;
  color: white;
}

.card {
  background-color: #FBEFEF;
  position: relative;
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

.scrollable-frame {
  max-height: 70vh;
  overflow-y: auto;
  padding: 20px;
}

.flag {
  width: 30px;
  height: 20px;
}

.team {
  font-weight: bold;
}

.time {
  font-style: italic;
}

.score {
  text-align: center;
}

.details-button {
  position: absolute;
  top: 10px;
  left: 10px;
  background-color: transparent;
  border: none;
  cursor: pointer;
  z-index: 10; 
  transition: transform 0.3s ease; 
}

.details-button:hover {
  transform: scale(1.1); 
}

.details-button img {
  width: 24px; 
  height: 24px;
}

</style>

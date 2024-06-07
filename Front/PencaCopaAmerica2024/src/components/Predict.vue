<template>
  <div>
    <header>
      <img :src="logo" alt="UCU Logo" class="logo" />
      <h1>Predict Matches</h1>
    </header>
    <main class="main-frame">
      <div class="button-frame">
        <button @click="submitPredictions" class="button">Submit Predictions</button>
        <button @click="backToIndex" class="button">Back to Index</button>
      </div>
      <div class="scrollable-frame">
        <div v-for="(matches, date) in groupedMatches" :key="date">
          <h2>{{ date }}</h2>
          <div v-for="match in matches" :key="match.id_match" class="match-frame">
            <div class="match-inner-frame">
              <span class="time">{{ formatTime(match.Date) }}</span>
              <img :src="getFlagImage(match['Home team'])" alt="Home Flag" class="flag" />
              <span class="team">{{ match['Home team'] }} [</span>
              <input type="number" :value="getHomeScore(match)" @input="updateHomeScore(match, $event.target.value)" class="score" min="0" />
              <span class="team">] Vs [</span>
              <input type="number" :value="getAwayScore(match)" @input="updateAwayScore(match, $event.target.value)" class="score" min="0" />
              <span class="team">] {{ match['Away team'] }}</span>
              <img :src="getFlagImage(match['Away team'])" alt="Away Flag" class="flag" />
            </div>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script>
import axios from 'axios'
import { reactive } from 'vue'

export default {
  name: 'PredictPage',
  data() {
    return {
      logo: require('@/assets/ucu_white_logo.png'),
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
    }
  },
  mounted() {
    this.fetchMatches()
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
}

.button-frame {
  text-align: center;
  margin: 20px;
}

.button {
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  background-color: #1abc9c;
  color: white;
  cursor: pointer;
}

.scrollable-frame {
  max-height: 70vh;
  overflow-y: auto;
  padding: 20px;
}

.match-frame {
  margin-bottom: 20px;
  display: flex;
  justify-content: center; /* Centra el contenido horizontalmente */
}

.match-inner-frame {
  display: flex;
  align-items: center;
  gap: 10px;
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
  width: 50px;
  text-align: center;
}
</style>

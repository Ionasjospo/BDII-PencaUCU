<template>
  <div>
    <header>
      <img :src="logo" alt="UCU Logo" class="logo" />
      <h1>Predict Matches</h1>
    </header>
    <div class="button-frame">
      <button @click="submitPredictions" class="button">Submit Predictions</button>
      <button @click="showIndex" class="button">Back to Index</button>
    </div>
    <div class="frame">
      <div v-for="(matches, date) in groupedMatches" :key="date">
        <h2>{{ date }}</h2>
        <div v-for="match in matches" :key="match.id_match" class="match">
          <div class="match-inner-frame">
            <span class="time">{{ formatTime(match.Date) }}</span>
            <img :src="getFlagImage(match['Home team'])" alt="Home Flag" class="flag" />
            <span class="team">{{ match['Home team'] }} [</span>
            <input v-if="predictions[match.id_match]" type="number" v-model.number="predictions[match.id_match].home_score" class="score" />
            <span class="team">] Vs [</span>
            <input v-if="predictions[match.id_match]" type="number" v-model.number="predictions[match.id_match].away_score" class="score" />
            <span class="team">] {{ match['Away team'] }}</span>
            <img :src="getFlagImage(match['Away team'])" alt="Away Flag" class="flag" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'PredictPage',
  props: ['username'],
  data() {
    return {
      logo: require('@/assets/ucu_white_logo.png'),
      matches: [],
      predictions: {}
    }
  },
  computed: {
    groupedMatches() {
      return this.matches.reduce((groups, match) => {
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
    showIndex() {
      this.$router.push({ path: '/index', query: { username: this.username } });
    },
    async fetchAndDisplayMatches() {
      try {
        const response = await axios.get(`http://localhost:5000/matches?predictable=true&username=${this.username}`)
        if (response.status === 200) {
          this.matches = response.data
          this.matches.forEach(match => {
            this.predictions[match.id_match] = {
              home_score: match.home_score ?? null,
              away_score: match.away_score ?? null,
              id_home_country: match.id_home_country,
              id_away_country: match.id_away_country
            }
          })
        } else {
          alert('Failed to fetch matches')
        }
      } catch (error) {
        alert(`Failed to fetch matches: ${error}`)
      }
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
    async submitPredictions() {
      const predictionData = {
        username: this.username,
        predictions: []
      }

      for (const matchId in this.predictions) {
        const { home_score, away_score, id_home_country, id_away_country } = this.predictions[matchId]
        if (home_score >= 0 && away_score >= 0 && id_home_country && id_away_country) {
          predictionData.predictions.push({
            id_match: matchId,
            home_score,
            away_score,
            id_home_country,
            id_away_country
          })
        }
      }

      if (predictionData.predictions.length > 0) {
        try {
          const response = await axios.post('http://localhost:5000/predictions', predictionData)
          if (response.status === 200) {
            alert('Predictions submitted successfully')
          } else {
            alert('Failed to submit predictions')
          }
        } catch (error) {
          alert(`Failed to submit predictions: ${error}`)
        }
      } else {
        alert('No valid predictions to submit')
      }
    }
  },
  mounted() {
    this.fetchAndDisplayMatches()
  }
}
</script>


<style scoped>
.logo {
  width: 250px;
  height: 150px;
  margin: 10px auto;
}

h1, h2 {
  text-align: center;
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

.frame {
  padding: 20px;
  max-height: 70vh;
  overflow-y: auto;
}

.match {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 10px;
  border-bottom: 1px solid #ccc;
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

.vs {
  margin: 0 10px;
}

.time {
  font-style: italic;
}

.score {
  width: 50px;
  text-align: center;
}
</style>

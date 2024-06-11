<template>
    <div>
      <header>
        <img :src="logo" alt="UCU Logo" class="logo" />
        <h1>Upload the final football match results</h1>
      </header>
      <main class="main-frame">
        <div class="button-frame">
          <button @click="submitMatches" class="button">Submit</button>
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
                <input type="number" v-model.number="matchesData[match.id_match].home_score" class="score" />
                <span class="team">] Vs [</span>
                <input type="number" v-model.number="matchesData[match.id_match].away_score" class="score" />
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
  
  export default {
  name: 'AdminResults',
  data() {
    return {
      logo: require('@/assets/ucu_white_logo.png'),
      matches: [],
      matchesData: {}
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
    backToIndex() {
        this.$router.push('/adminIndex');
      },
    async fetchMatches() {
      try {
        const token = localStorage.getItem('token')
        const response = await axios.get('http://localhost:5000/matches?predictable=false&results_admin=true&username=admin', {
          headers: {
            'Authorization': `Bearer ${token}`
          }
        })
        if (response.status === 200) {
          this.matches = response.data
          this.matches.forEach(match => {
            this.matchesData[match.id_match] = {
              home_score: match.home_score ?? null,
              away_score: match.away_score ?? null,
              id_home_country: match.id_home_country,
              id_away_country: match.id_away_country
            }
          })
        }else if (response.status === 204) {
          alert('No matches to submit results.')
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
    async submitMatches() {
      const matchesUpdatedData = {
        matches_updated: []
      }
  
      for (const matchId in this.matchesData) {
        const { home_score, away_score, id_home_country, id_away_country } = this.matchesData[matchId]
        if (home_score >= 0 && away_score >= 0 && id_home_country && id_away_country) {
          matchesUpdatedData.matches_updated.push({
            id_match: matchId,
            home_score,
            away_score
          })
        }
      }
  
      if (matchesUpdatedData.matches_updated.length > 0) {
        try {
          const token = localStorage.getItem('token')
          const response = await axios.post('http://localhost:5000/submit_matches', matchesUpdatedData, {
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
      } else {
        alert('No valid predictions to submit')
      }
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
  margin: 5px;
  }
  
  .scrollable-frame {
  max-height: 70vh;
  overflow-y: auto;
  padding: 20px;
  }
  
  .match-frame {
  margin-bottom: 20px;
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
  
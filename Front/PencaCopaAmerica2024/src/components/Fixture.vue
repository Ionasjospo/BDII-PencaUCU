<template>
  <div>
    <header>
      <img :src="logo" alt="UCU Logo" class="logo" />
      <h1>Fixture bro</h1>
    </header>
    <div class="button-frame">
      <button @click="showIndex" class="button">Back to Index</button>
    </div>
    <div class="frame">
      <div v-for="(matches, group) in groupedMatches" :key="group">
        <h2>{{ group }}</h2>
        <div v-for="match in matches" :key="match.Date" class="match">
          <div class="match-inner-frame">
            <span class="time">{{ formatDate(match.Date) }}</span>
            <img :src="getFlagImage(match['Home team'])" alt="Home Flag" class="flag" />
            <span class="team">{{ match['Home team'] }}</span>
            <span class="vs">Vs</span>
            <span class="team">{{ match['Away team'] }}</span>
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
  name: 'FixturePage',
  data() {
    return {
      logo: require('@/assets/ucu_white_logo.png'),
      matches: []
    }
  },
  computed: {
    groupedMatches() {
      return this.matches.reduce((groups, match) => {
        const group = match.Group || 'Others'
        if (!groups[group]) {
          groups[group] = []
        }
        groups[group].push(match)
        return groups
      }, {})
    }
  },
  methods: {
    showIndex() {
      this.$router.push('/index')
    },
    async fetchMatches() {
      const groups = ['A', 'B', 'C']
      const token = localStorage.getItem('token')
      let fetchedMatches = []
      for (const group of groups) {
        try {
          const response = await axios.get(`http://localhost:5000/matches?group=${group}`, {
            headers: {
              'Authorization': `Bearer ${token}`
            }
          })
          if (response.status === 200) {
            fetchedMatches = [...fetchedMatches, ...response.data]
          } else {
            alert('Failed to load matches')
          }
        } catch (error) {
          alert(`Failed to load matches: ${error}`)
        }
      }
      // Ordenar los partidos por fecha y hora
      fetchedMatches.sort((a, b) => new Date(a.Date) - new Date(b.Date))
      this.matches = fetchedMatches
    },
    formatDate(date) {
      const matchDatetime = new Date(date.replace(' GMT', ''))
      return matchDatetime.toLocaleString('en-GB', { day: '2-digit', month: '2-digit', hour: '2-digit', minute: '2-digit' })
    },
    getFlagImage(team) {
      const flagPath = require(`@/assets/Flags/Flag_of_${team}.png`)
      return flagPath ? flagPath : null
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
</style>

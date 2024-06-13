<template>
  <header>
    <button @click="showIndex" class="back-button">
      <img :src="require('@/assets/Icons/white_back_arrow.svg')" alt="Back to Index" />
    </button>
    <h1 class="title">FIXTURE</h1>
  </header>

  <div class="container">
    <div class="row text-center">
      <div class="col-6">
        <h4>Home</h4>
      </div>

      <div class="col-6">
        <h4>Away</h4>
      </div>
    </div>
  </div> 
    
  <div class="container">
    <div v-for="(matches, group) in groupedMatches" :key="group">
      <div v-for="match in matches" :key="match.Date" class="mb-4">
          
        <div class="card">
          <div class="card-body row align-items-center">
            <div class="col-4 d-flex justify-content-center align-items-center">
              <img :src="getFlagImage(match['Home team'])" alt="Home Flag" class="flag me-2" />
              <p class="team mb-0">{{ match['Home team'] }}</p>
            </div>

            <div class="col-4 text-center">
              <p class="team mb-0">vs</p>
            </div>

            <div class="col-4 d-flex justify-content-center align-items-center">
              <p class="team mb-0 me-2">{{ match['Away team'] }}</p>
              <img :src="getFlagImage(match['Away team'])" alt="Away Flag" class="flag" />
            </div>
          </div>

          <div class="card-footer text-center py-2 custom-card-footer">
            {{ formatDate(match.Date) }}
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
      
    
      const day = matchDatetime.getDate()
      const month = matchDatetime.toLocaleString('es-ES', { month: 'long' })
      const hours = matchDatetime.getHours()
      const minutes = matchDatetime.getMinutes().toString().padStart(2, '0')

      return `${day} de ${month.charAt(0).toUpperCase() + month.slice(1)} | ${hours}:${minutes} hs`
    }

,
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
.title {
  font-size: 700%;
  font-family: 'Impact', sans-serif;
  margin: 10px;
  color: #FBEFEF;
}

.card{
  background-color: #f8f9fa;
}

.back-button {
  position: absolute;
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

.custom-card-footer{
  background-color: #12997e;
  color: #f8f9fa; 
}

h1, h2 {
  text-align: center;
}

.button {
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  background-color: #1abc9c;
  color: white;
  cursor: pointer;
}

.flag {
  width: 20%;
  height: auto;
}

.team {
  color: black;
}

.time {
  font-style: italic;
}
</style>

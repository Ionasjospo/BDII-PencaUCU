<template>
  <div>
    <header>
      <button @click="backToIndex" class="back-button">
        <img :src="require('@/assets/Icons/white_back_arrow.svg')" alt="Back to Index" />
      </button>
      <h1 class="title">RANKING</h1>
    </header>
    
    <main class="main-frame">
      <div class="container mt-3">
        <table class="table table-striped table-hover table-bordered rounded-lg">
          <thead class="thead-dark">
            <tr>
              <th scope="col">Rank</th>
              <th scope="col">Username</th>
              <th scope="col">Points</th>
              <th scope="col">Champion</th>
              <th scope="col">Sub Champion</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(entry, index) in ranking" :key="entry.Username" :class="{ 'table-primary': entry.Username === loggedInUsername }">
              <th scope="row">{{ index + 1 }}</th>
              <td>{{ entry.Username }}</td>
              <td>{{ entry['Total Points'] }}</td>
              <td><img :src="flags[entry.Champion]" alt="Champion Flag" class="flag" /></td>
              <td><img :src="flags[entry['Sub Champion']]" alt="Sub Champion Flag" class="flag" /></td>
            </tr>
          </tbody>
        </table>
      </div>
    </main>
  
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'RankingPage',
  data() {
    return {
      logo: require('@/assets/ucu_white_logo.png'),
      ranking: [],
      flags: {},
      loggedInUsername: null 
    };
  },
  methods: {
    async fetchRanking() {
      const token = localStorage.getItem('token');
      try {
        const response = await axios.get('http://localhost:5000/ranking', {
          headers: {
            'Authorization': `Bearer ${token}`
          }
        });
        if (response.status === 200) {
          this.ranking = response.data.ranking;
          this.loggedInUsername = response.data.username; 
          this.loadFlags();
        } else {
          alert('Failed to fetch ranking');
        }
      } catch (error) {
        alert(`Failed to fetch ranking: ${error}`);
      }
    },
    async loadFlags() {
      for (const entry of this.ranking) {
        if (!this.flags[entry.Champion]) {
          this.flags[entry.Champion] = await this.fetchFlagImage(entry.Champion);
        }
        if (!this.flags[entry['Sub Champion']]) {
          this.flags[entry['Sub Champion']] = await this.fetchFlagImage(entry['Sub Champion']);
        }
      }
    },
    async fetchFlagImage(countryId) {
      try {
        const response = await axios.get(`http://localhost:5000/country/id?id=${countryId}`);
        if (response.status === 200) {
          const countryData = response.data;
          const flagPath = require(`@/assets/Flags/Flag_of_${countryData}.png`);
          return flagPath ? flagPath : null;
        } else {
          console.error(`Failed to fetch flag image for country ID ${countryId}`);
          return null;
        }
      } catch (error) {
        console.error(`Error fetching flag image for country ID ${countryId}: ${error}`);
        return null;
      }
    },
    backToIndex() {
      this.$router.push('/index');
    }
  },
  mounted() {
    this.fetchRanking();
  }
};
</script>

<style scoped>
.main-frame {
  background: transparent
}

.table {
  border-radius: 7px;   
  overflow: hidden;
}

.flag {
  width: 30px;
  height: 20px;
}

.table-primary {
  background-color: #b8daff;
}

header {
  color: white;
  text-align: center;
  padding: 20px 0;
  position: relative;
}
.title {
  font-size: 700%;
  font-family: 'Impact', sans-serif;
  margin: 10px;
  color: #FBEFEF;
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



.button-frame {
  text-align: center;
  margin: 20px;
}

.button {
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  background-color: #3498db; 
  color: white;
  cursor: pointer;
}


table {
  width: 100%;
  border-collapse: collapse;
  margin: 20px 0;
  font-size: 1em;
  min-width: 400px;
}

th, td {
  padding: 12px 15px;
  border: 1px solid #ddd;
  text-align: center;
}

th {
  background-color: #3498db; 
  color: white;
}

/* .flag {
  width: 30px;
  height: 20px;
} */

.logged-in-user {
  background-color: #007eec !important; 
}
</style>

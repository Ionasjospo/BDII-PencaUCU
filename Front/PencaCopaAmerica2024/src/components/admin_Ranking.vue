<template>
    <div>
      <header>
        <img :src="logo" alt="UCU Logo" class="logo" />
        <h1>Ranking</h1>
      </header>
      <main class="main-frame">
        <div class="button-frame">
          <button @click="backToIndex" class="button">Back to Index</button>
        </div>
        <div class="table-container">
          <table>
            <thead>
              <tr>
                <th>Rank</th>
                <th>Username</th>
                <th>Points</th>
                <th>Champion</th>
                <th>Sub Champion</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(entry, index) in ranking" :key="entry.Username" :class="{ 'logged-in-user': entry.Username === loggedInUsername }">
                <td>{{ index + 1 }}</td>
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
    name: 'AdminRankingPage',
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
        this.$router.push('/adminIndex');
      }
    },
    mounted() {
      this.fetchRanking();
    }
  };
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
    background-color: #3498db; 
    color: white;
    cursor: pointer;
  }
  
  .table-container {
    width: 100%;
    overflow-x: auto;
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
  
  .flag {
    width: 30px;
    height: 20px;
  }
  </style>
  
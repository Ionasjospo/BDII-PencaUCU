<template>
  <div id="app">
    <header>
      <h1 class="title">MENU</h1>
      
      <div class="container">
        <div class="row justify-content-center">
          <div class="col-md-8">
            <p class="responsive-paragraph">
              Welcome to Penca UCU 🌟 <br> 
              The best site for sports predictions and friendly competitions. 
              Whether you’re here to analyze fixtures, climb the rankings, 
              or make accurate predictions, Penca has you covered. 
              Let’s kick off the excitement together! 🏆⚽📈
            </p>
          </div>
        </div>
      </div>
      
      <div class="header-icons">
          <img :src="require('@/assets/Icons/logout.png')" alt="Logout Icon" class="icon" @click="logout"/>
      </div>
    </header>
    
    <main>
      <div class="container mt-3">
        <div class="row d-flex justify-content-center">
          <div class="col-sm d-flex justify-content-center mb-3">
            <button @click="showFixture" class="button-card">
              <img :src="require('@/assets/Icons/fixture.png')" alt="Fixture Icon" class="icon"/>
              <span style = "font-weight: bold;">Fixture</span>
            </button>
          </div>
          <div class="col-sm d-flex justify-content-center mb-3">
            <button @click="showRanking" class="button-card">
              <img :src="require('@/assets/Icons/ranking.png')" alt="Ranking Icon" class="icon"/>
              <span style = "font-weight: bold;">Ranking</span>
            </button>
          </div>
          <div class="col-sm d-flex justify-content-center mb-3">
            <button @click="showResults" class="button-card">
              <img :src="require('@/assets/Icons/checklist.png')" alt="Results Icon" class="icon"/>
              <span style = "font-weight: bold;">Results</span>
            </button>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>


<script>
//import axios from 'axios';

export default {
  name: 'AdminIndexPage',
  data() {
    return {
      showDropdown: false,
      notifications: [],
      unreadNotificationsCount: 0,
    };
  },
  methods: {
    showFixture() {
      this.$router.push('/adminFixture');
    },
    showRanking() {
      this.$router.push('/adminRanking');
    },
    showResults() {
      this.$router.push('/adminResults');
    },
    logout() {
      localStorage.removeItem('token');
      this.$router.push('/');
    },
  },
  mounted() {
  }
}
</script>

<style scoped>
#app {
  text-align: center;
}


.title {
  font-size: 700%;
  font-family: 'Impact', sans-serif;
  margin: 10px;
  color: #FBEFEF;
  /* color: #CBFFA9; */
}

.logo {
  width: 250px;
  height: 150px;
  margin: 10px auto;
}

h1 {
  font-family: Arial, sans-serif;
  font-size: 18px;
  padding: 10px;
}


.header-icons {
  position: absolute;
  top: 20px;
  right: 20px;
}

.header-icons .icon {
  width: 24px;
  height: 24px;
  margin: 0 10px;
  cursor: pointer;
}

.notification-icon {
  position: relative;
  display: inline-block;
}

.notification-badge {
  position: absolute;
  top: -5px;
  right: -5px;
  background: red;
  color: white;
  border-radius: 50%;
  padding: 2px 6px;
  font-size: 12px;
}

.button-container {
  display: flex;
  justify-content: center;
  gap: 20px;
  padding: 20px;
}

.button-card {
  width: 350px;
  height: 350px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  border: 1px solid #ccc;
  border-radius: 10px;
  background-color: #139279;
  color: #000000;
  cursor: pointer;
  transition: background-color 0.3s;
}

.button-card:hover {
  background-color: #ffffff;
}

.button-card .icon {
  width: 100px;
  height: 100px;
  margin-bottom: 10px;
}

.notification-dropdown {
  position: absolute;
  top: 50px;
  right: 20px;
  width: 300px;
  color: black;
  background: white;
  border: 1px solid #ccc;
  border-radius: 5px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.notification-dropdown ul {
  list-style: none;
  padding: 10px;
  margin: 0;
}

.notification-dropdown li {
  padding: 10px;
  border-bottom: 1px solid #cccccc57;
}

.notification-dropdown li:hover {
  cursor: pointer;
  padding: 10px;
  background-color: #f3f3f3cf;
  border-bottom: 1px solid #cccccc57;
}

.notification-dropdown li:last-child {
  border-bottom: none;
}
</style>

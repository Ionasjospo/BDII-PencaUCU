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
        <img :src="require('@/assets/Icons/notification.png')" alt="Notification Icon" class="icon" @click="showNotifications"/>
        <img :src="require('@/assets/Icons/settings.png')" alt="Settings Icon" class="icon" @click="showProfileSettings"/>
        <img :src="require('@/assets/Icons/logout.png')" alt="Logout Icon" class="icon" @click="logout"/>
      </div>
    </header>
    
    <main>
    
    <div class="container mt-3">
      <div class="row d-flex justify-content-center">
        <div class="col-sm d-flex justify-content-center mb-3">
          <button @click="showFixture" class="button-card">
            <img :src="require('@/assets/Icons/fixture.png')" alt="Fixture Icon" class="icon"/>
            <span>Fixture</span>
          </button>
        </div>
        <div class="col-sm d-flex justify-content-center mb-3">
          <button @click="showRanking" class="button-card">
            <img :src="require('@/assets/Icons/ranking.png')" alt="Ranking Icon" class="icon"/>
            <span>Ranking</span>
          </button>
        </div>
        <div class="col-sm d-flex justify-content-center mb-3">
          <button @click="showPredict" class="button-card">
            <img :src="require('@/assets/Icons/prediction.png')" alt="Prediction Icon" class="icon"/>
            <span>Predict</span>
          </button>
        </div>
      </div>
    </div>

    </main>
  </div>
</template>

<script>
export default {
  name: 'IndexPage',
  methods: {
    showFixture() {
      this.$router.push('/fixture');
    },
    showRanking() {
      this.$router.push('/ranking');
    },
    showPredict() {
      this.$router.push('/predict');
    },
    showNotifications() {
      // Logic to show notifications
      alert("Show notifications");
    },
    showProfileSettings() {
      this.$router.push('/profile');
    },
    logout() {
      // Remove the JWT token from localStorage
      localStorage.removeItem('token');
      // Redirect to the login page
      this.$router.push('/');
    }
  }
}
</script>

<style scoped>
#app {
  text-align: center;
}


.title {
  font-size: 900%;
  font-family: 'Impact', sans-serif;
  margin: 10px;
  color: #8ee9ce;
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


.button-card {
  width: 350px;
  height: 350px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  border: 1px solid #ccc;
  border-radius: 10px;
  background-color: #F3F7EC;
  color: #000000;
  cursor: pointer;
  transition: background-color 0.3s;
}

.button-card:hover {
  background-color: #555;
}

.button-card .icon {
  width: 100px;
  height: 100px;
  margin-bottom: 10px;
}
</style>

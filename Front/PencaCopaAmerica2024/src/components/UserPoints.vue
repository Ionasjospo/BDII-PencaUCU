<template>
    <div id="app">
        <header>
            <button @click="backToIndex" class="back-button">
                <img :src="require('@/assets/Icons/white_back_arrow.svg')" alt="Back to Index" />
            </button>

            <h1 class="title">YOUR POINTS</h1>

            <div class="header-icons">
                <div class="notification-icon" @click="showNotifications">
                    <img :src="require('@/assets/Icons/notification.png')" alt="Notification Icon" class="icon" />
                    <span v-if="unreadNotificationsCount > 0" class="notification-badge">{{ unreadNotificationsCount
                        }}</span>
                </div>
                <img :src="require('@/assets/Icons/settings.png')" alt="Settings Icon" class="icon"
                    @click="showProfileSettings" />
                <img :src="require('@/assets/Icons/logout.png')" alt="Logout Icon" class="icon" @click="logout" />
            </div>
        </header>

        <main>

            <div class="container">
                <div class="row">
                    <div class="col-12">
                        <h5 class="text-center">Total points: {{ total_points }}</h5>
                    </div>
                </div>
            </div>

            <div class="container custom-container">
                <div v-for="prediction in old_predictions" :key="prediction.id_match" class="mb-4">

                    <div class="card">
                        <div class="card-body row align-items-center">
                            <div class="col-4 d-flex justify-content-center align-items-center">
                                <img :src="getFlagImage(prediction.home_country)" alt="Home Flag" class="flag me-2" />
                                <p class="team mb-0">{{ prediction.home_country }}</p>
                            </div>

                            <div class="col-1 text-center">
                                <input type="number"
                                    v-model.number="old_predictions_data[prediction.id_match].home_score"
                                    class="form-control score w-15" min="0" />
                            </div>

                            <div class="col-2 text-center">
                                <p class="team mb-0">vs</p>
                            </div>

                            <div class="col-1 text-center">
                                <input type="number"
                                    v-model.number="old_predictions_data[prediction.id_match].away_score"
                                    class="form-control score w-15" min="0" />
                            </div>

                            <div class="col-4 d-flex justify-content-center align-items-center">
                                <p class="team mb-0 me-2">{{ prediction.away_country }}</p>
                                <img :src="getFlagImage(prediction.away_country)" alt="Away Flag" class="flag" />
                            </div>
                        </div>

                        <div class="card-footer text-center py-2 custom-card-footer">
                            <p>{{ old_predictions_data[prediction.id_match].points }} points.</p>
                        </div>
                    </div>
                </div>
            </div>
        </main>
    </div>
</template>


<script>
import axios from 'axios';

export default {
    components: {
    },
    name: 'UserPointsPage',
    data() {
        return {
            showDropdown: false,
            notifications: [],
            total_points: 0,
            unreadNotificationsCount: 0,
            old_predictions: [],
            old_predictions_data: {}
        };
    },
    computed: {
    },
    methods: {
    backToIndex() {
        this.$router.push('/index')
    },
        async fetchTotalPoints() {
        try {
            const token = localStorage.getItem('token');
            const response = await axios.get('http://localhost:5000/points', {
                headers: {
                    'Authorization': `Bearer ${token}`
                }
            });
            if (response.status === 200) {
                this.total_points = response.data;
            } else {
                alert('Failed to load points');
            }
        } catch (error) {
            alert(`Failed to load points: ${error}`);
        }
    },
        async fetchOldsPredictions() {
        try {
            const token = localStorage.getItem('token')
            const response = await axios.get('http://localhost:5000/old_predictions', {
                headers: {
                    'Authorization': `Bearer ${token}`
                }
            })
            if (response.status === 200) {
                this.old_predictions = response.data
                this.old_predictions.forEach(prediction => {
                    this.old_predictions_data[prediction.id_match] = {
                        home_country: prediction.home_country,
                        home_score: prediction.home_score ?? null,
                        away_country: prediction.away_country,
                        away_score: prediction.away_score ?? null,
                        points: (prediction.points != null ? prediction.points : 0)
                    }
                })
                console.log(this.old_predictions_data)
            } else if (response.status === 204) {
                alert('No predictions to submit results.')
            } else {
                alert('Failed to fetch predictions')
            }
        } catch (error) {
            alert(`Failed to fetch predictions: ${error}`)
        }
    },
    getFlagImage(team) {
        try {
            return require(`@/assets/Flags/Flag_of_${team}.png`)
        } catch {
            return null
        }
    },
    showNotifications() {
        this.showDropdown = !this.showDropdown;
        if (this.showDropdown) {
            this.fetchNotifications();
        }
    },
    showProfileSettings() {
        this.$router.push('/profile');
    },
    logout() {
        localStorage.removeItem('token');
        this.$router.push('/');
    },
        async fetchNotifications() {
        try {
            const token = localStorage.getItem('token');
            const response = await axios.get('http://localhost:5000/notifications', {
                headers: {
                    'Authorization': `Bearer ${token}`
                }
            });
            if (response.status === 200) {
                this.notifications = response.data;
                this.unreadNotificationsCount = this.notifications.length;
            } else {
                alert('Failed to load notifications');
            }
        } catch (error) {
            alert(`Failed to load notifications: ${error}`);
        }
    }
},
mounted() {
    //   this.fetchNotifications();
    this.fetchTotalPoints();
    this.fetchOldsPredictions();
}
}
</script>

<style scoped>
/* Scrollbar styles */
.custom-container {
    max-height: 400px; 
    overflow-y: auto; 
    scrollbar-width: thin; 
    scrollbar-color: #8bcdcd #e0e0e0; 
}

.custom-container::-webkit-scrollbar {
    width: 12px;
}

.custom-container::-webkit-scrollbar-track {
    background: #e0e0e0;
    border-radius: 10px;
}

.custom-container::-webkit-scrollbar-thumb {
    background-color: #8bcdcd;
    border-radius: 10px;
    border: 3px solid #e0e0e0;
}

.custom-container::-webkit-scrollbar-thumb:hover {
    background-color: #6bb5b5;
}

.custom-container {
    scrollbar-width: thin;
    scrollbar-color: #8bcdcd #e0e0e0;
}

.custom-container::-ms-scrollbar {
    width: 12px;
}

.custom-container::-ms-scrollbar-track {
    background: #e0e0e0;
    border-radius: 10px;
}

.custom-container::-ms-scrollbar-thumb {
    background-color: #8bcdcd;
    border-radius: 10px;
    border: 3px solid #e0e0e0;
}

.custom-container::-ms-scrollbar-thumb:hover {
    background-color: #6bb5b5;
}

.scroll-area {
  position: relative;
  margin: auto;
  width: 600px;
  height: 400px;
}

.container {
    max-width: 1000px;
    margin: 0 auto;
}

.scroll-area {
    position: relative;
    margin: auto;
}

.card {
    margin-bottom: 20px;
}

.flag {
    width: 30px;
    height: 20px;
}

.score {
    width: 50px;
}

.custom-card-footer {
    background-color: #f8f9fa;
}


#app {
    text-align: center;
}

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
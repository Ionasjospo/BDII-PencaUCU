<template>
  <header>
    <button @click="backToIndex" class="back-button">
      <img :src="require('@/assets/Icons/white_back_arrow.svg')" alt="Back to Index" />
    </button>
    <div class="header-icons">
        <div class="notification-icon" @click="showNotifications">
          <img :src="require('@/assets/Icons/notification.png')" alt="Notification Icon" class="icon"/>
          <span v-if="unreadNotificationsCount > 0" class="notification-badge">{{ unreadNotificationsCount }}</span>
        </div>
      <img :src="require('@/assets/Icons/settings.png')" alt="Settings Icon" class="icon"/>
      <img :src="require('@/assets/Icons/logout.png')" alt="Logout Icon" class="icon" @click="logout"/>
    </div>
  </header>


  <div class="profile-container">
    <div class="profile-header">
      <img :src="profileImage" alt="Profile Picture" class="profile-picture"/>
      <h5 class="title">Hello, {{ form.first_name }} {{ form.last_name }}!</h5>
    </div>
    <form @submit.prevent="updateProfile">
      <div class="mt-3 form-field">
        <label for="username" class="form-label text-start">Username</label>
        <input type="text" id="username" v-model="form.username" readonly />
      </div>

      <div class="row mt-3">
        <div class="col-md-6 form-field">
          <label for="first_name" class="form-label text-start">First Name</label>
          <input type="text" id="first_name" v-model="form.first_name" />
        </div>
        <div class="col-md-6 form-field">
          <label for="last_name" class="form-label text-start">Last Name</label>
          <input type="text" id="last_name" v-model="form.last_name" />
        </div>
      </div>

      <div class="mt-3 form-field">
        <label for="email" class="form-label text-start">Email</label>
        <input type="email" id="email" v-model="form.email" />
      </div>
      <div class="mt-3 form-field">
        <label for="profile_picture" class="form-label text-start">Profile Picture</label>
        <input type="file" id="profile_picture" @change="onFileChange" />
      </div>
      <button type="submit" class="btn btn-color mt-3">Update Profile</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'UserProfile',
  data() {
    return {
      form: {
        username: '',
        first_name: '',
        last_name: '',
        email: '',
        profile_picture: null,
      },
      profileImage: require('@/assets/Icons/person.png'), 
      showDropdown: false,
      notifications: [],
      unreadNotificationsCount: 0,
    };
  },
  methods: {
    async updateProfile() {
      const formData = new FormData();
      formData.append('username', this.form.username);
      formData.append('first_name', this.form.first_name);
      formData.append('last_name', this.form.last_name);
      formData.append('email', this.form.email);
      if (this.form.profile_picture) {
        formData.append('profile_picture', this.form.profile_picture);
      }

      try {
        const token = localStorage.getItem('token');
        const response = await axios.put('http://localhost:5000/profile', formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
            'Authorization': `Bearer ${token}`,
          },
        });
        if (response.status === 200) {
          alert('Profile updated successfully!');
        } else {
          alert('Failed to update profile.');
        }
      } catch (error) {
        alert(`Error updating profile: ${error}`);
      }
    },
    onFileChange() {
      const file = this.$refs.profile_picture.files[0];
      this.form.profile_picture = file;
      this.profileImage = URL.createObjectURL(file); 
    },
    async loadUserProfile() {
      try {
        const token = localStorage.getItem('token');
        const response = await axios.get('http://localhost:5000/profile', {
          headers: {
            'Authorization': `Bearer ${token}`,
          },
        });
        if (response.status === 200) {
          const userProfile = response.data;
          this.form.username = userProfile.Username;
          this.form.first_name = userProfile.Name;
          this.form.last_name = userProfile.Surname;
          this.form.email = userProfile.Email;
          if (userProfile.Profile_Picture) {
            this.profileImage = `http://localhost:5000${userProfile.Profile_Picture}`;
          }
        } else {
          console.log('Failed to load user profile');
          alert('Failed to load user profile.');
        }
      } catch (error) {
        console.log(`Error loading profile: ${error}`);
        alert(`Error loading profile: ${error}`);
      }
    },
    showNotifications() {
      this.showDropdown = !this.showDropdown;
      if (this.showDropdown) {
        this.fetchNotifications();
      }
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
    },
    logout() {
      localStorage.removeItem('token');
      this.$router.push('/');
    },
    backToIndex() {
      this.$router.push('/index');
    },
  },
  mounted() {
    this.loadUserProfile();
  },
};
</script>

<style scoped>
.title {
  font-size: 300%;
  font-family: 'Impact', sans-serif;
  margin: 10px;
  color: rgb(5, 43, 66);
}

.btn-color{
  background-color: #0e1c36;
  color: #fff; 
}

.btn-color:hover{
  background-color: #12997e;
  color: #fff; 
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


.profile-container {
  max-width: 600px;
  margin: auto;
  padding: 20px;
  background-color: #f5f5f5;
  border-radius: 10px;
  position: relative;
  text-align: center;
}

.profile-header {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 20px;
}

.profile-picture {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  margin-bottom: 10px;
  color: #000;
}

.header-icons .icon {
  width: 24px;
  height: 24px;
  margin: 0 10px;
  cursor: pointer;
}

.header-icons {
  position: absolute;
  top: 20px;
  right: 20px;
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

h1 {
  font-size: 24px;
  margin-bottom: 20px;
}

.form-field {
  color: black;
}

label {
  display: block;
  font-weight: bold;
}

input, select {
  width: 100%;
  padding: 10px;
  border-radius: 5px;
  border: 1px solid #ccc;
}

.button {
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  background-color: #1abc9c;
  color: white;
  cursor: pointer;
  width: 100%;
  margin-top: 10px;
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
</style>

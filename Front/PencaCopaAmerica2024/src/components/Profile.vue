<template>
  <div class="profile-container">
    <button @click="backToIndex" class="back-button">
      <img :src="require('@/assets/Icons/backarrow.png')" alt="Back to Index" />
    </button>
    <div class="profile-header">
      <img :src="profileImage" alt="Profile Picture" class="profile-picture"/>
      <h1>Hello, {{ form.first_name }} {{ form.last_name }}!</h1>
    </div>
    <form @submit.prevent="updateProfile">
      <div class="form-field">
        <label for="username">Username</label>
        <input type="text" id="username" v-model="form.username" readonly />
      </div>
      <div class="form-field">
        <label for="first_name">First Name</label>
        <input type="text" id="first_name" v-model="form.first_name" />
      </div>
      <div class="form-field">
        <label for="last_name">Last Name</label>
        <input type="text" id="last_name" v-model="form.last_name" />
      </div>
      <div class="form-field">
        <label for="email">Email</label>
        <input type="email" id="email" v-model="form.email" />
      </div>
      <div class="form-field">
        <label for="profile_picture">Profile Picture</label>
        <input type="file" id="profile_picture" @change="onFileChange" />
      </div>
      <button type="submit" class="button">Update Profile</button>
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
      profileImage: require('@/assets/Icons/person.png'), // Default profile image URL
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
    onFileChange(event) {
      const file = event.target.files[0];
      this.form.profile_picture = file;
      this.profileImage = URL.createObjectURL(file); // Update profile image preview
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
            this.profileImage = `http://localhost:5000/${userProfile.Profile_Picture}`; 
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
}

h1 {
  font-size: 24px;
  margin-bottom: 20px;
}

.form-field {
  margin-bottom: 15px;
  text-align: left;
}

label {
  display: block;
  margin-bottom: 5px;
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

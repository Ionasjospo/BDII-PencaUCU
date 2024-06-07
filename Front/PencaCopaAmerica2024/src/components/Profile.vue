<template>
    <div class="profile-container">
      <button @click="backToIndex" class="button back-button">Back to Index</button>
      <h1>Profile Settings</h1>
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
            this.form = response.data;
          } else {
            alert('Failed to load user profile.');
          }
        } catch (error) {
          alert(`Error loading profile: ${error}`);
        }
      },
      backToIndex() {
        this.$router.push('/index');
      }
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
  }
  
  .form-field {
    margin-bottom: 15px;
  }
  
  label {
    display: block;
    margin-bottom: 5px;
    font-weight: bold;
  }
  
  input {
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
    padding: 5px 10px;
    background-color: #34495e;
    font-size: 12px;
    width: auto;
  }
  </style>
  
<template>
  <div class="login-container">
    <img :src="logo" alt="UCU Logo" class="logo" />

    <div class="login-frame">
      <h1>Welcome to the penca of the copa america 2024</h1>

      <div class="login-fields">
        <div class="field">
          <img :src="usernameIcon" alt="Username Icon" class="icon" />
          <input type="text" v-model="username" placeholder="Username" />
        </div>

        <div class="field">
          <img :src="passwordIcon" alt="Password Icon" class="icon" />
          <input type="password" v-model="password" placeholder="Password" />
        </div>

        <button @click="login">Login</button>

        <p class="register-link" @click="switchToRegister">Don't have an account? Register</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import logo from '@/assets/ucu_white_logo.png'
import usernameIcon from '@/assets/Icons/username.png'
import passwordIcon from '@/assets/Icons/password.png'

export default {
  name: 'LoginComponent',
  data() {
    return {
      username: '', 
      password: '',
      logo,
      usernameIcon,
      passwordIcon
    }
  },
  methods: {
    switchToRegister() {
      this.$router.push('/register')
    },
    switchToIndex() {
      this.$router.push('/index')
    },
    switchToAdminIndex() {
      this.$router.push('/adminIndex')
    },
    async login() {
      if (!this.username || !this.password) {
        alert('Please enter both username and password')
        return
      }

      try {
        const response = await axios.post('http://localhost:5000/login', {
          Username: this.username,
          Password: this.password
        })

        if (response.status === 200) {
          const token = response.data.token
          localStorage.setItem('token', token)
          if (this.username === 'admin') {
            this.switchToAdminIndex()
          } else {
            this.switchToIndex()
          }
        } else if (response.status === 400) {
          alert('Login Failed: Missing username or password')
        } else if (response.status === 401 || response.status === 404) {
          alert('Login Failed: Invalid username or password')
        } else {
          alert(`Login failed: ${response.data.error || 'Unknown error'}`)
        }
      } catch (error) {
        alert(`Failed to login: ${error}`)
      }
    }
  }
}
</script>

<style scoped>
.login-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  background-color: #2c3e50;
  color: white;
}

.logo {
  width: 250px;
  height: 150px;
  margin-bottom: 20px;
}

.login-frame {
  background-color: #34495e;
  padding: 20px;
  border-radius: 10px;
}

.login-fields {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.field {
  display: flex;
  align-items: center;
  margin-bottom: 10px;
}

.icon {
  width: 20px;
  height: 20px;
  margin-right: 10px;
}

input {
  padding: 10px;
  border-radius: 5px;
  border: none;
  width: 300px;
}

button {
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  background-color: #1abc9c;
  color: white;
  cursor: pointer;
}

.register-link {
  margin-top: 10px;
  cursor: pointer;
  color: #1abc9c;
}
</style>

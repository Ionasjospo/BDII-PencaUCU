<template>
  <div class="container">
    <div class="row">
      <div class="col-md-6 offset-md-3">
        <div class="card my-5">

          <form class="card-body cardbody-color" @submit.prevent="login">
            <div class="text-center">
              <img src="../assets/copa_america_logo.png" class="img-fluid profile-image-pic img-thumbnail rounded-circle my-3"
                width="200px" alt="profile">
              <h5 class="title">LOGIN</h5>
            </div>
            
            

            <div class="mb-3 d-flex justify-content-center align-items-center">
              <input type="text" class="form-control" id="Username" aria-describedby="emailHelp"
              v-model="username" placeholder="Username">
            </div>
            <div class="mb-3 d-flex justify-content-center align-items-center">
              <input type="password" class="form-control" id="password" 
              v-model="password" placeholder="Password">
            </div>

            <div class="text-center">
              <button type="submit" class="btn btn-color mb-2 w-25">Login</button></div>
            
            <div id="emailHelp" class="form-text text-center mb-5 text-dark">Not
              Registered? <a href="#" @click="switchToRegister" class="text-dark fw-bold"> Create an
                Account</a>
            </div>
          </form>
        </div>

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

.profile-image-pic{
  height: 200px;
  width: 200px;
  object-fit: cover;
}



.cardbody-color{
  background-color: #f8f9fa;
}

a{
  text-decoration: none;
}

.login-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  color: white;
}

.logo {
  width: 250px;
  height: 150px;
  margin-bottom: 20px;
}

.login-frame {
  background-color: #4F6F52;
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

<template>
  <div>
    <header>
      <img :src="logo" alt="UCU Logo" class="logo" />
      <h1>Register to Penca UCU</h1>
    </header>
    <main class="main-frame">
      <div class="register-frame">
        <h2>Register to Penca UCU</h2>
        <form @submit.prevent="register">
          <div class="form-field" v-for="(field, index) in formFields" :key="index">
            <label :for="field.id">{{ field.label }}</label>
            <input
              v-if="field.type !== 'combo'"
              :type="field.type"
              :id="field.id"
              v-model="form[field.model]"
              :placeholder="field.label"
            />
            <select v-if="field.type === 'combo'" :id="field.id" v-model="form[field.model]">
              <option v-for="option in field.options" :key="option" :value="option">{{ option }}</option>
            </select>
          </div>
          <button type="submit" class="button">Register</button>
        </form>
        <p class="login-link" @click="switchToLogin">Already have an account? Login</p>
      </div>
    </main>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'RegisterPage',
  data() {
    return {
      logo: require('@/assets/ucu_white_logo.png'),
      form: {
        document: '',
        first_name: '',
        last_name: '',
        email: '',
        username: '',
        password: '',
        champion_prediction: '',
        second_prediction: ''
      },
      formFields: [
        { id: 'document', label: 'Document', type: 'text', model: 'document' },
        { id: 'first_name', label: 'First Name', type: 'text', model: 'first_name' },
        { id: 'last_name', label: 'Last Name', type: 'text', model: 'last_name' },
        { id: 'email', label: 'Email', type: 'email', model: 'email' },
        { id: 'username', label: 'Username', type: 'text', model: 'username' },
        { id: 'password', label: 'Password', type: 'password', model: 'password' },
        { id: 'champion_prediction', label: 'Champion Prediction', type: 'combo', model: 'champion_prediction', options: [] },
        { id: 'second_prediction', label: 'Second Prediction', type: 'combo', model: 'second_prediction', options: [] }
      ]
    }
  },
  methods: {
    async loadCountries() {
      try {
        const response = await axios.get('http://localhost:5000/countries')
        if (response.status === 200) {
          const countries = response.data
          this.formFields.find(f => f.model === 'champion_prediction').options = Object.keys(countries)
          this.formFields.find(f => f.model === 'second_prediction').options = Object.keys(countries)
        } else {
          alert('Failed to load countries')
        }
      } catch (error) {
        alert(`Failed to load countries: ${error}`)
      }
    },
    validateEmail(email) {
      const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
      return re.test(email)
    },
    async register() {
      const {
        document,
        username,
        first_name,
        last_name,
        email,
        password,
        champion_prediction,
        second_prediction
      } = this.form

      if (!document || !username || !first_name || !last_name || !email || !password || !champion_prediction || !second_prediction) {
        alert('Please fill in all fields')
        return
      }

      if (!this.validateEmail(email)) {
        alert('Invalid email format')
        return
      }

      try {
        const response = await axios.post('http://localhost:5000/register', {
          Document: document,
          Username: username,
          Name: first_name,
          Surname: last_name,
          Email: email,
          Password: password,
          Champion_Prediction: champion_prediction,
          Second_Prediction: second_prediction
        })
        if (response.status === 200) {
          alert('User registered successfully!')
          if (username === 'admin') {
            this.$router.push('/admin')
          } else {
            this.$router.push({ path: '/index', query: { username } })
          }
        } else {
          alert(`Failed to register: ${response.data.error || 'Unknown error'}`)
        }
      } catch (error) {
        alert(`Failed to register: ${error}`)
      }
    },
    switchToLogin() {
      this.$router.push('/')
    }
  },
  mounted() {
    this.loadCountries()
  }
}
</script>

<style scoped>
.logo {
  width: 250px;
  height: 150px;
  margin: 10px auto;
}

h1, h2 {
  text-align: center;
}

.main-frame {
  padding: 20px;
  display: flex;
  justify-content: center;
}

.register-frame {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
  max-width: 600px;
  padding: 20px;
  background-color: #f5f5f5;
  border-radius: 10px;
}

.form-field {
  display: flex;
  flex-direction: column;
  margin-bottom: 15px;
  width: 100%;
}

label {
  margin-bottom: 5px;
  font-weight: bold;
}

input, select {
  padding: 10px;
  border-radius: 5px;
  border: 1px solid #ccc;
  width: 100%;
}

.button {
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  background-color: #1abc9c;
  color: white;
  cursor: pointer;
  margin-top: 20px;
  width: 100%;
}

.login-link {
  margin-top: 10px;
  cursor: pointer;
  color: #1abc9c;
}
</style>

<template>
  <div class="container">
    <main class="d-flex justify-content-center">
      <div class="card p-4 w-100" style="max-width: 600px;">
        <div class="text-center">
              <img src="../assets/copa_america_logo.png" class="img-fluid profile-image-pic img-thumbnail rounded-circle my-3"
                width="200px" alt="profile">
                <h5 class="title">REGISTER</h5>
          </div>
        <form @submit.prevent="register">
          <div class="row">
            <div class="col-md-6 mb-3">
              <label for="first_name" class="form-label d-flex align-items-start">First Name</label>
              <input
                type="text"
                id="firstName"
                v-model="form.first_name"
                placeholder="Atilio"
                class="form-control"
              />
            </div>
            <div class="col-md-6 mb-3">
              <label for="last_name" class="form-label d-flex align-items-start">Last Name</label>
              <input
                type="text"
                id="lastName"
                v-model="form.last_name"
                placeholder="Garcia"
                class="form-control"
              />
            </div>
          </div>

          <div class="row">
            <div class="col-md-6 mb-3">
              <label for="username" class="form-label d-flex align-items-start ">Username</label>
              <input
                type="text"
                id="username"
                v-model="form.username"
                placeholder="atilio1899"
                class="form-control"
              />
            </div>

            <div class="col-md-6 mb-3">
              <label for="document" class="form-label d-flex align-items-start">Document</label>
              <input
                type="text"
                id="document"
                v-model="form.document"
                placeholder="1405189-9"
                class="form-control"
              />
            </div>            
          </div>

          <div class="row">
            <div class="col-md-6 mb-3">
              <label for="password1" class="form-label d-flex align-items-start">Password</label>
              <input
                type="password"
                id="password2"
                v-model="form.password1"
                placeholder=""
                class="form-control"
              />
            </div>

            <div class="col-md-6 mb-3">
              <label for="password2" class="form-label d-flex align-items-start">Repit your password</label>
              <input
                type="password"
                id="password2"
                v-model="form.password2"
                placeholder="Password"
                class="form-control"
              />
            </div>
          </div>

          
          <div class="mb-3">
            <label for="email" class="form-label d-flex align-items-start">Email</label>
            <input
              type="email"
              id="email"
              v-model="form.email"
              placeholder="atiliogarcia@gmail.com"
              class="form-control"
            />
          </div>
          
          
          
          <div class="mb-3">
            <label for="country" class="form-label d-flex align-items-start">Predict champion</label>
            <select id="champion_prediction" v-model="form.champion_prediction" class="form-select">
              <option value="" disabled>Select your country</option>
              <option v-for="country in countries" :key="country" :value="country">{{ country }}</option>
            </select>
          </div>

          <div class="mb-3">
            <label for="country" class="form-label d-flex align-items-start">Predict second place</label>
            <select id="second_prediction" v-model="form.second_prediction" class="form-select">
              <option value="" disabled>Select your country</option>
              <option v-for="country in countries" :key="country" :value="country">{{ country }}</option>
            </select>
          </div>

          <button type="submit" class="btn btn-color w-25">Register</button>
          <p v-if="errorMessage" class="text-danger mb-2">{{ errorMessage }}</p>
        </form>
        <p class="text-center mt-3">
          Already have an account?
          <a href="#" @click.prevent="switchToLogin" class="already-account">Login</a>
        </p>
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
      form: {
        document: '',
        first_name: '',
        last_name: '',
        email: '',
        username: '',
        password1: '',
        password2: '',
        champion_prediction: '',
        second_prediction: ''
      },
      errorMessage: '',
      countries: [
      ],
      
    }
  },
  methods: {
    async loadCountries() {
      try {
        const response = await axios.get('http://localhost:5000/countries')
        if (response.status === 200) {
          const countries_dict = response.data
          this.countries = Object.keys(countries_dict)
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
    validateDocument(document) {
      const re = /^\d{7}-\d$/;
      return re.test(document);
    },
    async register() {
      const {
        document,
        username,
        first_name,
        last_name,
        email,
        password1,
        password2,
        champion_prediction,
        second_prediction
      } = this.form;

      if (!document || !username || !first_name || !last_name || !email || !password1 || !password2 || !champion_prediction || !second_prediction) {
        this.errorMessage = 'Please fill in all fields';
        return;
      }

      if (champion_prediction === second_prediction) {
        this.errorMessage = 'Champion and runner up must not be the same';
        return;
      }

      if (!this.validateEmail(email)) {
        this.errorMessage = 'Invalid email format';
        return;
      }

      if (!this.validateDocument(document)) {
        this.errorMessage = 'Invalid document format. It must be like 1405189-9';
        return;
      }

      if (password1 !== password2) {
        this.errorMessage = 'Passwords do not match';
        return;
      }

      try {
        const validateResponse = await axios.get('http://localhost:5000/validate_register', {
          params: {
            username,
            document,
            email
          }
        });

        if (validateResponse.status !== 200) {
          this.errorMessage = `Validation failed: ${validateResponse.data.error}`;
          return;
        }

        const response = await axios.post('http://localhost:5000/register', {
          Document: document,
          Username: username,
          Name: first_name,
          Surname: last_name,
          Email: email,
          Password: password1,
          Champion_Prediction: champion_prediction,
          Second_Prediction: second_prediction
        });

        if (response.status === 200) {
          alert('User registered successfully!');
          if (username === 'admin') {
            this.$router.push({ path: '/adminIndex', query: { username } });
          } else {
            this.$router.push({ path: '/index', query: { username } });
          }
        } else {
          this.errorMessage = `Failed to register: ${response.data.error || 'Unknown error'}`;
        }
      } catch (error) {
        if (error.response) {
          if (error.response.status === 400) {
            this.errorMessage = 'Missing Username or Password';
          } else if (error.response.status === 401) {
            this.errorMessage = 'Invalid user or password';
          } else if (error.response.status === 404) {
            this.errorMessage = 'User not found';
          } else if (error.response.status === 409) {
            this.errorMessage = error.response.data.error;
          } else {
            this.errorMessage = `Failed to register: ${error.response.data.error || 'Unknown error'}`;
          }
        } else {
          this.errorMessage = `Failed to register: ${error.message}`;
        }
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
.title {
  font-size: 300%;
  font-family: 'Impact', sans-serif;
  margin: 10px;
  color: rgb(5, 43, 66);
}

.already-account{
  color: #0e1c36;
  font-weight: bold;
}

.btn-color{
  background-color: #0e1c36;
  color: #fff; 
}

.btn-color:hover{
  background-color: #12997e;
  color: #fff; 
}

.card{
  background-color: #f8f9fa;
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

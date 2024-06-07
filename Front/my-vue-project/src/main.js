import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import axios from 'axios';

axios.interceptors.request.use(
  config => {
    const token = localStorage.getItem('token');
    if (token) {
      config.headers['x-access-token'] = token;
    }
    return config;
  },
  error => {
    return Promise.reject(error);
  }
);

createApp(App).use(router).mount('#app');

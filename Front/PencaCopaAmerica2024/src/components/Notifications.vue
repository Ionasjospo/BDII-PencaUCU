<template>
  <div class="notifications">
    <img 
      :src="require('@/assets/Icons/notification.png')" 
      alt="Notification Icon" 
      class="icon" 
      @click="toggleDropdown"
    />
    <div v-if="unreadCount > 0" class="notification-count">{{ unreadCount }}</div>
    <div v-if="showDropdown" class="dropdown">
      <p v-if="notifications && notifications.length === 0">No notifications</p>
      <p v-else v-for="notification in notifications" :key="notification.id_notification">
        {{ notification.message }}
      </p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Notifications',
  data() {
    return {
      showDropdown: false,
      notifications: [],
      unreadCount: 0,
    };
  },
  methods: {
    async loadNotifications() {
      try {
        const token = localStorage.getItem('token');
        const response = await axios.get('http://localhost:5000/notifications', {
          headers: {
            'Authorization': `Bearer ${token}`
          }
        });
        if (response.status === 200) {
          this.notifications = response.data;
          if (!this.notifications || this.notifications.length === 0) {
            console.log('No notifications found');
          }
          this.unreadCount = this.notifications ? this.notifications.length : 0;
        } else {
          alert('Failed to load notifications.');
        }
      } catch (error) {
        alert(`Failed to load notifications: ${error}`);
      }
    },
    toggleDropdown() {
      this.showDropdown = !this.showDropdown;
    }
  },
  mounted() {
    this.loadNotifications();
  }
};
</script>

<style scoped>
.notifications {
  position: relative;
  display: inline-block;
}

.icon {
  width: 24px;
  height: 24px;
  cursor: pointer;
}

.notification-count {
  position: absolute;
  top: 0;
  right: 0;
  background-color: red;
  color: white;
  border-radius: 50%;
  width: 16px;
  height: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 12px;
}

.dropdown {
  position: absolute;
  top: 30px;
  right: 0;
  background-color: white;
  border: 1px solid #ccc;
  padding: 10px;
  width: 200px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  z-index: 1;
}
</style>

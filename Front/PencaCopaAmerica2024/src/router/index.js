import { createRouter, createWebHistory } from 'vue-router';
import LoginComponent from '../components/Login.vue';
import IndexPage from '../components/Index.vue';
import FixturePage from '../components/Fixture.vue';
import PredictPage from '../components/Predict.vue';
import RankingPage from '../components/Ranking.vue';
import RegisterPage from '../components/Register.vue';
import AdminResults from '../components/admin_results.vue';
import AdminIndex from '../components/admin_Index.vue';
import AdminFixture from '../components/admin_Fixture.vue';
import AdminRanking from '../components/admin_Ranking.vue';
import ProfilePage from '../components/Profile.vue';

const routes = [
  { path: '/', component: LoginComponent },
  { path: '/index', component: IndexPage, meta: { requiresAuth: true } },
  { path: '/fixture', component: FixturePage, meta: { requiresAuth: true } },
  { path: '/predict', component: PredictPage, meta: { requiresAuth: true } },
  { path: '/ranking', component: RankingPage, meta: { requiresAuth: true } },
  { path: '/register', component: RegisterPage },
  { path: '/adminResults', component: AdminResults, meta: { requiresAuth: true } },
  { path: '/adminIndex', component: AdminIndex, meta: { requiresAuth: true } },
  { path: '/adminFixture', component: AdminFixture, meta: { requiresAuth: true } },
  { path: '/adminRanking', component: AdminRanking, meta: { requiresAuth: true } },
  { path: '/profile', component: ProfilePage, meta: { requiresAuth: true } }
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    const token = localStorage.getItem('token')
    if (!token) {
      next('/')
    } else {
      next()
    }
  } else {
    next()
  }
});


export default router;

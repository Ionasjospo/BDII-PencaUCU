import { createRouter, createWebHistory } from 'vue-router';
import LoginComponent from '../components/Login.vue';
import IndexPage from '../components/Index.vue';
import FixturePage from '../components/Fixture.vue';
import PredictPage from '../components/Predict.vue';
import PredictStatsPage from '../components/Predict_Stats.vue';
import RankingPage from '../components/Ranking.vue';
import RegisterPage from '../components/Register.vue';
import AdminResults from '../components/AdminResults.vue';
import AdminIndex from '../components/AdminIndex.vue';
import AdminFixture from '../components/AdminFixture.vue';
import AdminRanking from '../components/AdminRanking.vue';
import ProfilePage from '../components/Profile.vue';
import RulesPage from '../components/Rules.vue';
import Pricing from '../components/Pricing.vue';
import FAQs from '../components/FAQs.vue';
import UserPoint from '../components/UserPoints.vue';

const routes = [
  { path: '/', component: LoginComponent },
  { path: '/index', component: IndexPage, meta: { requiresAuth: true } },
  { path: '/fixture', component: FixturePage, meta: { requiresAuth: true } },
  { path: '/predict', component: PredictPage, meta: { requiresAuth: true } },
  { path: '/predictStats/:id', component: PredictStatsPage, meta: { requiresAuth: true } },
  { path: '/ranking', component: RankingPage, meta: { requiresAuth: true } },
  { path: '/register', component: RegisterPage },
  { path: '/adminResults', component: AdminResults, meta: { requiresAuth: true } },
  { path: '/adminIndex', component: AdminIndex, meta: { requiresAuth: true } },
  { path: '/adminFixture', component: AdminFixture, meta: { requiresAuth: true } },
  { path: '/adminRanking', component: AdminRanking, meta: { requiresAuth: true } },
  { path: '/profile', component: ProfilePage, meta: { requiresAuth: true } },
  { path: '/rules', component: RulesPage, meta: { requiresAuth: true } },
  { path: '/pricing', component: Pricing, meta: { requiresAuth: true } },
  { path: '/FAQs', component: FAQs, meta: { requiresAuth: true } },
  { path: '/userpoint', component: UserPoint, meta: { requiresAuth: true } }
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

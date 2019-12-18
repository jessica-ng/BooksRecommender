import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '../views/Home.vue';
import Onboarding1 from '../views/OnboardingStage1.vue';
import Onboarding2 from '../views/OnboardingStage2.vue';
import Onboarding3 from '../views/OnboardingStage3.vue';
import MyRecommendations from '../views/Recommendations.vue';
import Profile from '../views/Profile.vue';

import Test from '../components/test.vue';
import Login from '../components/Login/Login.vue';
import SignUp from '../components/SignUp/SignUp.vue';
import BookCard from '../components/BookCard/BookCard.vue';
import SubmitRatings from '../components/SubmitRatings/SubmitRatings.vue';
import ConfirmSignUp from '../components/ConfirmSignUp/ConfirmSignUp.vue';



Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home,
  },
  {
    path: '/about',
    name: 'Profile',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/Profile.vue'),
  },
  {
    path: '/test',
    name: 'test',
    component: Test,
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
  },
  {
    path: '/signup',
    name: 'SignUp',
    component: SignUp,
  },
  {
    path: '/books',
    name: 'BookCard',
    component: BookCard,
  },
  {
    path: '/submitRatings',
    name: 'SubmitRatings',
    component: SubmitRatings,
  },
  {
    path: '/onboarding1',
    name: 'Onboarding1',
    component: Onboarding1,
  },
  {
    path: '/onboarding2',
    name: 'Onboarding2',
    component: Onboarding2,
  },
  {
    path: '/onboarding3',
    name: 'Onboarding3',
    component: Onboarding3,
  },
  {
    path: '/confirm_signup',
    name: 'ConfirmSignUp',
    component: ConfirmSignUp,
  },
  {
    path: '/recommendations',
    name: 'MyRecommendations',
    component: MyRecommendations,
  },
  {
    path: '/profile',
    name: 'Profile',
    component: Profile,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;

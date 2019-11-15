import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '../views/Home.vue';
import Test from '../components/test.vue';
import Login from '../components/Login/Login.vue';
import SignUp from '../components/SignUp/SignUp.vue';
import BookCard from '../components/BookCard/BookCard.vue';
import SubmitRatings from '../components/SubmitRatings/SubmitRatings.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home,
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue'),
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
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;

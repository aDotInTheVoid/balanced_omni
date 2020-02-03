import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '../views/Home.vue';

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
    path: '/login',
    name: 'Log in',
    component: () => import(/* webpackChunkName: "login" */'@/views/auth/Login.vue'),
  },
  {
    path: '/tasks',
    name: 'Tasks',
    component: () => import(/* webpackChunkName: "tasks" */'@/views/TaskList.vue'),
  },
  {
    path: '/tasks/:id',
    name: 'Task',
    component: () => import(/* webpackChunkName: "task" */'@/views/TaskDetail.vue'),
  },

  {
    path: '/create',
    name: 'Create Task',
    component: () => import(/* webpackChunkName: "notfound" */'@/components/tasks/CreateTask.vue'),
  },
  {
    path: '*',
    name: 'Not Found',
    component: () => import(/* webpackChunkName: "notfound" */'@/views/NotFound.vue'),
  },
];

const router = new VueRouter({
  mode: (process.env.CI == 'true' ? 'hash' : 'history'),
  base: process.env.BASE_URL,
  routes,
});

export default router;

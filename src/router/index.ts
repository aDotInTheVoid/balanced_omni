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
    component: () => import(/* webpackChunkName: "create" */'@/components/tasks/CreateTask.vue'),
  },
  {
    path: '/m2',
    name: 'Matrix Test',
    component: () => import(/* webpackChunkName: "matrix" */'@/components/tasks/TaskMatrix.vue'),
  },
  {
    path: '*',
    name: 'Not Found',
    component: () => import(/* webpackChunkName: "notfound" */'@/views/NotFound.vue'),
  },
];


const router = new VueRouter({
  base: process.env.BASE_URL,
  routes,
});

export default router;

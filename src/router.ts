import Vue from 'vue';
import VueRouter from 'vue-router';

Vue.use(VueRouter);

const routes = [
  {
    path: '/',
    name: 'home',
    component: () => import(/* webpackChunkName: "home" */'@/views/Home.vue'),
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
    component: () => import(/* webpackChunkName: "create" */'@/views/CreateTask.vue'),
  },
  {
    path: '/matrix',
    name: 'Task Matrix',
    component: () => import(/* webpackChunkName: "matrix" */'@/views/TaskMatrix.vue'),
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

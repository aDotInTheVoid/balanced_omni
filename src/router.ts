import Vue from 'vue';
import VueRouter, { Route } from 'vue-router';
// import { getToken } from '@/api/jwt';

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
    meta: { guestOnly: true },
    props: (route: Route) => ({
      to: route.query.to || '/',
    }),
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

// TODO: make this a call to the API service
const isAuthenticated = true;

// Beware, it's super easy to make this recurse infinitely.
// Make sure each path through the code calls `next` exactly once.
// Also make sure you eventually resolve to a call to `next()` with
// no arguments.
router.beforeEach((to, from, next) => {
  // Accessing a guestOnly (eg login)
  if (to.matched.some(x => x.meta.guestOnly)) {
    // If they have auth, go home
    if (isAuthenticated) {
      next('/');
      return;
    }
  } else {
    // Otherwise we require login
    if (!isAuthenticated) {
      const loginPath = encodeURIComponent(to.fullPath);
      next(`/login?to=${loginPath}`);
      return;
    }
  }
  // By default, just continue
  next();
});


export default router;

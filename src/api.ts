import Vue from 'vue';
import axios from 'axios';
import VueAxios from 'vue-axios';
import JwtService from '@/store/auth/jwt';

const API_URL = 'http://127.0.0.1:8000/api';

const ApiService = {
  init() {
    Vue.use(VueAxios, axios);
    Vue.axios.defaults.baseURL = API_URL;
    Vue.axios.defaults.headers.common['Content-Type'] = 'Content-Type';
  },

  setHeader() {
    Vue.axios.defaults.headers.common.Authorization = `Token ${JwtService.getToken()}`;
  },

  query(resource: any, params: any) {
    return Vue.axios.get(resource, params).catch((error) => {
      throw new Error(`[RWV] ApiService ${error}`);
    });
  },

  get(resource: string, slug = '') {
    return Vue.axios.get(`${resource}/${slug}`).catch((error) => {
      throw new Error(`[RWV] ApiService ${error}`);
    });
  },

  post(resource: string, params: any) {
    return Vue.axios.post(`${resource}`, params);
  },

  update(resource: String, slug: String, params: any) {
    return Vue.axios.put(`${resource}/${slug}`, params);
  },

  put(resource: string, params: any) {
    return Vue.axios.put(`${resource}`, params);
  },

  delete(resource: string) {
    return Vue.axios.delete(resource).catch((error) => {
      throw new Error(`[RWV] ApiService ${error}`);
    });
  },
};

ApiService.init();

export default ApiService;

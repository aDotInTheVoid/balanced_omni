

import { AuthState, LoginCredentials, User } from './types';
import { JWTService } from '../../api/jwt';
import APIService from '@/api/api';



(context: AuthContext, cred: LoginCredentials) {
    return new Promise((resolve) => {
      APIService.post('users/login', { user: cred })
        .then(({ data }) => {
          context.commit(ids.AUTH_SET_USER, data.user);
          resolve(data);
        })
        .catch((x) => {
          console.log(x);
          // commitSetErrors(context, response.data.errors);
        });
    });
  },
  [ids.AUTH_INIT](context: AuthContext) {
    if (JWTService.getToken()) {
      APIService.setHeader();
      APIService.get('user').then(
        ({ data }) => {
          context.commit(ids.AUTH_SET_USER, data.user);
          JWTService.saveToken(data.user.token);
        },
      ).catch(({ responce }) => {
        context.commit(ids.AUTH_SET_ERROR, responce.data.errors);
      });
    } else {
      // purge the auth
      context.commit(ids.AUTH_PURGE);
    }
  },
};
const mutations = {
  [ids.AUTH_PURGE](state: AuthState) {
    state.isLogedIn = false;
    state.user = null;
    JWTService.destroyToken();
  },
  [ids.AUTH_SET_USER](state: AuthState, user: User) {
    state.user = user;
    state.isLogedIn = true;
    state.errors = {};
    JWTService.saveToken(user.token);
  },
  [ids.AUTH_SET_ERROR](state: AuthState, errors: any) {
    state.errors = errors;
  },
};

const auth: Module<AuthState, RootState> = {
  // namespaced: true,
  actions,
  mutations,
};

export default auth;

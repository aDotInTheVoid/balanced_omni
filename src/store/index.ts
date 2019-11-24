import Vue from 'vue';
import Vuex from 'vuex';

import auth from './auth';

/*
                     _____________
                    /             \
                    | Backend API |
                    \_____________/
                           /\
                           ||                      VUEX
                   ++++++++++++++++++++++++++++++++++++
                   +       ||                         +
                   +   ____\/___                      +
          Dispatch +  /         \ Commit              +
        /----------+->| Actions |-----------\         +
 _______|________  +  \_________/           |         +
/                \ +                    ____v______   +   __________
| Vue Components | +                   /           \  +  /          \
\_______________/  +                   | Mutations |<-+->| Devtools |
         /\        +     _______       \___________/  +  \__________/
         ||        +    /       \          |          +
         \\--------+----| State |<---------/          +
            Render +    \_______/  Mutate             +
                   +                                  +
                   ++++++++++++++++++++++++++++++++++++
*/

// https://codeburst.io/vuex-and-typescript-3427ba78cfa8


Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    auth,
  },
});

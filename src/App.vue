<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      dark
    >
      <div class="d-flex align-center">
        <router-link
          to="/"
        >
          <v-img
            alt="Vuetify Logo"
            class="shrink mr-2"
            contain
            src="https://cdn.vuetifyjs.com/images/logos/vuetify-logo-dark.png"
            transition="scale-transition"
            width="40"
          />
        </router-link>
      </div>
      <v-toolbar-title v-text="title" />
      <v-spacer />


      <v-btn
        icon
        x-large
        to="/tasks"
      >
        <v-icon>mdi-view-list</v-icon>
      </v-btn>
      <v-btn
        icon
        x-large
      >
        <v-icon>mdi-plus-box</v-icon>
      </v-btn>
    </v-app-bar>

    <v-content>
      <v-layout
        v-if="loading"
        row
        justify-center
        align-center
        fill-height
      >
        <v-progress-circular
          size="128"
          indeterminate
        />
      </v-layout>
      <router-view v-else />
    </v-content>
  </v-app>
</template>

<script lang="ts">
import Vue from 'vue';
import HelloWorld from './components/HelloWorld.vue';

export default Vue.extend({
  name: 'App',


  data() {
    return { loading: false };
  },
  computed: {
    title() {
      return this.$route.name;
    },
  },
  created() {
    this.$router.beforeEach((to, from, next) => {
      this.loading = true;
      next();
    });
    this.$router.afterEach((to, from) => {
      this.loading = false;
    });
  },

});
</script>

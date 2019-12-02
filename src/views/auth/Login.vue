<template>
  <v-layout
    row
    justify-center
    mt-3
  >
    <v-flex
      xs11
      sm8
      md6
    >
      <v-card>
        <v-card-actions class="primary white--text">
          <v-spacer />
          <div class="headline mb-0">
            Sign in
          </div>
          <v-spacer />
        </v-card-actions>
        <v-card-text>
          <v-form v-model="valid">
            <v-text-field
              v-model="email"
              :rules="emailRules"
              label="Email"
              required
              class="my-2"
            />
            <v-text-field
              v-model="password"
              type="password"
              :rules="passwordRules"
              label="Password"
              required
              class="my-2"
            />
            <v-btn
              :disabled="!valid"
              class="primary ml-0"
              @click="submit"
            >
              Sign in
            </v-btn>

            <v-alert
              v-if="errors"
              :value="errors"
              type="error"
              class="my-2"
            >
              {{ errors }}
            </v-alert>
          </v-form>
        </v-card-text>
      </v-card>
    </v-flex>
  </v-layout>
</template>

<script>
import { dispatchLogin } from '@/store/auth';

export default {
  props: ['to'],
  data: () => ({
    errors: '',
    valid: false,
    email: '',
    password: '',
    emailRules: [
      v => !!v || 'Email is required',
      v => /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(v) || 'E-mail must be valid',
    ],
    passwordRules: [
      p => !!p || 'Password is required',
    ],
  }),
  methods: {
    submit() {
      // api.post('login', {
      //   username: this.email,
      //   password: this.password,
      // })
      //   .then(({ data }) => {
      //     auth.login(data.token, data.user, data.expiry);
      //     this.$router.push(this.to);
      //     this.errors = '';
      //   }).catch(({ response }) => {
      //     this.errors = response.data.message;
      //   });
      this.$store.dispatch('LOGIN', { email: this.email, password: this.password });
    },


  },
};
</script>

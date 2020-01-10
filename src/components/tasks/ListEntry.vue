<template>
  <v-card
    class="mx-auto my-1"
    max-width="344"
  >
    <v-list-item two-line>
      <v-list-item-content>
        <v-list-item-title>{{ title }} ({{ x }}, {{ y }})</v-list-item-title>
        <v-list-item-subtitle>
          {{ dueDate }}
          <br>
          {{ description }}
        </v-list-item-subtitle>
      </v-list-item-content>

      <v-list-item-avatar>
        <v-btn
          class="mx-2"
          icon
          color="black"
        >
          <v-icon dark>
            mdi-check
          </v-icon>
        </v-btn>
      </v-list-item-avatar>
    </v-list-item>
  </v-card>
</template>

<script lang="ts">
import Vue from 'vue';

const REQUIRED_STRING = {
  type: String,
  required: true,
};

const REQUIRED_NUMBER = {
  type: Number,
  required: true,
};

export default Vue.extend({
  props: {
    title: REQUIRED_STRING,
    dueDate: REQUIRED_STRING,
    description: REQUIRED_STRING,
    x: REQUIRED_NUMBER,
    y: REQUIRED_NUMBER,
  },
});
</script>

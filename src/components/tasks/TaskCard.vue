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
        <v-card-title>
          {{ task.title }}
        </v-card-title>
        <v-card-subtitle>
          Due {{ task.dueDate }}
        </v-card-subtitle>
        <v-card-text>
          <v-card outlined>
            <v-card-text>{{ task.description }}</v-card-text>
          </v-card><br>
          <b>Priority:</b> {{ task.x }} <br>
          <b>Importance:</b> {{ task.y }} <br>
          <b>Urgency:</b> {{ task.z }} <br>
          <b>Quadrant:</b> {{ task.q }}
        </v-card-text>
        <v-card-actions>
          <v-btn left>
            <v-icon>mdi-check</v-icon> Mark as done
          </v-btn>
          <v-btn left>
            <v-icon>mdi-delete</v-icon> Delete
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-flex>
  </v-layout>
</template>

<script lang="ts">
import Vue from 'vue';

type TASK = {
    id: Number,
    title: String,
    x: Number,
    y: Number,
    z: Number,
    q: String,
    description: String
    dueDate: String
}

export default Vue.extend({
  props: {
    task: {
      type: Object as () => TASK,
      required: true,
    },
  },
});
</script>

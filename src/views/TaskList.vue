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
            Tasks
          </div>
          <v-spacer />
        </v-card-actions>
        <v-card-text>
          <task-list />
        </v-card-text>
      </v-card>
    </v-flex>
  </v-layout>
</template>

<script lang="ts">
import Vue from 'vue';

import TaskList from '@/components/tasks/TaskList.vue';

export default Vue.extend({
  components: {
    TaskList,
  },
});
</script>

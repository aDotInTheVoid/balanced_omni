<template>
  <v-card>
    <h1>Task List</h1>
    <task-list />
  </v-card>
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

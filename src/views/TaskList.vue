<template>
  <task-list />
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

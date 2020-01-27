<template>
  <div>
    <ListEntry
      v-for="i in tasks"
      :key="i.id"
      :task="i"
      @clicked-done="removeTask"
    />
  </div>
</template>

<script lang="ts">
import Vue from 'vue';

import ListEntry from '@/components/tasks/ListEntry.vue';
import { Tasks } from '@/data/tasks';

export default Vue.extend({
  name: 'TaskList',
  components: {
    ListEntry,
  },
  data() {
    return {
      tasks: Tasks,
    };
  },
  methods: {
    removeTask(id: Number) {
      // TODO: Backend interaction
      // TODO: Animation
      const pos = this.tasks.indexOf(this.tasks.filter(x => x.id == id)[0]);
      this.tasks.splice(pos, 1);
    },
  },
});
</script>

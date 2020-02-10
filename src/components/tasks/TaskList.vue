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
import Vue, { VueConstructor } from 'vue';

import ListEntry from '@/components/tasks/ListEntry.vue';
import default_tasks, { Task } from '@/data/tasks';

interface TaskList extends Vue{
  tasks: Task[]
}

export default (Vue as VueConstructor<TaskList>).extend({
  name: 'TaskList',
  components: {
    ListEntry,
  },
  props: {
    tasks: {
      default: () => default_tasks,
    },
  },
  methods: {
    removeTask(id: Number) {
      // TODO: Backend interaction
      // TODO: Animation
      const pos = this.tasks.indexOf(this.tasks.filter(x => x.id === id)[0]);
      this.tasks.splice(pos, 1);
    },
  },
});
</script>

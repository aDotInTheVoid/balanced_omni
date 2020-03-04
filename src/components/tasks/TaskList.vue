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
import DefaultTasks, { Task } from '@/data/tasks';

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
      default: () => DefaultTasks,
    },
  },
  methods: {
    removeTask(id: Number) {
      // TODO: Backend interaction
      // TODO: Animation
      // Disabled for demo, as it messes things up
      // const pos = this.tasks.indexOf(this.tasks.filter(x => x.id === id)[0]);
      // this.tasks.splice(pos, 1);
    },
  },
});
</script>

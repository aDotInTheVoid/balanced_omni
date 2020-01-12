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

const TASK = {
  id: Number,
  title: String,
  x: Number,
  y: Number,
  dueDate: String,
};

export default Vue.extend({
  name: 'TaskList',
  components: {
    ListEntry,
  },
  data() {
    return {
      tasks: [
        {
          id: 1,
          title: 'Taskidy Task',
          x: 5,
          y: 5,
          dueDate: 'Jan 8',
        },
        {
          id: 2,
          title: 'Another Task',
          x: 2,
          y: 20,
          dueDate: 'Jan 92',
        },
        {
          id: 3,
          title: 'Another Task',
          x: 2,
          y: 20,
          dueDate: 'Jan 92',
        },
        {
          id: 4,
          title: 'Another Task',
          x: 2,
          y: 20,
          dueDate: 'Jan 92',
        },
        {
          id: 5,
          title: 'Another Task',
          x: 2,
          y: 20,
          dueDate: 'Jan 92',
        },
        {
          id: 6,
          title: 'Another Task',
          x: 2,
          y: 20,
          dueDate: 'Jan 92',
        },
        {
          id: 7,
          title: 'Another Task',
          x: 2,
          y: 20,
          dueDate: 'Jan 92',
        },
        {
          id: 8,
          title: 'Another Task',
          x: 2,
          y: 20,
          dueDate: 'Jan 92',
        },
        {
          id: 9,
          title: 'Another Task',
          x: 2,
          y: 20,
          dueDate: 'Jan 92',
        },
        {
          id: 10,
          title: 'Another Task',
          x: 2,
          y: 20,
          dueDate: 'Jan 92',
        },
      ],
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

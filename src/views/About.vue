<template>
  <div>
    <ListEntry
      v-for="task in tasks"
      :key="task.id"
      :title="task.title"
      :x="task.x"
      :y="task.y"
      :due-date="task.dueDate"
      :description="task.description"
    />
  </div>
</template>

<script lang="ts">
import Vue from 'vue';

import ListEntry from '@/components/tasks/ListEntry.vue';


export default Vue.extend({
  name: 'About',
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
          id: 2,
          title: 'Another Task',
          x: 2,
          y: 20,
          dueDate: 'Jan 92',
        },
        {
          id: 2,
          title: 'Another Task',
          x: 2,
          y: 20,
          dueDate: 'Jan 92',
        },
        {
          id: 2,
          title: 'Another Task',
          x: 2,
          y: 20,
          dueDate: 'Jan 92',
        },
        {
          id: 2,
          title: 'Another Task',
          x: 2,
          y: 20,
          dueDate: 'Jan 92',
        },
        {
          id: 2,
          title: 'Another Task',
          x: 2,
          y: 20,
          dueDate: 'Jan 92',
        },
        {
          id: 2,
          title: 'Another Task',
          x: 2,
          y: 20,
          dueDate: 'Jan 92',
        },
        {
          id: 2,
          title: 'Another Task',
          x: 2,
          y: 20,
          dueDate: 'Jan 92',
        },
        {
          id: 2,
          title: 'Another Task',
          x: 2,
          y: 20,
          dueDate: 'Jan 92',
        },
      ],
    };
  },
});
</script>

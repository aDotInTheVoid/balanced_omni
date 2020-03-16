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
import DefaultTasks, { Task, convert } from '@/data/tasks';

import api from '@/api/api';

interface TaskList extends Vue{
  tasks: Task[]
}

export default (Vue as VueConstructor<TaskList>).extend({
  name: 'TaskList',
  components: {
    ListEntry,
  },
  data() {
    return {
      tasks: [],
    };
  },
  mounted() {
    this.getTasks();
  },
  methods: {
    removeTask(id: Number) {
      api.patch(`/tasks/${id}/`, { is_done: true }).then(
        // TODO: Refresh other elements, like matrix
        () => this.getTasks(),
      ).catch(
        ({ response }) => console.log(response),
      );
    },
    getTasks() {
      api.get('tasks?done=false').then(
        ({ data }) => {
          this.tasks = data.map(convert);
        },
      ).catch(({ response }) => { console.log(response); });
    },
  },
});
</script>

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
      <task-card :task="task" />
    </v-flex>
  </v-layout>
</template>
<script lang="ts">
import Vue from 'vue';
import TaskCard from '@/components/tasks/TaskCard.vue';
import { convert } from '@/data/tasks';
import api from '@/api/api';


export default Vue.extend({
  components: {
    TaskCard,
  },
  data() {
    return {
      task: {},
    };
  },
  created() {
    const rid = this.$route.params.id; // Raw ID as string
    if (Number.isNaN(Number(rid))) { // If not number
      this.$router.push('/not_found');
    }
    const id = Number(rid);
    api.get(`/tasks/${id}/`).then(({ data }) => {
      this.task = convert(data);
    }).catch(({ response }) => {
      this.$router.push('/not_found');
    });
    // this.task = this.tasks.filter(x => x.id === id)[0];
  },
});
</script>

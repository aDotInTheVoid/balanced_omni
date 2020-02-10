<template>
  <Plotly
    :data="chartdata"
    :layout="layout"
    :display-mode-bar="false"
    :frames="[]"
  />
</template>

<script lang="ts">
import Vue, { VueConstructor } from 'vue';
import { Plotly } from 'vue-plotly';
import default_tasks, { Task } from '@/data/tasks';
import Tasks from '@/data/tasks';

interface TaskMatrix extends Vue{
  tasks: Task[]
}

export default (Vue as VueConstructor<TaskMatrix>).extend({
  components: {
    Plotly,
  },
  props: {
    tasks: {
      default: () => default_tasks,
    },
  },
  data() {
    return {

      layout: {
        xaxis: {
          type: 'linear',
          range: [
            -1,
            1,
          ],
          title: 'Importance',
          gridcolor: 'rgba(255, 255, 255, 0)',
          showticklabels: false,
        },
        yaxis: {
          type: 'linear',
          range: [
            -1.1, // So text above 1.0 can be on the chart
            1.1,
          ],
          title: 'Priority',
          gridcolor: 'rgba(255, 255, 255, 0)',
          showticklabels: false,
        },
        hovermode: false,
        dragmode: false,
        margin: {
          t: 0, autoexpand: false, l: 20, r: 0,
        },
      },
    };
  },
  computed: {
    chartdata() {
      return [{
        x: this.tasks.map(t => t.importance), // TODO: Fetch from prop
        y: this.tasks.map(t => t.importance),
        text: this.tasks.map(t => t.title),
        type: 'scatter',
        mode: 'markers+text',
        textposition: 'top',
      }];
    },
  },
});
</script>

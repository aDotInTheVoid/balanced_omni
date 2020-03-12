<template>
  <Plotly
    ref="plot"
    :data="chartdata"
    :layout="layout"
    :display-mode-bar="false"
    :frames="[]"
  />
</template>

<script lang="ts">
import Vue, { VueConstructor } from 'vue';
import { Plotly } from 'vue-plotly';
import DefaultTasks, { convert, Task } from '@/data/tasks';
import api from '@/api/api';

  interface TaskMatrix extends Vue {
    tasks: Task[],
    getTasks(): void,
  }

export default (Vue as VueConstructor<TaskMatrix>).extend({
  components: {
    Plotly,
  },
  data() {
    return {
      layout: {
        xaxis: {
          type: 'linear',
          range: [
            -5,
            5,
          ],
          title: 'Importance',
          gridcolor: 'rgba(255, 255, 255, 0)',
          showticklabels: false,
          fixedrange: true,
        },
        yaxis: {
          type: 'linear',
          range: [
            -5.1, // So text above 1.0 can be on the chart
            5.1,
          ],
          title: 'Priority',
          gridcolor: 'rgba(255, 255, 255, 0)',
          showticklabels: false,
          fixedrange: true,
        },
        hovermode: false,
        dragmode: false,
        clickmode: 'event',
        margin: {
          t: 0, autoexpand: false, l: 20, r: 0,
        },
      },
      tasks: [],
    };
  },
  computed: {
    chartdata() {
      return [{
        x: this.tasks.map(t => t.priority), // TODO: Fetch from prop
        y: this.tasks.map(t => t.importance),
        text: this.tasks.map(t => t.title),
        type: 'scatter',
        mode: 'markers+text',
        textposition: 'top',
        marker: {
          color: '#0d47a1',
        },
      }];
    },
  },
  mounted() {
    this.getTasks();
    (this.$refs.plot as any).update();
  },
  methods: {
    getTasks() {
      api.get('tasks?done=false').then(
        ({ data }) => {
          this.tasks = data.map(convert);
        },
      ).catch((responce) => {
        console.log(responce);
      });
    },
  },

});
</script>

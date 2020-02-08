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
      <v-card>
        <v-card-actions class="primary white--text">
          <v-spacer />
          <div class="headline mb-0">
            Task Matrix
          </div>
          <v-spacer />
        </v-card-actions>
        <v-card-text>
          <Plotly
            :data="data"
            :layout="layout"
            :display-mode-bar="false"
            :frames="[]"
          />
        </v-card-text>
      </v-card>
    </v-flex>
  </v-layout>
</template>

<script lang="ts">
import Vue from 'vue';
import { Plotly } from 'vue-plotly';


export default Vue.extend({
  components: {
    Plotly,
  },
  data() {
    return {
      data: [{
        x: [-0.2, 0.4, 0.3, -0.7], // TODO: Fetch from prop
        y: [0.7, 0.8, 0.4, -0.2],
        text: ['History Essay', 'Water Chickens', 'Watch "In the loop"', 'Research staplers'],
        type: 'scatter',
        mode: 'markers+text',
        textposition: 'top',
      }],
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
});
</script>

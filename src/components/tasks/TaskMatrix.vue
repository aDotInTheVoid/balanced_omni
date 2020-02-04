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
        <div>
          <apexchart
            type="scatter"
            :options="chartOptions"
            :series="series"
          />
        </div>
      </v-card>
    </v-flex>
  </v-layout>
</template>

<script lang="ts">
import Vue, { VueConstructor } from 'vue';
import { ApexOptions, ApexAxisChartSeries } from '@/plugins/apexcharts';

interface TaskMatrix extends Vue{
  random_point: () => [number, number],
  clickedTask(event: Event): void
}

export default (Vue as VueConstructor<TaskMatrix>).extend({
  data(): {chartOptions: ApexOptions, series: ApexAxisChartSeries} {
    return {
      chartOptions:  {
        chart: {
          zoom: {
            enabled: false,
          },
        },
        yaxis: {
          min: 0,
          max: 1,
          tickAmount: 10,
          decimalsInFloat: 1,
          title: {
            text: 'urgency',
          },
          labels: {
            formatter(val) {
              return val.toFixed(1);
            },
          },
        },
        xaxis: {
          min: 0,
          max: 1,
          tickAmount: 9,
          title: {
            text: 'importance',
          },
          labels: {
            formatter(val) {
              return parseFloat(val).toFixed(1);
            },
          },
        },
        markers: {
          onClick: this.clickedTask,
        },
        // The mouseover Stuff
        tooltip: {
          // Create the tooltip
          custom({
            series, seriesIndex, dataPointIndex, w,
          }: any) { // TODO: Type
          // TODO: Use Vue's styling
            return `${'<div class="arrow_box">'
      + '<span>'}${series[seriesIndex][dataPointIndex]}</span>`
      + '</div>';
          },
        },
      },
      series: [{
        name: '',
        // data: [[1, 1], [3, 3], [5, 5]],
        data: [this.random_point(), this.random_point(), this.random_point(), this.random_point(), this.random_point(), this.random_point()],
      }],
    };
  },
  methods: {
    random_point: () => [(Math.random() * 1), (Math.random() * 1)],
    clickedTask(event: Event) {
      // This is the index into the charts `series.data` that corestonds to the clicked point
      const index = (event as any).target.attributes.j.value; // TODO: make this not a hack
      console.log(this.series[0].data[index]);
    },
  },
});
</script>

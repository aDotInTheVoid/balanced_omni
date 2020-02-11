<template>
  <div
    id="chartmeup"
    style="width: 100%;"
  />
</template>
<script>
import Vue from 'vue';
import Plotly from 'plotly.js';

export default Vue.extend({
    props: {
        data: {
            required: true
        },
        layout: {
            required: true,
        }
    },
  mounted() {
    const myPlot = document.getElementById('chartmeup');


    
    Plotly.newPlot('chartmeup', this.data, this.layout, { displayModeBar: false, frames:[] });

        myPlot.on('plotly_click', function (data) {
            var pts = '';
            for (var i = 0; i < data.points.length; i++) {
                pts = 'x = ' + data.points[i].x + '\ny = ' +
                    data.points[i].y.toPrecision(4) + '\n\n';
            }
            alert('Closest point clicked:\n\n' + pts);
        });
  },
});
</script>

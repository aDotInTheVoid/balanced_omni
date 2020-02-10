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
        <!-- Top Line -->
        <v-card-actions class="primary white--text">
          <v-spacer />
          <div class="headline mb-0">
            Task Matrix
          </div>
          <v-spacer />
        </v-card-actions>
        <v-card-text><task-matrix /></v-card-text>
      </v-card>
    </v-flex>
  </v-layout>
</template>
<script lang="ts">
import Vue from 'vue';
import TaskMatrix from '@/components/tasks/TaskMatrix.vue';

export default Vue.extend({
  components: {
    TaskMatrix,
  },
});
</script>

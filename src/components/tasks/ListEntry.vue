<template>
  <v-card
    class="mx-auto my-1"
  >
    <v-list-item two-line>
      <v-list-item-content @click="pushLink">
        <v-list-item-title>
          {{ task.title }} ({{ task.importance }}, {{ task.urgency }})
        </v-list-item-title>
        <v-list-item-subtitle>
          {{ task.dueDate }}
          <br>
          {{ task.description }}
        </v-list-item-subtitle>
      </v-list-item-content>

      <v-list-item-avatar>
        <v-btn
          class="mx-2"
          icon
          color="black"
          @click="clickedDone"
        >
          <v-icon dark>
            mdi-check
          </v-icon>
        </v-btn>
      </v-list-item-avatar>
    </v-list-item>
  </v-card>
</template>

<script lang="ts">
import Vue from 'vue';
import { Task } from '@/data/tasks';


export default Vue.extend({
  props: {
    task: {
      type: Object as () => Task,
      required: true,
    },
  },
  computed: {
    link() {
      const { id } = this.$props.task;
      return `/tasks/${id}`;
    },
  },
  methods: {
    clickedDone() {
      this.$emit('clicked-done', this.$props.task.id);
    },
    pushLink() {
      // TODO use the ts wisardry from ./TaskMatrix
      // @ts-ignore Link is computed and TS can't handle the js introspection
      this.$router.push(this.link);
    },
  },
});
</script>

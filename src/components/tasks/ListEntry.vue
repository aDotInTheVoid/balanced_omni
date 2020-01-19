<template>
  <v-card
    class="mx-auto my-1"
    max-width="344"
  >
    <v-list-item two-line>
      <v-list-item-content @click="pushLink">
        <v-list-item-title>
          {{ task.title }} ({{ task.x }}, {{ task.y }})
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

const REQUIRED_STRING = {
  type: String,
  required: true,
};

const REQUIRED_NUMBER = {
  type: Number,
  required: true,
};

type TASK = {
    id: Number,
    title: String,
    x: Number,
    y: Number,
    dueDate: String
}

export default Vue.extend({
  props: {
    task: {
      type: Object as () => TASK,
      reqired: true,
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
      this.$router.push(this.link);
    },
  },
});
</script>

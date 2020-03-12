
<template>
  <!-- Preable -->
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
            Create Task
          </div>
          <v-spacer />
        </v-card-actions>
        <!-- Main Form -->
        <v-card-text>
          <v-form v-model="valid">
            <v-text-field
              v-model="title"
              :rules="required"
              required
              dense
              label="Title"
              counter="20"
            />
            <v-textarea
              v-model="description"
              :rules="required"
              required
              dense
              label="Description"
            />
            <v-slider
              v-model="priority"
              label="Priority"
              dense
              thumb-label
              min="-5"
              max="5"
            />
            <v-slider
              v-model="importance"
              label="Importance"
              thumb-label
              dense
              min="-5"
              max="5"
            />
            <!-- Date Picker -->
            <v-menu
              ref="startMenu"
              v-model="startMenu"
              :close-on-content-click="false"
              :nudge-right="40"
              :return-value.sync="date"
              transition="scale-transition"
              min-width="290px"
              offset-y
            >
              <template v-slot:activator="{ on }">
                <v-text-field
                  v-model="date"
                  class="mt-3 my-2"
                  label="Start Date"
                  prepend-icon="mdi-calendar"
                  dense
                  readonly
                  hide-details
                  v-on="on"
                />
              </template>
              <v-date-picker
                v-model="date"
                no-title
              >
                <v-spacer />
                <v-btn
                  text
                  color="primary"
                  @click="startMenu = false"
                >
                  Cancel
                </v-btn>
                <v-btn
                  text
                  color="primary"
                  @click="$refs.startMenu.save(start)"
                >
                  OK
                </v-btn>
              </v-date-picker>
            </v-menu>
            <v-btn
              class="primary ml-0"
              :disabled="!valid"
              @click="submit"
            >
              Create
            </v-btn>
          </v-form>
        </v-card-text>
      </v-card>
    </v-flex>
  </v-layout>
</template>
<script lang="ts">
import Vue from 'vue';
import api from '@/api/api';

export default Vue.extend({
  data() {
    return {
      startMenu: false,
      date: '2019-02-13', // TODO: Load todays date
      title: '',
      description: '',
      priority: 0,
      importance: 0,
      required: [
        (v: String) => !!v || 'Field is required',
      ],
      valid: false,
    };
  },
  methods: {
    submit() {
      const content = {
        name: this.title,
        due_date: this.date,
        description: this.description,
        priority: this.priority,
        importance: this.importance,
        is_done: false,
      };
      api.post('/tasks/', content).then((x) => {}).catch(({ response }) => console.log(response));
    },
  },
});
</script>

<style scoped>
.controls {
  position: relative;
}
</style>

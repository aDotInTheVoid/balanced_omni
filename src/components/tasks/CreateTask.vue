
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
          <v-form>
            <v-text-field
              required
              dense
              label="Title"
              counter="20"
            />
            <v-textarea
              required
              dense
              label="Description"
            />
            <v-slider
              label="Priority"
              dense
              thumb-label
            />
            <v-slider
              label="Importance"
              thumb-label
              dense
            />
            <!-- Date Picker -->
            <v-menu
              ref="startMenu"
              v-model="startMenu"
              :close-on-content-click="false"
              :nudge-right="40"
              :return-value.sync="start"
              transition="scale-transition"
              min-width="290px"
              offset-y
            >
              <template v-slot:activator="{ on }">
                <v-text-field
                  v-model="start"
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
                v-model="start"
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

export default Vue.extend({
  data() {
    return {
      startMenu: false,
      start: '2019-01-12',
    };
  },
});
</script>

<style scoped>
.controls {
  position: relative;
}
</style>

import { shallowMount } from '@vue/test-utils';
import Vue from 'vue';
import Vuetify from 'vuetify';
import HelloWorld from '@/components/HelloWorld.vue';

describe('HelloWorld.vue', () => {
  beforeAll(() => Vue.use(Vuetify));

  it('renders ecosystem', () => {
    const wrapper = shallowMount(HelloWorld, {});
    const eco = wrapper.vm.$data.ecosystem;
    eco.forEach((i: any) => {
      Object.keys(i).forEach((k) => {
        expect(wrapper.html()).toContain(i[k]);
      });
    });
  });
});

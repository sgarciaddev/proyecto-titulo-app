import './assets/main.css';

import { createApp } from 'vue';
import App from './App.vue';
import router from './router';

import { addIcons, OhVueIcon } from 'oh-vue-icons';
import {
  FaGlobe,
  FaRobot,
  FaRocket,
  HiMenu,
  HiX,
  SiGithub,
  SiLinkedin,
} from 'oh-vue-icons/icons';

const app = createApp(App);

app.use(router);

addIcons(SiGithub, SiLinkedin, FaGlobe, FaRocket, FaRobot, HiMenu, HiX);
app.component('v-icon', OhVueIcon);
app.mount('#app');

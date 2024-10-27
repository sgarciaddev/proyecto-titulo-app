import '@fontsource/monaspace-xenon/300.css';
import '@fontsource/monaspace-xenon/200.css';
import '@fontsource/monaspace-xenon';
import '@fontsource/monaspace-xenon/500.css';
import '@fontsource/monaspace-xenon/600.css';
import '@fontsource/monaspace-xenon/700.css';
import '@fontsource/monaspace-xenon/800.css';
import './assets/main.css';
import '/node_modules/flag-icons/css/flag-icons.min.css';

import { createApp } from 'vue';
import App from './App.vue';
import router from './router';

import { addIcons, OhVueIcon } from 'oh-vue-icons';
import {
  BiMemory,
  FaGlobe,
  FaRobot,
  FaRocket,
  GiForest,
  GiRocketThruster,
  HiMenu,
  HiX,
  SiGithub,
  SiLinkedin
} from 'oh-vue-icons/icons';

const app = createApp(App);

app.use(router);

addIcons(
  SiGithub,
  SiLinkedin,
  FaGlobe,
  FaRocket,
  FaRobot,
  HiMenu,
  HiX,
  GiForest,
  GiRocketThruster,
  BiMemory
);
app.component('v-icon', OhVueIcon);
app.mount('#app');

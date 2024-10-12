<script setup lang="ts">
import { onBeforeUnmount, onMounted, ref } from 'vue';

const isScrolled = ref(false);
const isOpened = ref(false);

const links = [
  {
    text: 'Inicio',
    to: { path: '/inicio', hash: '#inicio' },
  },
  {
    text: 'Amenazas',
    to: { path: '/inicio', hash: '#cyberthreat-map' },
  },
  {
    text: 'Machine Learning',
    to: { path: '/inicio', hash: '#ml' },
  },
];

const handleScroll = () => {
  isScrolled.value = window.scrollY > 0;
};

const handleToggle = () => {
  isOpened.value = !isOpened.value;
};

onMounted(() => {
  window.addEventListener('scroll', handleScroll);
});

onBeforeUnmount(() => {
  window.removeEventListener('scroll', handleScroll);
});
</script>

<template>
  <!-- Header -->
  <header
    class="fixed inset-x-0 top-0 z-50 transition-colors duration-500"
    :class="{ 'bg-black/60 ': isScrolled, 'bg-transparent': !isScrolled }"
  >
    <nav
      class="mx-auto flex max-w-7xl items-center justify-between p-6 lg:px-8"
      aria-label="Global"
    >
      <div class="flex lg:flex-1">
        <span class="-m-1.5 p-1.5">
          <span class="sr-only">DDoS Attack Simulator</span>
        </span>
      </div>
      <div class="flex lg:hidden">
        <button
          type="button"
          class="-m-2.5 inline-flex items-center justify-center rounded-md p-2.5 text-hacker-green-soft hover:text-white"
          @click="handleToggle"
        >
          <span class="sr-only">Open main menu</span>
          <v-icon name="hi-menu" class="h-6 w-6" />
        </button>
      </div>
      <div class="hidden lg:flex lg:gap-x-12">
        <RouterLink
          v-for="link in links"
          :key="link.text"
          :to="link.to"
          class="text-sm/6 font-semibold text-white hover:text-hacker-green-soft hover:font-bold"
          >{{ link.text }}
        </RouterLink>
      </div>
      <div class="hidden lg:flex lg:flex-1 lg:justify-end">
        <RouterLink
          to="/simulador"
          class="transition-transform delay-100 duration-300 ease-in-out text-sm font-bold text-black bg-hacker-green-soft/70 px-8 py-3 rounded-xl hover:scale-105 hover:bg-hacker-green-soft/90 hover:font-extrabold"
        >
          <v-icon name="fa-rocket" />
          Simulador
        </RouterLink>
      </div>
    </nav>
    <!-- Mobile menu, show/hide based on menu open state. -->
    <div class="lg:hidden" role="dialog" v-if="isOpened">
      <!-- Background backdrop, show/hide based on slide-over state. -->
      <div class="fixed inset-0 z-50"></div>
      <div
        class="fixed inset-y-0 right-0 z-50 w-full overflow-y-auto bg-zinc-900 px-6 py-6 sm:max-w-sm sm:ring-1 sm:ring-white/10"
      >
        <div class="flex items-center justify-between">
          <a href="#" class="-m-1.5 p-1.5">
            <span class="sr-only">DDoS Attack Simulator</span>
            <TheIcon class="h-12 w-auto" />
          </a>
          <button
            type="button"
            class="transition-all duration-300 hover:scale-110 -m-2.5 rounded-md p-2.5 text-white hover:text-hacker-green-soft"
            @click="handleToggle"
          >
            <span class="sr-only">Close menu</span>
            <v-icon name="hi-x" class="h-6 w-6" />
          </button>
        </div>
        <div class="mt-6 flow-root">
          <div class="-my-6 divide-y divide-zinc-500/25">
            <div class="space-y-2 py-6">
              <RouterLink
                v-for="link in links"
                :key="link.text"
                :to="link.to"
                class="-mx-3 block rounded-lg px-3 py-2 text-base/7 font-semibold text-white hover:text-hacker-green-soft"
                >{{ link.text }}
              </RouterLink>
            </div>
            <div class="py-6">
              <RouterLink
                to="/simulador"
                class="transition-all delay-100 duration-300 ease-in-out -mx-3 block rounded-lg px-3 py-2.5 text-base/7 font-semibold text-white hover:bg-hacker-green-soft hover:text-black"
              >
                <v-icon name="fa-rocket" />
                Simulador
              </RouterLink>
            </div>
          </div>
        </div>
      </div>
    </div>
  </header>
</template>

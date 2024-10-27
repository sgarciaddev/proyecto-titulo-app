<script setup lang="ts">
import TheBackground from '@/components/TheBackground.vue';
import SimulatorControls from '@/components/simulator/SimulatorControls.vue';
</script>

<template>
  <main class="relative isolate">
    <TheBackground />
    <div class="pt-32 pb-12 px-8 xl:py-40 xl:px-20">
      <h2
        class="text-4xl text-center font-semibold tracking-tight text-white sm:text-5xl"
      >
        Simulador de ataques <span class="text-hacker-green-soft">DDoS</span>
      </h2>
      <SimulatorControls class="mt-20" />
    </div>
  </main>
</template>

<style scoped></style>

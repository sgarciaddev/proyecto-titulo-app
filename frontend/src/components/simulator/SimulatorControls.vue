<script setup lang="ts">
import { ref } from 'vue';

const alg = [
  {
    value: 'none',
    label: 'Paso 1. Seleccione algoritmo',
    icon: 'fa-robot',
    description: 'Seleccione un algoritmo para iniciar la simulación.',
  },
  {
    value: 'rf',
    label: 'Random Forest',
    icon: 'gi-forest',
    description:
      'Analiza patrones complejos de tráfico para detectar anomalías que indican posibles ataques DDoS.',
  },
  {
    value: 'xgb',
    label: 'XGBoost',
    icon: 'gi-rocket-thruster',
    description:
      'Identifica rápidamente comportamientos maliciosos mediante técnicas de boosting en grandes volúmenes de datos.',
  },
  {
    value: 'lstm',
    label: 'LSTM',
    icon: 'bi-memory',
    description:
      'Predice ataques al reconocer secuencias temporales en el flujo de tráfico de la red.',
  },
];
const currentAlg = ref(alg[0]);
const algSelectOpened = ref(false);
const currentQAttacks = ref(100);
const qSelectOpened = ref(false);
</script>

<template>
  <div class="xl:mx-auto xl:max-w-6xl flex flex-col relative">
    <button
      class="text-white flex items-center gap-x-2 xl:gap-x-8 py-2 px-4 cursor-pointer bg-zinc-500 hover:bg-hacker-green-soft hover:text-black"
      @click="algSelectOpened = !algSelectOpened"
    >
      <v-icon class="h-20 w-20" name="fa-robot" />
      <h3 class="text-xl/7 ml-4">Paso 1. Seleccione algoritmo</h3>
    </button>
    <div
      v-if="algSelectOpened"
      class="absolute flex flex-col gap-y-2 bg-zinc-600 px-2 py-4"
    >
      <h4 class="text-sm text-hacker-green-soft mb-8">
        Seleccione un algoritmo:
      </h4>
      <div
        v-for="algorithm in alg.slice(1)"
        :key="algorithm.value"
        @click="
          currentAlg = algorithm;
          algSelectOpened = false;
        "
        class="flex items-center justify-between py-2 px-2 cursor-pointer hover:bg-zinc-800"
      >
        <v-icon
          class="h-12 w-12 text-hacker-green-soft"
          :name="algorithm.icon"
        />
        <h3 class="text-lg/7 text-white ml-4">{{ algorithm.label }}</h3>
      </div>
    </div>
    <button
      class="mt-20 text-white flex items-center gap-x-2 xl:gap-x-8 py-2 px-4 cursor-pointer bg-zinc-500 hover:bg-hacker-green-soft hover:text-black"
      @click="qSelectOpened = !qSelectOpened"
    >
      <v-icon class="h-20 w-20" name="fa-robot" />
      <h3 class="text-xl/7 ml-4">
        Paso 2: Seleccione cantidad de paquetes de red
      </h3>
    </button>
    <div
      v-if="qSelectOpened"
      class="absolute flex flex-col gap-y-2 bg-zinc-600 px-2 py-4"
    >
      <h4 class="text-sm text-hacker-green-soft mb-8">
        Indique cantidad de paquetes a enviar, y la proporción de ataques:
      </h4>
      <input
        class="pr-6 bg-red-500"
        type="range"
        value="100"
        min="100"
        max="250000"
        @change="
          currentQAttacks = Number.parseInt(
            ($event.target as HTMLInputElement).value
          )
        "
        @mousemove="
          currentQAttacks = Number.parseInt(
            ($event.target as HTMLInputElement).value
          )
        "
      />
      <div>
        <h3 class="text-lg/7 text-white ml-4">
          Cantidad de paquetes: {{ currentQAttacks }}
        </h3>
      </div>
      <div
        @click="qSelectOpened = false"
        class="flex items-center justify-between py-2 px-2 cursor-pointer hover:bg-zinc-800"
      >
        <h3 class="text-lg/7 text-white ml-4">Guardar</h3>
      </div>
    </div>
    <div class="mt-20 flex flex-col">
      <div class="flex items-center gap-x-8">
        <v-icon class="h-20 w-20 text-hacker-green" :name="currentAlg.icon" />
        <h3 class="text-base/7 font-bold text-white ml-4">
          Seleccionado: {{ currentAlg.label }} - {{ currentQAttacks }} paquetes
        </h3>
      </div>
      <p class="mt-4 text-sm text-white">{{ currentAlg.description }}</p>
      <p class="mt-4 text-sm text-white">
        Serán enviados a análisis la cantidad exacta de {{ currentQAttacks }}
        paquetes de red, a través de diferentes puertos y protocolos. De los
        {{ currentQAttacks }} paquetes, se espera que
        {{ Math.round(currentQAttacks * 0.2) }} sean benignos, y
        {{ currentQAttacks - Math.round(currentQAttacks * 0.2) }} sean
        maliciosos.
      </p>
    </div>
    <button
      class="mt-32 text-white flex items-center gap-x-2 xl:gap-x-8 py-2 px-4 cursor-pointer bg-hacker-green hover:bg-hacker-green-soft hover:text-black"
    >
      <v-icon class="h-20 w-20" name="fa-rocket" />
      <h3 class="text-xl/7 ml-4">Paso 3. Simular ataque</h3>
    </button>
  </div>
</template>

<style scoped></style>

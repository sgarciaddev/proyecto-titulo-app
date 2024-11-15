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
const results = ref(null);
const error = ref(null);
const isLoading = ref(false);

const simulateAttack = async () => {
  error.value = null;
  results.value = null;
  isLoading.value = true;

  // Se valida que se haya seleccionado un algoritmo
  if (currentAlg.value.value === 'none') {
    error!.value = 'Por favor, seleccione un algoritmo.';
    isLoading.value = false;
    return;
  }

  try {
    const response = await axios.post('/simulate', {
      dataset: currentAlg.value.value === 'lstm' ? 'nbaiot' : 'cicddos2019',
      model: currentAlg.value.value,
      attack_size: currentQAttacks.value,
    });

    results.value = response.data;
  } catch (err: any) {
    if (err.response) {
      error.value = err.response.data.error || 'Error al procesar la solicitud';
    } else if (err.request) {
      error.value = 'No se recibió respuesta del servidor';
    } else {
      error.value = 'Error al configurar la solicitud';
    }
  } finally {
    isLoading.value = false;
  }
};
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
        :value="currentQAttacks"
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
        class="rounded-lg flex text-white items-center justify-between py-2 px-2 cursor-pointer bg-hacker-green hover:bg-hacker-green-soft hover:text-black"
      >
        <h3 class="text-lg/7 ml-4 text-center">Guardar</h3>
      </div>
    </div>
    <div v-if="currentAlg.value != 'none'" class="mt-20 flex flex-col">
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
        {{ Math.round(currentQAttacks * 0.08) }} sean benignos, y
        {{ currentQAttacks - Math.round(currentQAttacks * 0.08) }} sean
        maliciosos.
      </p>
    </div>
    <button
      class="mt-32 text-white flex items-center gap-x-2 xl:gap-x-8 py-2 px-4 cursor-pointer bg-hacker-green hover:bg-hacker-green-soft hover:text-black"
      @click="simulateAttack"
    >
      <v-icon class="h-20 w-20" name="fa-rocket" />
      <p class="text-xl/7 ml-4">Paso 3. Simular ataque</p>
    </button>
    <div v-if="isLoading" class="mt-8">
      <p class="text-white">Simulando ataque, por favor espera...</p>
    </div>

    <div v-if="error" class="mt-8">
      <p class="text-red-500">Error: {{ error }}</p>
    </div>

    <div v-if="results" class="mt-8 text-white">
      <h2 class="text-xl font-bold">Resultados de la Simulación:</h2>
      <ul class="mt-4">
        <li>TP (Verdaderos Positivos): {{ results.TP }}</li>
        <li>FP (Falsos Positivos): {{ results.FP }}</li>
        <li>TN (Verdaderos Negativos): {{ results.TN }}</li>
        <li>FN (Falsos Negativos): {{ results.FN }}</li>
      </ul>
    </div>
  </div>
</template>

<style scoped></style>

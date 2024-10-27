<script setup lang="ts">
const ml = [
  {
    name: 'Random Forest',
    icon: 'gi-forest',
    description:
      'Analiza patrones complejos de tráfico para detectar anomalías que indican posibles ataques DDoS.'
  },
  {
    name: 'XGBoost',
    icon: 'gi-rocket-thruster',
    description:
      'Identifica rápidamente comportamientos maliciosos mediante técnicas de boosting en grandes volúmenes de datos.'
  },
  {
    name: 'LSTM',
    icon: 'bi-memory',
    description:
      'Predice ataques al reconocer secuencias temporales en el flujo de tráfico de la red.'
  }
];
</script>

<template>
  <div id="ml" class="mx-auto my-8 pt-24 max-w-7xl px-6 sm:pt-32 lg:px-8">
    <div class="mx-auto max-w-2xl lg:mx-0">
      <h2
        class="text-pretty text-4xl font-semibold tracking-tight text-white sm:text-5xl"
      >
        Detección y mitigación usando
        <span class="text-hacker-green-soft font-extrabold"
          >Machine Learning</span
        >
      </h2>
      <p class="mt-6 text-lg/8 text-zinc-300">
        Para enfrentar los desafíos que representan los ataques DDoS, se emplean
        algoritmos avanzados, los que permiten su detección y mitigación de
        manera eficiente.
      </p>
    </div>
    <dl
      class="mx-auto mt-16 grid max-w-2xl grid-cols-1 gap-4 text-base/7 text-zinc-300 sm:grid-cols-2 lg:mx-0 lg:max-w-none lg:grid-cols-3"
    >
      <div v-for="algorithm in ml" class="relative pl-20 xl:pl-28">
        <dt class="inline font-semibold text-white mr-4">
          <v-icon
            class="absolute left-0 top-1 h-16 w-16 text-hacker-green xl:w-24 xl:h-24"
            :name="algorithm.icon"
          />
          {{ algorithm.name }}
        </dt>
        <dd class="inline">
          {{ algorithm.description }}
        </dd>
      </div>
    </dl>
    <RouterLink
      to="/simulador"
      class="text-lg my-12 2xl:text-2xl 2xl:my-16 text-center transition-all delay-100 duration-300 ease-in-out w-full block rounded-lg py-8 font-semibold text-hacker-green-soft bg-zinc-600 hover:bg-hacker-green-soft hover:text-black"
    >
      <v-icon class="w-12 h-8" name="fa-rocket" />
      Prueba nuestro simulador impulsado por IA
    </RouterLink>
  </div>
</template>

<style scoped></style>

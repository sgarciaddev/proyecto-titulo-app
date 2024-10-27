<script setup lang="ts"></script>

<template>
  <div
    id="cyberthreat-map"
    class="my-12 pt-24 sm:pt-32 xl:mx-auto xl:max-w-7xl"
  >
    <h3 class="mb-16 text-4xl text-white text-center">
      Ataques cibernéticos
      <span class="text-hacker-green-soft">en tiempo real</span>
    </h3>
    <iframe
      class="cyberthreat-map px-10 xl:px-0"
      src="https://cybermap.kaspersky.com/es/widget/dynamic/dark"
    ></iframe>
    <p class="px-12 mt-8 xl:px-20 w-full text-base/7 text-zinc-100 md:mt-16">
      El
      <a
        class="font-extrabold text-zinc-100 hover:text-hacker-green-soft"
        target="_blank"
        href="https://cybermap.kaspersky.com/"
        >mapa interactivo de Kaspersky</a
      >
      muestra
      <span class="font-extrabold text-zinc-100">en tiempo real</span> cómo las
      amenazas cibernéticas se propagan globalmente,
      <span class="font-extrabold text-zinc-100"
        >subrayando la urgencia de proteger nuestros activos digitales</span
      >. Innovar en la investigación de soluciones de ciberseguridad avanzadas e
      innovadoras es esencial para detectar y neutralizar ataques cada vez más
      sofisticados, garantizando un entorno digital más seguro y resiliente para
      todos.
    </p>
  </div>
</template>

<style scoped>
.cyberthreat-map {
  width: 100%;
  aspect-ratio: 16 / 9;
  object-fit: cover;
  border-radius: 1rem;
}
</style>

<script setup lang="ts">
import TheIcon from '@/components/TheIcon.vue';
</script>

<template>
  <footer class="bg-zinc-900">
    <div
      class="mx-auto max-w-7xl px-6 py-12 md:flex md:items-center md:justify-between lg:px-8"
    >
      <div class="flex justify-center gap-x-6 md:order-2">
        <a
          href="https://linkedin.com/in/sgarciad"
          target="_blank"
          class="text-zinc-400 hover:text-zinc-300"
        >
          <span class="sr-only">LinkedIn</span>
          <v-icon class="h-8 w-auto" name="si-linkedin" />
        </a>
        <a
          href="https://sgarciad.me"
          target="_blank"
          class="text-zinc-400 hover:text-zinc-300"
        >
          <span class="sr-only">Sitio Web</span>
          <v-icon class="h-8 w-auto" name="fa-globe" />
        </a>
        <a
          href="https://github.com/sgarciaddev"
          target="_blank"
          class="ml-8 text-zinc-400 hover:text-zinc-300"
        >
          <span class="sr-only">GitHub</span>
          <v-icon class="h-8 w-auto" name="si-github" />
        </a>
      </div>
      <div class="flex items-center gap-x-8">
        <TheIcon class="h-16 w-auto" />
        <p class="mt-8 text-center text-sm/6 text-zinc-400 md:order-1 md:mt-0">
          2024 | Desarrollado por Sebastián García Delgadillo (<a
            class="text-hacker-green-soft hover:text-hacker-green"
            href="https://github.com/sgarciaddev"
            >@sgarciaddev</a
          >)
        </p>
      </div>
    </div>
  </footer>
</template>

<style scoped></style>

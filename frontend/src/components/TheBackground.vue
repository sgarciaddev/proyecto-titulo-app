<script setup lang="ts"></script>

<template>
  <div
    class="absolute top-4 -z-10 flex transform-gpu justify-center overflow-hidden blur-3xl"
  >
    <div
      class="opacity-15 background w-full bg-gradient-to-b from-hacker-green-soft to-hacker-green"
    ></div>
  </div>
</template>

<style scoped>
.background {
  clip-path: polygon(
    0% 70%,
    15% 50%,
    30% 75%,
    45% 40%,
    60% 80%,
    75% 50%,
    85% 85%,
    100% 40%,
    85% 20%,
    60% 25%,
    45% 10%,
    30% 25%,
    15% 0%,
    0% 20%
  );
  aspect-ratio: 4 / 3;
}
</style>

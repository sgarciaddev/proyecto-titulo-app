<script setup lang="ts">
import TheHeader from '@/components/TheHeader.vue';
import TheFooter from '@/components/TheFooter.vue';
</script>

<template>
  <div class="bg-zinc-900 min-h-svh">
    <TheHeader />
    <slot />
    <TheFooter />
  </div>
</template>

<style scoped></style>

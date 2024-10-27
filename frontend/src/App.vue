<template>
  <MainLayout>
    <Transition
      name="fade-slide"
      mode="in-out"
      enter-active-class="transition-all duration-500 ease-in"
      enter-from-class="opacity-0"
      enter-to-class="opacity-100"
      leave-active-class="transition-all duration-500 ease-out"
      leave-from-class="opacity-100"
      leave-to-class="opacity-0"
    >
      <RouterView />
    </Transition>
  </MainLayout>
</template>

<script lang="ts" setup>
import { RouterView } from 'vue-router';
import MainLayout from '@/layouts/MainLayout.vue';
</script>

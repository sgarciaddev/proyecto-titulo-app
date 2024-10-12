<template>
  <MainLayout>
    <RouterView />
  </MainLayout>
</template>

<script lang="ts" setup>
import { RouterView } from 'vue-router';
import MainLayout from '@/layouts/MainLayout.vue';
</script>

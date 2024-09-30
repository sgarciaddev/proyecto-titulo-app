<script setup lang="ts">
defineProps<{
  msg: string;
}>();
</script>

<template>
  <h1 class="text-green-500 text-2xl font-semibold">{{ msg }}</h1>
</template>

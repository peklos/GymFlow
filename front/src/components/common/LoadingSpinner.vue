<template>
  <div class="flex justify-center items-center" :class="containerClass">
    <div class="relative">
      <div class="w-16 h-16 border-4 border-primary-200 border-t-primary-600 rounded-full animate-spin"></div>
      <div class="absolute inset-0 w-16 h-16 border-4 border-transparent border-r-accent-600 rounded-full animate-spin" style="animation-direction: reverse; animation-duration: 1.5s;"></div>
    </div>
    <p v-if="text" class="ml-4 text-slate-600 font-medium">{{ text }}</p>
  </div>
</template>

<script setup>
defineProps({
  text: {
    type: String,
    default: ''
  },
  containerClass: {
    type: String,
    default: 'py-12'
  }
})
</script>

<style scoped>
</style>

<template>
  <div class="card card-hover group">
    <div class="flex flex-col h-full">
      <!-- Header with Icon -->
      <div class="flex items-start justify-between mb-4">
        <div class="flex-1">
          <h3 class="text-xl font-bold text-slate-800 mb-2 group-hover:text-primary-600 transition-colors">
            {{ section.name }}
          </h3>
          <div class="flex items-center gap-2 text-sm text-slate-600">
            <span class="badge badge-info">{{ section.sport_type }}</span>
            <span v-if="section.is_free" class="badge badge-success">Бесплатно</span>
          </div>
        </div>
        <div class="w-12 h-12 bg-gradient-to-br from-primary-100 to-accent-100 rounded-xl flex items-center justify-center group-hover:scale-110 transition-transform">
          <svg class="w-6 h-6 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" />
          </svg>
        </div>
      </div>

      <!-- Description -->
      <p class="text-slate-600 mb-4 flex-1 line-clamp-2">
        {{ section.description }}
      </p>

      <!-- Age Range -->
      <div class="flex items-center gap-2 mb-4 text-sm">
        <svg class="w-5 h-5 text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197M13 7a4 4 0 11-8 0 4 4 0 018 0z" />
        </svg>
        <span class="text-slate-600">
          Возраст: <span class="font-semibold">{{ section.age_from }}-{{ section.age_to }} лет</span>
        </span>
      </div>

      <!-- Action Button -->
      <button
        @click="$emit('view-details', section.id)"
        class="btn btn-primary w-full mt-2"
      >
        Подробнее
      </button>
    </div>
  </div>
</template>

<script setup>
defineProps({
  section: {
    type: Object,
    required: true
  }
})

defineEmits(['view-details'])
</script>

<style scoped>
.line-clamp-2 {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style>

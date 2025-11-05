<template>
  <div>
    <div class="mb-8">
      <h1 class="text-3xl font-bold text-slate-800 mb-2">Управление клиентами</h1>
      <p class="text-slate-600">Просмотр и редактирование информации о клиентах</p>
    </div>

    <LoadingSpinner v-if="isLoading" text="Загрузка клиентов..." />

    <div v-else-if="clients.length > 0" class="card">
      <div class="overflow-x-auto">
        <table class="w-full">
          <thead>
            <tr class="border-b border-slate-200">
              <th class="text-left py-3 px-4 font-semibold text-slate-700">ID</th>
              <th class="text-left py-3 px-4 font-semibold text-slate-700">ФИО</th>
              <th class="text-left py-3 px-4 font-semibold text-slate-700">Телефон</th>
              <th class="text-left py-3 px-4 font-semibold text-slate-700">Возраст</th>
              <th class="text-left py-3 px-4 font-semibold text-slate-700">Пол</th>
            </tr>
          </thead>
          <tbody>
            <tr
              v-for="client in clients"
              :key="client.id"
              class="border-b border-slate-100 hover:bg-slate-50 transition-colors"
            >
              <td class="py-3 px-4">{{ client.id }}</td>
              <td class="py-3 px-4 font-medium">{{ client.last_name }} {{ client.first_name }} {{ client.patronymic }}</td>
              <td class="py-3 px-4">{{ client.phone_number }}</td>
              <td class="py-3 px-4">{{ calculateAge(client.birth_date) }} лет</td>
              <td class="py-3 px-4">{{ client.gender }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <div v-else class="card text-center py-12">
      <p class="text-slate-600">Клиенты не найдены</p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import LoadingSpinner from '@/components/common/LoadingSpinner.vue'
import { adminClientsService } from '@/api/services'

const clients = ref([])
const isLoading = ref(false)

onMounted(async () => {
  await loadClients()
})

const loadClients = async () => {
  try {
    isLoading.value = true
    const response = await adminClientsService.getAll()
    clients.value = response.data
  } catch (error) {
    console.error('Error loading clients:', error)
  } finally {
    isLoading.value = false
  }
}

const calculateAge = (birthDate) => {
  const today = new Date()
  const birth = new Date(birthDate)
  let age = today.getFullYear() - birth.getFullYear()
  const monthDiff = today.getMonth() - birth.getMonth()
  if (monthDiff < 0 || (monthDiff === 0 && today.getDate() < birth.getDate())) {
    age--
  }
  return age
}
</script>

<style scoped>
</style>

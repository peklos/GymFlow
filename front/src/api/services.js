import api from './axios'

// Auth Services
export const authService = {
  register: (data) => api.post('/auth/register', data),
  login: (data) => api.post('/auth/login', data),
  getUser: (userId) => api.get(`/auth/me/${userId}`),
}

// Profile Services
export const profileService = {
  getProfile: (clientId) => api.get(`/profile/${clientId}`),
  updateProfile: (clientId, data) => api.patch(`/profile/${clientId}`, data),
}

// Sections Services
export const sectionsService = {
  getAll: (params) => api.get('/sections/', { params }),
  getById: (id) => api.get(`/sections/${id}`),
}

// Schedule Services
export const scheduleService = {
  getAll: (params) => api.get('/schedule/', { params }),
  getById: (id) => api.get(`/schedule/${id}`),
}

// Bookings Services
export const bookingsService = {
  create: (data) => api.post('/bookings/', data),
  getByClient: (clientId) => api.get(`/bookings/client/${clientId}`),
  cancel: (id) => api.delete(`/bookings/${id}`),
}

// Admin Auth Services
export const adminAuthService = {
  login: (data) => api.post('/admin/auth/login', data),
  getEmployee: (employeeId) => api.get(`/admin/auth/me/${employeeId}`),
}

// Admin Clients Services
export const adminClientsService = {
  getAll: (params) => api.get('/admin/clients/', { params }),
  getById: (id) => api.get(`/admin/clients/${id}`),
  update: (id, data) => api.patch(`/admin/clients/${id}`, data),
  delete: (id) => api.delete(`/admin/clients/${id}`),
}

// Admin Trainers Services
export const adminTrainersService = {
  getAll: (params) => api.get('/admin/trainers/', { params }),
  create: (data) => api.post('/admin/trainers/', data),
  update: (id, data) => api.patch(`/admin/trainers/${id}`, data),
  delete: (id) => api.delete(`/admin/trainers/${id}`),
}

// Admin Sections Services
export const adminSectionsService = {
  getAll: (params) => api.get('/admin/sections/', { params }),
  create: (data) => api.post('/admin/sections/', data),
  update: (id, data) => api.patch(`/admin/sections/${id}`, data),
  delete: (id) => api.delete(`/admin/sections/${id}`),
}

// Admin Schedule Services
export const adminScheduleService = {
  getAll: (params) => api.get('/admin/schedule/', { params }),
  create: (data) => api.post('/admin/schedule/', data),
  update: (id, data) => api.patch(`/admin/schedule/${id}`, data),
  delete: (id) => api.delete(`/admin/schedule/${id}`),
}

// Admin Bookings Services
export const adminBookingsService = {
  getAll: (params) => api.get('/admin/bookings/', { params }),
  getById: (id) => api.get(`/admin/bookings/${id}`),
  updateStatus: (id, data) => api.patch(`/admin/bookings/${id}`, data),
  getStats: () => api.get('/admin/bookings/stats/overview'),
}

// Admin Attendance Services
export const adminAttendanceService = {
  getAll: (params) => api.get('/admin/attendance/', { params }),
  mark: (data) => api.post('/admin/attendance/', data),
  update: (id, data) => api.patch(`/admin/attendance/${id}`, data),
}

// Admin Employees Services
export const adminEmployeesService = {
  getAll: (params) => api.get('/admin/employees/', { params }),
  create: (data) => api.post('/admin/employees/', data),
  update: (id, data) => api.patch(`/admin/employees/${id}`, data),
  delete: (id) => api.delete(`/admin/employees/${id}`),
}

// Admin Roles Services
export const adminRolesService = {
  getAll: () => api.get('/admin/roles/'),
}

// Admin Stats Services
export const adminStatsService = {
  getDashboard: () => api.get('/admin/stats/dashboard/'),
}

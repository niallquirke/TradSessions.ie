import axios from 'axios'
import endpoints from '@/cloud.config'

const apiClient = axios.create({
  baseURL: endpoints.PublicEventServiceApiEndpoint,
  headers: {
    Accept: 'application/json',
    'Content-Type': 'application/x-www-form-urlencoded'
  },
  timeout: 10000
})

export default {
  getEvents(page) {
    return apiClient.get('/events?page=' + page)
  },
  getEvent(id) {
    return apiClient.get('/events?id=' + id)
  }
}

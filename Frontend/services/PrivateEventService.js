import axios from 'axios'
import endpoints from '@/cloud.config'

const apiClient = axios.create({
  baseURL: endpoints.PrivateEventServiceApiEndpoint,
  headers: {
    Accept: 'application/json',
    'Content-Type': 'application/json'
  },
  timeout: 10000
})

export default {
  getUserEvents(user, page, idToken) {
    apiClient.defaults.headers.common.Authorization = idToken
    return apiClient.get('/events?user=' + user + '&page=' + page)
  },
  createEvent(event, idToken) {
    apiClient.defaults.headers.common.Authorization = idToken
    return apiClient.post('/events', event)
  }
}

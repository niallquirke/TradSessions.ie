import axios from 'axios'

const apiClient = axios.create({
  baseURL: 'https://0rdjsjwb3c.execute-api.eu-west-1.amazonaws.com/Prod/',
  withCredentials: false,
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
  },
  createEvent(event) {
    return apiClient.post('/events', event)
  }
}

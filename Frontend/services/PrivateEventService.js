import axios from 'axios'

const apiClient = axios.create({
  baseURL: 'https://jzkmw995q4.execute-api.eu-west-1.amazonaws.com/Prod/',
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

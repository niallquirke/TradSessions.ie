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
  getUserEvents(username, page, idToken) {
    apiClient.defaults.headers.common.Authorization = idToken
    console.log(username, page)
    return apiClient.get('/events')
  }
}

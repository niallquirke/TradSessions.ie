import UserService from '@/services/UserService.js'
import PrivateEventService from '@/services/PrivateEventService'

export const state = () => ({
  user: {},
  events: [],
  idToken: null,
  directedFromCreate: false
})

export const mutations = {
  SET_USER(state, response) {
    state.idToken = response.idToken.jwtToken
    state.user = response.idToken.payload
    state.user.username = state.user['cognito:username']
  },
  CLEAR_USER() {
    location.reload()
  },
  SET_USER_EVENTS(state, userEvents) {
    state.events = userEvents
  },
  SET_DIRECTED_FROM_CREATE(state, directed) {
    state.directedFromCreate = directed
  }
}

export const actions = {
  login({ commit }, creds) {
    return UserService.login(creds).then((response) => {
      commit('SET_USER', response)
    })
  },
  logout({ commit }) {
    return UserService.logout().then(() => {
      commit('CLEAR_USER')
    })
  },
  fetchUserEvents({ commit, state }, page) {
    return PrivateEventService.getUserEvents(
      state.user.username,
      page,
      state.idToken
    ).then((response) => {
      commit('SET_USER_EVENTS', response.data)
    })
  },
  setDirectedFromCreate({ commit }, directed) {
    commit('SET_DIRECTED_FROM_CREATE', directed)
  },
  createEvent({ state }, event) {
    event.user = state.user.username
    return PrivateEventService.createEvent(event, state.idToken)
  }
}

export const getters = {
  isAuthenticated: (state) => !!state.idToken
}

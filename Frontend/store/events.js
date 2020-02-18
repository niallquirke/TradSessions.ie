import PublicEventService from '~/services/PublicEventService.js'

export const state = () => ({
  events: [],
  event: {}
})

export const mutations = {
  SET_EVENTS(state, events) {
    state.events = events
  },
  SET_EVENT(state, event) {
    state.event = event
  }
}

export const actions = {
  fetchEvents({ commit }, page) {
    return PublicEventService.getEvents(page).then((response) => {
      commit('SET_EVENTS', response.data)
    })
  },
  fetchEvent({ commit }, id) {
    return PublicEventService.getEvent(id).then((response) => {
      commit('SET_EVENT', response.data)
    })
  },
  createEvent({ commit }, event) {
    return PublicEventService.createEvent(event).then(() => {
      commit('SET_EVENT', event)
    })
  }
}

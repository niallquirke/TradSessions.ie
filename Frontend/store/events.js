import EventService from '@/services/EventService.js'

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
    return EventService.getEvents(page).then((response) => {
      commit('SET_EVENTS', response.data)
    })
  },
  fetchEvent({ commit }, id) {
    return EventService.getEvent(id).then(function(response) {
      commit('SET_EVENT', response.data)
    })
  },
  createEvent({ commit }, event) {
    return EventService.createEvent(event).then(() => {
      commit('SET_EVENT', event)
    })
  }
}

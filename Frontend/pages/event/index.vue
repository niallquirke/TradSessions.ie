<template>
  <div class="body">
    <div class="event-header">
      <h1 class="title">{{ event.title }}</h1>
      <h5>By {{ event.user }}</h5>
    </div>
    <h2>Where</h2>
    <p>{{ event.location }}, {{ event.county }}</p>
    <h2>When</h2>
    <p>{{ event.day }} @ {{ event.time }}</p>
    <h2>The Craic</h2>
    <p>{{ event.craic }}</p>
  </div>
</template>

<script>
import { mapState } from 'vuex'
export default {
  head() {
    return {
      title: this.event.title,
      meta: [
        {
          hid: 'description',
          name: 'description',
          content:
            'What you need to know about this session ' + this.event.title
        }
      ]
    }
  },
  computed: mapState({
    event: (state) => state.events.event
  }),
  async fetch({ store, route, error }) {
    try {
      await store.dispatch('events/fetchEvent', route.query.id)
    } catch (e) {
      error({
        statusCode: 503,
        message: 'Unable to fetch session #' + route.query.id
      })
    }
  }
}
</script>

<style scoped>
.location {
  margin-bottom: 0;
}
.location > .icon {
  margin-left: 10px;
}
.event-header > .title {
  margin-top: 4%;
}
.list-group {
  margin: 0;
  padding: 0;
  list-style: none;
}
.list-group > .list-item {
  padding: 1em 0;
  border-bottom: solid 1px #e5e5e5;
}
</style>

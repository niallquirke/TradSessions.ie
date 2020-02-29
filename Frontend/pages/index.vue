<template>
  <div class="body">
    <H1>So what's the craic with the trad sessions?</H1>
    <EventCard
      v-for="(event, index) in events.events"
      :key="index"
      :data-index="index"
      :event="event"
      :rank="index + 1 + (page - 1) * 10"
    />
    <nuxt-link v-show="page != 1" :to="{ path: '/', query: { page: page - 1 } }"
      >Prev Page</nuxt-link
    >
    <template v-if="page != 1 && !events.last_page">|</template>
    <nuxt-link
      v-show="!events.last_page"
      :to="{ path: '/', query: { page: page + 1 } }"
      >Next Page</nuxt-link
    >
  </div>
</template>

<script>
import { mapState } from 'vuex'
import EventCard from '@/components/EventCard.vue'

export default {
  head() {
    return {
      title: 'TradSessions.ie',
      meta: [
        {
          hid: 'description',
          name: 'description',
          content:
            'A list of the top traditional Irish music sessions in Ireland'
        }
      ]
    }
  },
  components: {
    EventCard
  },
  computed: {
    page() {
      return parseInt(this.$route.query.page) || 1
    },
    ...mapState({
      events: (state) => state.events.events
    })
  },
  watch: {
    $route: {
      handler: 'urlChange',
      immediate: true
    }
  },
  async fetch({ store, error, route }) {
    try {
      const page = parseInt(route.query.page) || 1
      await store.dispatch('events/fetchEvents', page)
    } catch (e) {
      error({
        statusCode: 503,
        message: 'Unable to fetch events at this time. Please try again later.'
      })
    }
  },
  methods: {
    async urlChange() {
      try {
        const page = parseInt(this.$route.query.page) || 1
        await this.$store.dispatch('events/fetchEvents', page)
      } catch (error) {
        error({
          statusCode: 503,
          message:
            'Unable to fetch events at this time. Please try again later.'
        })
      }
    }
  }
}
</script>

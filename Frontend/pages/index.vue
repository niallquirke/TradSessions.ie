<template>
  <div class="body">
    <H1>{{ phrase }}</H1>
    <EventCard
      v-for="(event, index) in events.events"
      :key="index"
      :data-index="index"
      :event="event"
      :rank="index + 1 + (page - 1) * 10"
    />
    <div>
      <nuxt-link
        v-show="page != 1"
        :to="{ path: '/', query: { page: page - 1 } }"
        >Prev Page</nuxt-link
      >
      <template v-if="page != 1 && !events.last_page">|</template>
      <nuxt-link
        v-show="!events.last_page"
        :to="{ path: '/', query: { page: page + 1 } }"
        >Next Page</nuxt-link
      >
      <template v-if="!events.last_page">|</template>
      <a href="https://niallquirke.com/contact.html" target="_blank">Contact</a>
    </div>
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
            'A platform to find, share and review Irish traditional music sessions.'
        }
      ]
    }
  },
  components: {
    EventCard
  },
  data() {
    return {
      phrases: [
        "So what's the craic with the trad sessions?",
        'Are ye still at the music?',
        "C'mere 'til I tell ye",
        'Stay quiet!',
        "Hack a'you",
        'Christ on a bike!',
        'Shsssh!',
        'Sure look it',
        'Sure listen',
        'tis what it tis now yanno yourself now',
        'Great drying out this weather',
        'Mon the town',
        'Yup outta that'
      ]
    }
  },
  computed: {
    page() {
      return parseInt(this.$route.query.page) || 1
    },
    phrase() {
      return this.phrases[Math.floor(Math.random() * this.phrases.length)]
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
        message:
          'Unable to fetch sessions at this time. Please try again later.'
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
            'Unable to fetch sessions at this time, please try again later.'
        })
      }
    }
  }
}
</script>

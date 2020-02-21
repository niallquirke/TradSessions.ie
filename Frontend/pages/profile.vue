<template>
  <div>
    <H1>{{ user.preferred_username }}'s Events</H1>
    <p v-show="events.events.length == 0">
      You haven't created any sessions yet :(
    </p>
    <p v-show="events.events.length == 0">
      <n-link to="/event/create">Create a one now!</n-link>
    </p>
    <EventCard
      v-for="(event, index) in events.events"
      :key="index"
      :event="event"
      :data-index="index"
    />
    <nuxt-link v-show="page != 1" :to="{ path: '/', query: { page: page - 1 } }"
      >Prev Page</nuxt-link
    >
    <!--<template v-if="page != 1 && !events.last_page">|</template>-->
    <nuxt-link v-show="false" :to="{ path: '/', query: { page: page + 1 } }"
      >Next Page</nuxt-link
    >
    <!--<template v-if="page != 1 || !events.last_page">|</template>-->
    <nuxt-link to="/" @click.native="logout">Log Out</nuxt-link>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import EventCard from '@/components/EventCard.vue'

export default {
  middleware: 'auth',
  components: {
    EventCard
  },
  computed: {
    page() {
      return parseInt(this.$route.query.page) || 1
    },
    ...mapState({
      events: (state) => state.user.events,
      user: (state) => state.user.user
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
      await store.dispatch('user/fetchUserEvents', page)
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
        await this.$store.dispatch('user/fetchUserEvents', page)
      } catch (error) {
        error({
          statusCode: 503,
          message:
            'Unable to fetch events at this time. Please try again later.'
        })
      }
    },
    logout() {
      this.$router.push({ path: '/' }, () => {
        this.$store.dispatch('user/logout')
      })
    }
  }
}
</script>

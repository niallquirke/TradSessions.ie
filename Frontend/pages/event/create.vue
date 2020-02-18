<template>
  <div>
    <h1>Create a Session</h1>
    <form @submit.prevent="createEvent">
      <h3>Session</h3>
      <BaseInput
        v-model="event.title"
        :class="{ error: $v.event.title.$error }"
        @blur="$v.event.title.$touch()"
        placeholder="Monday's at Murphy's"
        type="text"
      />
      <template v-if="$v.event.title.$error">
        <p v-if="!$v.event.title.required" class="errorMessage">
          Title is required.
        </p>
      </template>

      <h3>Where</h3>
      <BaseInput
        v-model="event.location"
        :class="{ error: $v.event.location.$error }"
        @blur="$v.event.location.$touch()"
        placeholder="Murphy's"
        type="text"
      />
      <template v-if="$v.event.location.$error">
        <p v-if="!$v.event.location.required" class="errorMessage">
          Location is required.
        </p>
      </template>
      <BaseSelect
        :options="counties"
        v-model="event.county"
        :class="{ error: $v.event.county.$error }"
        @blur="$v.event.county.$touch()"
        label="County"
      />
      <template v-if="$v.event.county.$error">
        <p v-if="!$v.event.county.required" class="errorMessage">
          County is required.
        </p>
      </template>

      <h3>When</h3>
      <BaseSelect
        :options="days"
        v-model="event.day"
        :class="{ error: $v.event.day.$error }"
        @blur="$v.event.day.$touch()"
        label="Day"
      />
      <template v-if="$v.event.day.$error">
        <p v-if="!$v.event.day.required" class="errorMessage">
          Day is required.
        </p>
      </template>
      <BaseSelect
        :options="times"
        v-model="event.time"
        :class="{ error: $v.event.time.$error }"
        @blur="$v.event.time.$touch()"
        label="Time"
      />
      <template v-if="$v.event.time.$error">
        <p v-if="!$v.event.time.required" class="errorMessage">
          Time is required.
        </p>
      </template>

      <h3>The Craic</h3>
      <BaseInput
        v-model="event.description"
        :class="{ error: $v.event.description.$error }"
        @blur="$v.event.description.$touch()"
        placeholder="Lovely Pints"
        type="text"
      />
      <template v-if="$v.event.description.$error">
        <p v-if="!$v.event.description.required" class="errorMessage">
          The craic is required.
        </p>
      </template>

      <div class="button_cont" align="center">
        <BaseButton
          :disabled="$v.$anyError"
          type="submit"
          button-class="-fill-gradient"
          >Create</BaseButton
        >
      </div>
    </form>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import { required } from 'vuelidate/lib/validators'

export default {
  middleware: 'auth',
  data() {
    return {
      event: this.createFreshEventObject(),
      days: [
        'Mondays',
        'Tuesdays',
        'Wednesdays',
        'Thursdays',
        'Fridays',
        'Saturdays',
        'Sundays'
      ],
      counties: [
        'Antrim',
        'Armagh',
        'Carlow',
        'Cavan',
        'Clare',
        'Cork',
        'Derry',
        'Donegal',
        'Down',
        'Dublin',
        'Fermanagh',
        'Galway',
        'Kerry',
        'Kildare',
        'Kilkenny',
        'Laois',
        'Leitrim',
        'Limerick',
        'Longford',
        'Louth',
        'Mayo',
        'Meath',
        'Monaghan',
        'Offaly',
        'Roscommon',
        'Sligo',
        'Tipperary',
        'Tyrone',
        'Waterford',
        'Westmeath',
        'Wexford',
        'Wicklow'
      ]
    }
  },
  computed: {
    times() {
      const times = []
      for (let i = 1; i <= 12; i++) {
        times.push(i + 'am')
      }
      for (let i = 1; i <= 12; i++) {
        times.push(i + 'pm')
      }
      return times
    },
    ...mapState(['user'])
  },
  methods: {
    createFreshEventObject() {
      return {
        id: Math.floor(Math.random() * 10000000).toString(),
        user: this.$store.state.user.user,
        title: '',
        location: '',
        county: '',
        day: '',
        time: '',
        description: '',
        comments: []
      }
    },
    createEvent() {
      this.$v.$touch()
      if (!this.$v.$invalid) {
        this.$store.dispatch('events/createEvent', this.event).then(() => {
          this.$router.push({
            name: 'event',
            query: { id: this.event.id }
          })
        })
      }
    }
  },
  validations: {
    event: {
      title: { required },
      location: { required },
      county: { required },
      day: { required },
      time: { required },
      description: { required }
    }
  }
}
</script>

<style scoped>
.field {
  margin-bottom: 24px;
}
</style>

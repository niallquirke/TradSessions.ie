<template>
  <nuxt-link
    :to="{ path: '/event', query: { id: event.id } }"
    class="event-link"
  >
    <div class="event-card -shadow">
      <span class="eyebrow">{{ event.day }} @ {{ event.time }}</span>
      <span class="rank">{{ rank }}.</span>
      <h4>{{ event.title }}</h4>
      <BaseIcon name="users">0 comments</BaseIcon>
    </div>
  </nuxt-link>
</template>

<script>
export default {
  name: 'EventCard',
  props: {
    event: Object,
    rank: Number
  }
}
</script>
<style scoped>
.event-card {
  background-color: white;
  padding: 20px;
  margin-bottom: 24px;
  transition: all 0.2s linear;
  cursor: pointer;
  border-radius: 15px;
  position: relative;
}
.event-card:hover {
  transform: scale(1.01);
  box-shadow: 0 3px 12px 0 rgba(0, 0, 0, 0.2), 0 1px 15px 0 rgba(0, 0, 0, 0.19);
}
.event-card > .title {
  margin: 0;
}
.event-link {
  color: black;
  text-decoration: none;
  font-weight: 100;
}
.rank {
  position: absolute;
  right: 5%;
  font-size: 20px;
  color: grey;
}
</style>

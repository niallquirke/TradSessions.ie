<template>
  <div class="nav">
    <nuxt-link @click.native="setDirectedFromCreate(false)" to="/" class="brand"
      >TradSessions.ie</nuxt-link
    >
    <nav>
      <n-link @click.native="setDirectedFromCreate(true)" to="/event/create"
        ><BaseIcon
          name="plus"
          width="50px"
          height="50px"
          color="green"
        ></BaseIcon
      ></n-link>
      <n-link @click.native="setDirectedFromCreate(false)" to="/profile"
        ><BaseIcon
          name="user"
          width="50px"
          height="50px"
          color="green"
        ></BaseIcon
      ></n-link>
    </nav>
  </div>
</template>

<script>
export default {
  methods: {
    setDirectedFromCreate(directed) {
      this.$store.dispatch('user/setDirectedFromCreate', directed)
    }
  }
}
</script>

<style scoped>
.nav {
  background-color: #fff;
  height: 60px;
  padding: 0 20px 0px 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 1.2em;
  border: 1px solid #dbdbdb;
  border-radius: 0px 0px 15px 15px;
}
.nav .nav-item {
  box-sizing: border-box;
  margin: 0 5px;
  color: rgba(0, 0, 0, 0.5);
  text-decoration: none;
}
.nav .nav-item.router-link-exact-active {
  color: #39b982;
  border-bottom: solid 2px #39b982;
}
.nav a {
  display: inline-block;
}
.brand {
  font-family: 'Montserrat', sans-serif;
  font-weight: 700;
  font-size: 1.5em;
  color: #39b982;
  text-decoration: none;
}
</style>

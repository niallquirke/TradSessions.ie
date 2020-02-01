<template>
  <dev class="login-wrapper">
    <div class="login">
      <h2>So who's this now?</h2>
      <form>
        <label for="name">Username:</label>
        <BaseInput v-model="name" type="text" name="name" value="Optional" />

        <label for="email">Email:</label>
        <BaseInput v-model="email" type="email" name="email" value />

        <label for="password">Password:</label>
        <BaseInput v-model="password" type="password" name value />

        <BaseButton type="submit" name="button" button-class="-fill-gradient">
          Sign Up / Login
        </BaseButton>
      </form>
    </div>
  </dev>
</template>

<script>
export default {
  data() {
    return {
      name: '',
      email: '',
      password: ''
    }
  }
}
</script>

<style scoped>
.login-wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
}
.login {
  width: 80%;
  text-align: center;
  margin-top: 10%;
}
</style>

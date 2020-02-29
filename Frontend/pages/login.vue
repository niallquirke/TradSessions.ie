<template>
  <div class="body">
    <div class="login-wrapper">
      <div class="login">
        <h2 style="display:inline-block">So who's this now?</h2>
        <p v-show="directedFromCreate">
          You must be logged in to create events
        </p>
        <input v-model="isLogin" class="toggle" type="checkbox" />
        <form @submit.prevent="signupLogin">
          <label v-show="!isLogin" for="username">Username:</label>
          <BaseInput
            v-show="!isLogin"
            v-model="user.username"
            :class="{ error: $v.user.username.$error }"
            @blur="$v.user.username.$touch()"
            type="text"
            name="username"
          />
          <div v-if="$v.user.username.$error">
            <p v-if="!$v.user.username.required" class="errorMessage">
              Username is required.
            </p>
          </div>
          <label for="email">Email:</label>
          <BaseInput
            v-model="user.email"
            :class="{ error: $v.user.email.$error }"
            @blur="$v.user.email.$touch()"
            type="email"
            name="email"
          />
          <div v-if="$v.user.email.$error">
            <p v-if="!$v.user.email.required" class="errorMessage">
              Email is required.
            </p>
          </div>
          <label for="password">Password:</label>
          <BaseInput
            v-model="user.password"
            :class="{ error: $v.user.password.$error }"
            @blur="$v.user.password.$touch()"
            type="password"
            name="password"
          />
          <div v-if="$v.user.password.$error">
            <p v-if="!$v.user.password.required" class="errorMessage">
              Password is required.
            </p>
          </div>
          <label v-show="!isLogin" for="password2">Confirm Password:</label>
          <BaseInput
            v-show="!isLogin"
            v-model="pwd_conf"
            type="password"
            name="pwd_conf"
          />
          <BaseButton
            v-show="isLogin"
            type="submit"
            name="button"
            button-class="-fill-gradient"
            >Login</BaseButton
          >
          <BaseButton
            v-show="!isLogin"
            :disabled="$v.$anyError"
            type="submit"
            name="button"
            button-class="-fill-gradient"
            >Sign Up</BaseButton
          >
        </form>
        <p class="err">{{ error }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import { required } from 'vuelidate/lib/validators'
import UserService from '@/services/UserService.js'

export default {
  data() {
    return {
      user: {
        username: '',
        email: '',
        password: ''
      },
      isLogin: false,
      pwd_conf: '',
      error: null
    }
  },
  computed: {
    isRequired() {
      return !this.isLogin
    },
    ...mapState({
      directedFromCreate: (state) => state.user.directedFromCreate
    })
  },
  methods: {
    signupLogin() {
      if (this.isLogin) {
        this.$store
          .dispatch('user/login', this.user)
          .then((response) => {
            if (this.directedFromCreate) {
              this.$router.push({ path: '/event/create' })
            } else {
              this.$router.push({ path: '/profile' })
            }
          })
          .catch((err) => {
            this.error = err.response
          })
      } else if (this.user.password !== this.pwd_conf) {
        this.error = "The passwords you have entered don't match"
      } else {
        UserService.signup(this.user)
          .then((response) => {
            alert(
              'A verification email was sent to "' +
                this.user.email +
                '". Please click the link in the email to verify your account 😊'
            )
            this.isLogin = true
          })
          .catch((err) => {
            this.error = err.message
          })
      }
    }
  },
  validations: {
    user: {
      username: {},
      email: { required },
      password: { required }
    }
  }
}
</script>

<style scoped>
.login-wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
}
.login {
  width: 80%;
  text-align: center;
  margin-top: 2%;
}
.toggle {
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
  width: 100px;
  height: 32px;
  display: inline-block;
  position: relative;
  border-radius: 50px;
  overflow: hidden;
  outline: none;
  border: none;
  cursor: pointer;
  background-color: #84cf6a;
  transition: background-color ease 0.3s;
  margin-bottom: 15px;
}
.toggle:before {
  content: 'Login SignUp';
  display: block;
  position: absolute;
  z-index: 2;
  width: 28px;
  height: 28px;
  background: #fff;
  left: 2px;
  top: 2px;
  border-radius: 50%;
  font: 14px/30px Helvetica;
  text-transform: uppercase;
  font-weight: bold;
  text-indent: -53px;
  word-spacing: 40px;
  color: #fff;
  text-shadow: -1px -1px rgba(0, 0, 0, 0.15);
  white-space: nowrap;
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.2);
  transition: all cubic-bezier(0.3, 1.5, 0.7, 1) 0.3s;
}
.toggle:checked {
  background-color: #16c0b0;
}
.toggle:checked:before {
  left: 70px;
}
p {
  margin-top: -10px;
  margin-bottom: 20px;
}
.err {
  color: red;
  margin-top: 30px;
}
</style>

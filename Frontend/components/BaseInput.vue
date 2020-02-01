<template>
  <div class="field">
    <label v-if="label">{{ label }}</label>
    <input
      :value="value"
      v-on="listeners"
      @input="updateValue"
      v-bind="$attrs"
    />
  </div>
</template>

<script>
export default {
  inheritAttrs: false,
  props: {
    // eslint-disable-next-line vue/require-default-prop
    value: [String, Number],
    // eslint-disable-next-line vue/require-default-prop
    label: String
  },
  computed: {
    listeners() {
      return {
        ...this.$listeners,
        input: this.updateValue
      }
    }
  },
  methods: {
    updateValue(event) {
      this.$emit('input', event.target.value)
    }
  }
}
</script>

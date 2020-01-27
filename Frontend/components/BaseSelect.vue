<template>
  <div>
    <label v-if="label">{{ label }}</label>
    <select
      @change="updateValue"
      v-bind="$attrs"
      v-on="$listeners"
      style="border-radius: 10px"
    >
      <option></option>
      <option
        v-for="option in options"
        :value="option"
        :key="option.id"
        :selected="option === value"
        >{{ option }}</option
      >
    </select>
  </div>
</template>

<script>
export default {
  inheritAttrs: false,
  props: {
    options: {
      type: Array,
      required: true
    },
    // eslint-disable-next-line vue/require-default-prop
    value: [String, Number],
    // eslint-disable-next-line vue/require-default-prop
    label: String
  },
  methods: {
    updateValue() {
      this.$emit('input', event.target.value)
    }
  }
}
</script>

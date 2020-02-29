<template>
  <div class="icon-wrapper" :class="color">
    <svg :width="width" :height="height" class="icon">
      <use v-bind="{ href: '/feather-sprite.svg#' + name }" />
    </svg>
    <slot></slot>
  </div>
</template>

<script>
export default {
  name: 'Icon',
  props: {
    name: String,
    width: {
      type: [Number, String],
      default: 24
    },
    height: {
      type: [Number, String],
      default: 24
    },
    color: {
      type: String,
      default: 'grey'
    }
  }
}
</script>

<style scoped>
.icon-wrapper {
  display: inline-flex;
  align-items: center;
  font-size: 1rem;
  font-weight: 600;
}
.icon {
  stroke: currentColor;
  stroke-width: 2;
  stroke-linecap: round;
  stroke-linejoin: round;
  fill: none;
}
.grey {
  color: rgba(0, 0, 0, 0.4);
}
.green {
  color: #39b982;
}
</style>

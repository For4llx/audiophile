<template>
  <component :is="`h${level}`" class="heading">
    <slot />
  </component>
</template>

<script>
export default {
  name: 'BaseHeading',
  props: {
    level: String,
  },
};
</script>

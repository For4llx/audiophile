<template>
  <component :is="`h${level}`" class="heading heading--white">
    <slot />
  </component>
</template>

<script>
export default {
  name: 'BaseHeadingWhite',
  props: {
    level: String,
  },
};
</script>

<template>
  <ul class="showcase">
    <li class="showcase__item">
      <slot name="big" />
    </li>
    <li class="showcase__item">
      <slot name="small" />
    </li>
    <li class="showcase__item">
      <slot name="split" />
    </li>
  </ul>
</template>

<script>
export default {
  name: 'TheShowcase',
};
</script>

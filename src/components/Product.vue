<template>
  <article class="product">
    <h1 class="product__title">{{ title }}</h1>
    <p v-if="isNew" class="overline product__new">New product</p>
    <p class="product__description">{{ description }}</p>
    <button class="button subtitle product__button">See product</button>
  </article>
</template>

<script>
export default {
  name: 'Product',
  props: {
    isNew: Boolean,
    title: String,
    description: String,
  },
};
</script>

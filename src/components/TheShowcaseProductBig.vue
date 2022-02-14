<template>
  <BaseProduct class="showcase__product showcase__product--big">
    <div class="product__inner product__inner--centered">
      <BaseHeadingWhite class="product__heading--zx9" level="1">{{ title }}</BaseHeadingWhite>
      <BaseParagraphWhite class="product__description">{{ description }}</BaseParagraphWhite>
      <BaseButtonBlack>See Product</BaseButtonBlack>
    </div>
  </BaseProduct>
</template>

<script>
export default {
  name: 'TheShowcaseProductBig,',
  props: {
    title: String,
    description: String,
  },
};
</script>

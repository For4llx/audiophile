<template>
  <BaseProduct class="showcase__product showcase__product--split">
    <div class="product__inner product__inner--split">
      <BaseHeading level="4">{{ title }}</BaseHeading>
      <BaseButton>See Product</BaseButton>
    </div>
  </BaseProduct>
</template>

<script>
export default {
  name: 'TheShowcaseProductSplit,',
  props: {
    title: String,
  },
};
</script>

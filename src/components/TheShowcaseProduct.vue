<template>
  <BaseProduct class="showcase__product showcase__product--small">
    <div class="product__inner product__inner--small">
      <BaseHeading level="4">{{ title }}</BaseHeading>
      <BaseButton>See Product</BaseButton>
    </div>
  </BaseProduct>
</template>

<script>
export default {
  name: 'TheShowcaseProduct,',
  props: {
    title: String,
  },
};
</script>

<template>
  <BaseProduct class="header__product">
    <div class="product__inner product__inner--centered">
      <BaseOverline v-if="isNew" class="product__overline overline--white">
        New product
      </BaseOverline>
      <BaseHeadingWhite class="heading--wide" level="1">{{ title }}</BaseHeadingWhite>
      <BaseParagraphWhite class="product__description">{{ description }}</BaseParagraphWhite>
      <BaseButtonPrimary>See Product</BaseButtonPrimary>
    </div>
  </BaseProduct>
</template>

<script>
export default {
  name: 'HeaderProduct,',
  props: {
    isNew: Boolean,
    title: String,
    description: String,
  },
};
</script>

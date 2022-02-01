<template>
  <header class="header">
    <div class="wrapper wrapper--header header__wrapper">
      <NavBar />
      <Product
        isNew
        title="XX99 Mark II Headphones"
        description="Experience natural, lifelike audio and excep
        tional build quality made for the passionate music enthusiast."
      />
    </div>
  </header>
  <main class="home">
    <div class="wrapper home__wrapper">
      <NavCategory />
    </div>
  </main>
</template>

<script>
import NavBar from '../components/NavBar.vue';
import Product from '../components/Product.vue';
import NavCategory from '../components/NavCategory.vue';

export default {
  name: 'App',
  components: {
    NavBar,
    Product,
    NavCategory,
  },
};
</script>

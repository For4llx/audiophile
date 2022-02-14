<template>
  <!--eslint-disable max-len -->
  <Header>
    <HeaderNavigation />
    <HeaderProduct
      isNew
      title="XX99 Mark II Headphones"
      description="Experience natural, lifelike audio and except ional build quality made for the passionate music enthusiast."
    />
  </Header>
  <Home>
    <HomeCategories />
    <TheShowcase>
      <template v-slot:big>
        <TheShowcaseProductBig
          title="ZX9 SPEAKER"
          description="Upgrade to premium speakers that are phenomenally built to deliver truly remarkable sound."
        />
      </template>
      <template v-slot:small>
        <TheShowcaseProduct title="ZX7 SPEAKER" />
      </template>
      <template v-slot:split>
        <TheShowcaseProductSplit title="YX1 EARPHONES" />
      </template>
    </TheShowcase>
    <HomeAbout />
  </Home>
  <TheFooter />
</template>

<script>
import Header from '../components/Header.vue';
import HeaderNavigation from '../components/HeaderNavigation.vue';
import HeaderProduct from '../components/HeaderProduct.vue';
import Home from '../components/Home.vue';
import HomeCategories from '../components/HomeCategories.vue';
import HomeAbout from '../components/HomeAbout.vue';
import TheShowcase from '../components/TheShowcase.vue';
import TheShowcaseProductBig from '../components/TheShowcaseProductBig.vue';
import TheShowcaseProduct from '../components/TheShowcaseProduct.vue';
import TheShowcaseProductSplit from '../components/TheShowcaseProductSplit.vue';
import TheFooter from '../components/TheFooter.vue';

export default {
  name: 'HomePage',
  components: {
    Header,
    HeaderNavigation,
    HeaderProduct,
    Home,
    HomeCategories,
    HomeAbout,
    TheShowcase,
    TheShowcaseProduct,
    TheShowcaseProductBig,
    TheShowcaseProductSplit,
    TheFooter,
  },
};
</script>

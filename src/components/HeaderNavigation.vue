<template>
  <BaseNavigation class="header__navigation">
    <img src="../assets/shared/large/logo.svg" alt="audiophile" class="navigation__logo" />
    <div class="toggle navigation__toggle">
      <button class="hamburger">
        <img src="../assets/shared/medium/icon-hamburger.svg" />
      </button>
      <BaseMenu class="toggle__menu">
        <ul class="menu__inner menu__inner--toggle">
          <li class="menu__item"><router-link to="/" class="link">Home</router-link></li>
          <li class="menu__item">
            <router-link to="/headphones" class="link">Headphones</router-link>
          </li>
          <li class="menu__item">
            <router-link to="/speakers" class="link">Speakers</router-link>
          </li>
          <li class="menu__item">
            <router-link to="/earphones" class="link">Earphones</router-link>
          </li>
        </ul>
      </BaseMenu>
    </div>

    <button class="navigation__cart">
      <img src="../assets/shared/large/icon-cart.svg" alt="cart" />
    </button>
  </BaseNavigation>
</template>

<script>
export default {
  name: 'HeaderNavigation',
};
</script>

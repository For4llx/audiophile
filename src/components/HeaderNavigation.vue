<template>
  <BaseNavigation class="header__navigation">
    <img src="../assets/shared/large/logo.svg" alt="audiophile" class="navigation__logo" />
    <div class="toggle navigation__toggle">
      <button class="hamburger">
        <img src="../assets/shared/medium/icon-hamburger.svg" />
      </button>
      <BaseMenu class="toggle__menu">
        <ul class="menu__inner menu__inner--toggle">
          <li class="menu__item"><a class="link">Home</a></li>
          <li class="menu__item"><a class="link">Headphones</a></li>
          <li class="menu__item"><a class="link">Speakers</a></li>
          <li class="menu__item"><a class="link">Earphones</a></li>
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

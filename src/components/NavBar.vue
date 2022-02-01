<template>
  <div class="navbar">
    <img class="navbar__logo" src="../assets/shared/large/logo.svg" alt="logo" />
    <div class="menu navbar__menu">
      <button class="menu__hamburger">
        <img src="../assets/shared/medium/icon-hamburger.svg" alt="menu" />
      </button>
      <nav class="menu__nav">
        <ul class="menu__ul">
          <li><a class="menu__link">Home</a></li>
          <li><a class="menu__link">Headphones</a></li>
          <li><a class="menu__link">Speakers</a></li>
          <li><a class="menu__link">Earphones</a></li>
        </ul>
      </nav>
    </div>
    <button class="navbar__cart">
      <img src="../assets/shared/large/icon-cart.svg" alt="cart" />
    </button>
  </div>
</template>

<script>
export default {
  name: 'NavBar',
};
</script>

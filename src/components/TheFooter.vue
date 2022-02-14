<template>
  <footer class="footer">
    <div class="footer__inner">
      <BaseNavigation class="footer__navigation navigation--borderless">
        <img src="../assets/shared/large/logo.svg" alt="audiophile" class="navigation__logo" />
        <BaseMenu class="navigation__menu">
          <ul class="menu__inner menu--column">
            <li class="menu__item"><a class="link">Home</a></li>
            <li class="menu__item"><a class="link">Headphones</a></li>
            <li class="menu__item"><a class="link">Speakers</a></li>
            <li class="menu__item"><a class="link">Earphones</a></li>
          </ul>
        </BaseMenu>
      </BaseNavigation>
      <div class="footer__about">
        <BaseParagraph class="footer__paragraph body--white">
          Audiophile is an all in one stop to fulfill your audio needs. We're a small team of music
          lovers and sound specialists who are devoted to helping you get the most out of personal
          audio. Come and visit our demo facility - we’re open 7 days a week.
        </BaseParagraph>
        <BaseSocial class="social--about" />
      </div>
      <div class="footer__copyright">
        <BaseParagraph class="body--white body--bold">
          Copyright 2021. All Rights Reserved
        </BaseParagraph>
        <BaseSocial class="social--copyright" />
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  name: 'TheFooter',
};
</script>

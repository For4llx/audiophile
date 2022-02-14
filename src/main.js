import { createApp } from 'vue';
import App from './App.vue';
import store from './store';

import BaseButton from './components/BaseButton.vue';
import BaseButtonBlack from './components/BaseButtonBlack.vue';
import BaseButtonPrimary from './components/BaseButtonPrimary.vue';
import BaseIcon from './components/BaseIcon.vue';
import BaseIconFacebook from './components/BaseIconFacebook.vue';
import BaseIconTwitter from './components/BaseIconTwitter.vue';
import BaseIconInstagram from './components/BaseIconInstagram.vue';
import BaseParagraph from './components/BaseParagraph.vue';
import BaseParagraphWhite from './components/BaseParagraphWhite.vue';
import BaseHeading from './components/BaseHeading.vue';
import BaseHeadingWhite from './components/BaseHeadingWhite.vue';
import BaseOverline from './components/BaseOverline.vue';
import BaseMenu from './components/BaseMenu.vue';
import BaseProduct from './components/BaseProduct.vue';
import BaseNavigation from './components/BaseNavigation.vue';
import BaseCategories from './components/BaseCategories.vue';
import BaseAbout from './components/BaseAbout.vue';
import BaseSocial from './components/BaseSocial.vue';

const app = createApp(App);

app.component('BaseButton', BaseButton);
app.component('BaseButtonBlack', BaseButtonBlack);
app.component('BaseButtonPrimary', BaseButtonPrimary);
app.component('BaseIcon', BaseIcon);
app.component('BaseIconFacebook', BaseIconFacebook);
app.component('BaseIconTwitter', BaseIconTwitter);
app.component('BaseIconInstagram', BaseIconInstagram);
app.component('BaseParagraph', BaseParagraph);
app.component('BaseParagraphWhite', BaseParagraphWhite);
app.component('BaseHeading', BaseHeading);
app.component('BaseHeadingWhite', BaseHeadingWhite);
app.component('BaseOverline', BaseOverline);
app.component('BaseMenu', BaseMenu);
app.component('BaseProduct', BaseProduct);
app.component('BaseNavigation', BaseNavigation);
app.component('BaseCategories', BaseCategories);
app.component('BaseAbout', BaseAbout);
app.component('BaseSocial', BaseSocial);

app.use(store).mount('#app');

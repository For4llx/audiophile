const template = document.createElement('template');
template.innerHTML = /* html */`
<style type="text/css">
@import "static/website/css/dist/main.css";
</style>
<button id="decrement" class="subtitle subtitle--opacity-25 counter__item counter__item--button">-</button>
<input type="text" id="count" class="subtitle counter__number counter__item"></p>
<button id="increment" class="subtitle subtitle--opacity-25 counter__item counter__item--button">+</button>
`;
export class CounterButton extends HTMLElement {
    constructor() {
        super();
        this.count = this.dataset.value;
        this.attachShadow({ mode: 'open' });
    }
    connectedCallback() {
        this.shadowRoot.appendChild(template.content.cloneNode(true));
        this.shadowRoot.getElementById('increment').onclick = () => this.handleClickIncrement();
        this.shadowRoot.getElementById('decrement').onclick = () => this.handleClickDecrement();
        this.update(this.count);
    }

    update() {
        this.shadowRoot.getElementById('count').value = this.count;
        this.innerHTML = /* html */`<input type="hidden" name="quantity" value="${this.count}"/>`;
    }

    handleClickIncrement() {
        this.update(this.count++);
    }

    handleClickDecrement() {
        if (this.count > 1) {
            this.update(this.count--);
        }
    }

}

customElements.define('counter-button', CounterButton);

const template = document.createElement('template');
template.innerHTML = /* html */`
    <style type="text/css">
        @import "static/website/css/dist/main.css";
    </style>
    <button id="decrement" class="subtitle subtitle--opacity-25 counter__item counter__item--button">-</button>
    <p id="count" class="subtitle counter__number counter__item"></p>
    <button id="increment" class="subtitle subtitle--opacity-25 counter__item counter__item--button">+</button>
`;
export class CounterButton extends HTMLElement {
    constructor() {
        super();
        this.count = 0;
        this.attachShadow({ mode: 'open' });
    }

    connectedCallback() {
        this.shadowRoot.appendChild(template.content.cloneNode(true));
        this.shadowRoot.getElementById('increment').onclick = () => this.handleClickIncrement();
        this.shadowRoot.getElementById('decrement').onclick = () => this.handleClickDecrement();
        this.update(this.count);
    }

    update() {
        this.shadowRoot.getElementById('count').innerText = this.count;
        this.shadowRoot.getElementById('count-input').value = this.count;
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
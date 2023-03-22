export class CounterButton extends HTMLElement {
    constructor() {
        super();
        this.count = 1;
    }
    connectedCallback() {
        document.getElementById(`increment-button-${this.id}`).onclick = () => this.handleClickIncrement(this.id);
        document.getElementById(`decrement-button-${this.id}`).onclick = () => this.handleClickDecrement(this.id);
    }

    handleClickIncrement(id) {
        this.count++;
        document.getElementById(`counter-text-${id}`).innerText = this.count;
        document.getElementById(`counter-value-${id}`).value = this.count;
    }

    handleClickDecrement(id) {
        if (this.count > 1) {
            this.count--;
            document.getElementById(`counter-text-${id}`).innerText = this.count;
            document.getElementById(`counter-value-${id}`).value = this.count;
        }
    }
}

customElements.define('counter-button', CounterButton);

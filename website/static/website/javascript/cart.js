export class CartButton extends HTMLElement {
    constructor() {
        super();
        let is_open = false;
        this.addEventListener('click', this.handleClick)
    }
    handleClick(event) {
        if (!this.is_open) {
            document.getElementById("cart").style.display = "flex";
            this.is_open = true;
        }
        else {
            document.getElementById("cart").style.display = "none";
            this.is_open = false;
        }
    }
}

window.customElements.define("cart-button", CartButton);

export class HamburgerButton extends HTMLElement {
    constructor() {
        super();
        let is_open = false;
        this.addEventListener('click', this.handleClick)
    }
    handleClick(event) {
        if (!this.is_open) {
            document.getElementById("menu").style.display = "block";
            this.is_open = true
        }
        else {
            document.getElementById("menu").style.display = "none";
            this.is_open = false;
        }
    }
}

window.customElements.define("hamburger-button", HamburgerButton);

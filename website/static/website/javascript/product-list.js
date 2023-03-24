export class ProductListButton extends HTMLElement {
    constructor() {
        super();
        document.getElementsByClassName("listButton").is_open = false;
        this.addEventListener('click', this.handleClick)
    }
    handleClick(event) {
        if (!document.getElementsByClassName("listButton").is_open) {
            document.getElementById("product-list").style.display = "flex";
            document.getElementsByClassName("listButton").is_open = true;
            document.getElementById("list-button-plus").style.display = "none";
        }
        else {
            document.getElementById("product-list").style.display = "none";
            document.getElementsByClassName("listButton").is_open = false;
            document.getElementById("list-button-plus").style.display = "block";
        }
    }
}

window.customElements.define("product-list-button", ProductListButton);

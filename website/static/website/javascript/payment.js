export class PaymentCheckBox extends HTMLElement {
    constructor() {
        super();
        document.getElementById('id_payment_method_0').addEventListener('change', this.handleChange);
        document.getElementById('id_payment_method_1').addEventListener('change', this.handleChange);
    }
    handleChange(event) {
        if (document.getElementById('id_payment_method_0').checked) {
            document.getElementById('emoney-input_0').style.display = "flex";
            document.getElementById('emoney-input_1').style.display = "flex";
            document.getElementById('onDelivery').style.display = "none";

        }
        if (document.getElementById('id_payment_method_1').checked) {
            document.getElementById('emoney-input_0').style.display = "none";
            document.getElementById('emoney-input_1').style.display = "none";
            document.getElementById('onDelivery').style.display = "flex";
        }
    }
}

window.customElements.define("payment-checkbox", PaymentCheckBox);


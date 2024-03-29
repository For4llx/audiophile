import { CartButton } from "./cart.js";
import { HamburgerButton } from "./hamburger.js";
import { CounterButton } from "./counter.js";
import { PaymentCheckBox } from "./payment.js";
import { ProductListButton } from "./product-list.js";

function uuidv4() {
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function (c) {
        var r = Math.random() * 16 | 0, v = c == 'x' ? r : (r & 0x3 | 0x8);
        return v.toString(16);
    });
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

let device = getCookie('device')

if (device == null || device == undefined) {
    device = uuidv4()
}

document.cookie = `device=${device};domain=;path=/`


// form validation
const form = document.querySelector("#form");
const firstName = document.querySelector("#firstName");
const lastName = document.querySelector("#lastName");
const password = document.querySelector("#password");
const email = document.querySelector("#email");
const address = document.querySelector("#address");
const city = document.querySelector("#city");
const zipCode = document.querySelector("#zipCode");
const phoneNumber = document.querySelector("#phoneNumber");
const submit = document.querySelector("#submit");

zipCode.addEventListener("input", function(e) {
    if(/^\d{5}(-\d{4})?$/.test(this.value)) {
        this.style.border = "2px solid green";
    } else {
        this.style.border = "2px solid red";
    }

})

phoneNumber.addEventListener("input", function(e) {
    if(/^(\([0-9]{3}\) |[0-9]{3}-)[0-9]{3}-[0-9]{4}$/.test(this.value)) {
        this.style.border = "2px solid green";
    } else {
        this.style.border = "2px solid red";
    }
})




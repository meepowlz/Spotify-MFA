/*
JavaScript for mobile number input from
https://www.twilio.com/blog/international-phone-number-input-html-javascript
JavaScript for mobile number validation from
https://www.twilio.com/blog/validate-phone-number-input
*/

const phoneInputField = document.querySelector("#mobile_number");
const phoneInput = window.intlTelInput(phoneInputField, {
   preferredCountries: ["us", "gb", "mx", "ca", "au"],
   utilsScript:
   "https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/17.0.8/js/utils.js",
});

const info = document.querySelector(".alert-info");
const error = document.querySelector(".alert-error");

function process(event) {

    event.preventDefault();

    var form = new FormData(event.target);
    var data = Object.fromEntries(form);

    const phoneNumber = phoneInput.getNumber();

    if (phoneInput.isValidNumber()){
        /* Displays confirmation message
        info.style.display = "";
        info.innerHTML = `Phone number in E.164 format: <strong>${phoneNumber}</strong>`;
         */

        // Submits the formatted phone number
        data["mobile_number"] = phoneNumber;
        fetch("http://localhost:8080/register", {
            method: "POST",
            body: JSON.stringify(data),
            headers: {"Content-Type": "application/json"}
        }).then(response => {
            response.json().then(data => {  // parse JSON
                const success = data.success
                const errorMessage = data.error
                if (success === true) {  // redirect if registration was successful
                    location.assign("http://localhost:8080/authenticate")
                } else {  // display an error if registration was not successful
                    error.style.display = "";
                    error.innerHTML = errorMessage
                }
            })
        }).catch(error => {
            error.innerHTML = "Something went wrong :( Try again later."
        })
    } else {
        // Displays error message
        error.style.display = "";
        error.innerHTML = "Invalid phone number"
    }


}

var formElement = document.querySelector("form");
formElement.addEventListener("submit", process);


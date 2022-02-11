/*
Handles submission of login credentials
using fetch API
 */

const error = document.querySelector(".alert-error");

function process(event) {

    event.preventDefault();

    let form = new FormData(event.target);
    let data = Object.fromEntries(form);

    fetch("http://localhost:8080/login", {
        method: "POST",
        body: JSON.stringify(data),
        headers: {"Content-Type": "application/json"}
    }).then(response => {
        response.json().then(data => {  // parse JSON
                const success = data.success
                const errorMessage = data.error
                if (success === true) {  // redirect if login was successful
                    location.assign("http://localhost:8080/authenticate")
                } else {  // display an error if login was not successful
                    error.style.display = "";
                    error.innerHTML = errorMessage
                }
            })
        }).catch(error => {
            error.innerHTML = "Something went wrong :( Try again later."
        })
}

let formElement = document.querySelector("form");
formElement.addEventListener("submit", process);


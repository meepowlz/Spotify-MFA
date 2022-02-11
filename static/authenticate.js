 /* Handles code submission & error display
 Allows code to be resent
 */

    function resend() {
        let error = document.getElementById("error-message-resend")
        fetch("http://localhost:8080/resend-code", {
            method: "POST",
        }).then(response => {
        response.json().then(data => {  // parse JSON
                const success = data.success
                const errorMessage = data.error
                if (success === false) {  // redirect if login was successful
                    error.style.display = "";
                    error.innerHTML = errorMessage
                }
            })
        }).catch(error => {
            error.style.display = "";
            error.innerHTML = "Unable to resend code"
        })
    }
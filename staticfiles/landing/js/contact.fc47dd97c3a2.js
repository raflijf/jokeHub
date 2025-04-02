const form = document.getElementById("myForm");
const emailInput = document.getElementById("id_email");
const messageInput = document.getElementById("id_pesan");
const alertEmail = document.getElementById("alert-email");
const alertMessage = document.getElementById("alert-message");

form.addEventListener("submit", function (event) {
    let isValid = true;

    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailPattern.test(emailInput.value.trim())) {
        alertEmail.classList.remove("hidden");
        isValid = false;
    } else {
        alertEmail.classList.add("hidden");
    }

    if (messageInput.value.trim() === "") {
        alertMessage.classList.remove("hidden");
        isValid = false;
    } else {
        alertMessage.classList.add("hidden");
    }

    if (!isValid) {
        event.preventDefault(); 
    } 
});

const closeAlertTag = document.getElementById('close-alert')
const alertTag =  document.getElementById('alert')
closeAlertTag.addEventListener('click', () => alertTag.remove())



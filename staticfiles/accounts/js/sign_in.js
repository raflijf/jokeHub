const fields = document.querySelectorAll('.field')
const alerts = document.querySelectorAll('.alert')
const form = document.getElementById('form')

form.addEventListener('submit', event => {
    fields.forEach((e,i) => {
        if (e.value === '') {
            alerts[i].style.display = 'flex'
            event.preventDefault()
        } else {
            alerts[i].style.display = 'none'
            localStorage.setItem('email', fields[0].value)
        }
    })
})

const showPassword = document.getElementById('show-password')
showPassword.addEventListener('change', function () {
    fields[1].type = (this.checked) ? 'text' : 'password' 
})
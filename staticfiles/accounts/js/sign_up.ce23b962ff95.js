const showPassword = document.querySelectorAll('.show-password')
const inputPassword = document.querySelectorAll('.input-password')
showPassword.forEach((e, i) => {
    e.addEventListener('change', function () {
        inputPassword[i].type = this.checked ? 'text' : 'password'
    })
})

const alertPassword = document.getElementsByClassName('alert-password')[0]
const signupForm = document.getElementById('signup-form')
const fields = document.querySelectorAll('.field')
const Alert = document.querySelectorAll('.alert')
signupForm.addEventListener('submit', (form) => {
    fields.forEach((e,i) => {
        if (e.value === '') {
            Alert[i].style.display = 'flex'
            form.preventDefault()
        } else {
            Alert[i].style.display = 'none'     
            localStorage.setItem('email', fields[0].value)
        }

        const password1 = fields[2].value
        const password2 = fields[3].value
        if (password1 !== '' && password2 !== '') {
            if (password1 !== password2) {
                Alert[3].style.display = 'flex'
                alertPassword.textContent = '• Kedua password tidak sama'
                form.preventDefault()
               console.log('dk samo') 
            } else if ((password1 === password2) && password1.length < 8  ) {
                Alert[3].style.display = 'flex'
                alertPassword.textContent = '• Password minimal 8 karakter'
                form.preventDefault()
            } else {
                Alert[3].style.display = 'none'
                localStorage.setItem('email', fields[0].value)
            }
        }

    })
})

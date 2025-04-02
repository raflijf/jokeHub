const form = document.getElementById('form')
const button  = document.getElementById('submitButton')
const fields = document.querySelectorAll('.field')
const minLengthValidatePassword = document.getElementById('minLengthValidatePassword')

fields[1].addEventListener('input',  function () {
    (this.value.length >= 8 ) ? minLengthValidatePassword.classList.add('text-green-600') : minLengthValidatePassword.classList.remove('text-green-600')
})
fields.forEach(field => {
    field.addEventListener('input' ,  function () {
        const isAllValid = [...fields].every(f => f.value !== '' && f.value.length >= 8) 
        if (isAllValid) {
            console.log('paca nahh')
            button.removeAttribute('disabled')
            button.classList.remove('opacity-60')
        } else {
            console.log('dk acak')
            button.setAttribute('disabled', '')
            button.classList.add('opacity-60')
        }
    })
})

const fields = document.querySelectorAll('.field')

fields[2].addEventListener('input', function () {document.getElementById('lengthName').innerHTML = this.value.length })
document.getElementById('lengthName').innerHTML = fields[2].value.length
fields[3].addEventListener('input', function () {document.getElementById('lengthBio').innerHTML = this.value.length })
document.getElementById('lengthBio').innerHTML = fields[3].value.length

const message = document.getElementById('message')
const closeButton = document.getElementById('closeButton')


const input_pic = document.getElementById('id_profile_image');
const photo_profile = document.getElementById('photo_profil');

input_pic.addEventListener('change', function () {
    const file = this.files[0]
    if (file) {
        const reader = new FileReader()
        reader.onload = function (e) {
            photo_profile.src = e.target.result
        }
        reader.readAsDataURL(file)
        console.log(file)
    }
})

if (message) closeButton.addEventListener('click', () => message.remove())















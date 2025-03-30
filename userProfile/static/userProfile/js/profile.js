// alert('shdsjifhui')
const copyButton = document.getElementById('copyButton')
const path = document.getElementById('path')


copyButton.addEventListener('click', () => {
    navigator.clipboard.writeText(path.textContent)
        .then(() => {
            copyButton.innerHTML = '<h1 class="text-white "> Copied</h1> '
            setTimeout(() => {
                copyButton.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="white"><path d="M360-240q-33 0-56.5-23.5T280-320v-480q0-33 23.5-56.5T360-880h360q33 0 56.5 23.5T800-800v480q0 33-23.5 56.5T720-240H360Zm0-80h360v-480H360v480ZM200-80q-33 0-56.5-23.5T120-160v-560h80v560h440v80H200Zm160-240v-480 480Z"/></svg>'
            }, 2000)
        })
        .catch(error => {
            copyButton.innerHTML = '<h1 class="text-white "> Fail</h1> '
            setTimeout(() => {
                copyButton.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960" width="24px" fill="white"><path d="M360-240q-33 0-56.5-23.5T280-320v-480q0-33 23.5-56.5T360-880h360q33 0 56.5 23.5T800-800v480q0 33-23.5 56.5T720-240H360Zm0-80h360v-480H360v480ZM200-80q-33 0-56.5-23.5T120-160v-560h80v560h440v80H200Zm160-240v-480 480Z"/></svg>'
            }, 2000)
        })
})

document.querySelectorAll('.follower')
    .forEach(item => {
        const delelteButton = item.querySelector('.deleteFollower')
        delelteButton.addEventListener('submit',async function (event) {
            event.preventDefault()
            try  {
                const response = await fetch(this.action, {
                    method : 'POST',
                    body : new FormData(this)
                })  
                console.log(item)
            } catch (error) {
                console.log(error)
            }
        })
    })

const react = document.querySelectorAll('.react')
let csrftoken = document.querySelector('meta[name="csrf-token"]').content;

react.forEach(item => {
    item.addEventListener('click', async function () {
        try {
            await fetch(this.value, {
                method : 'POST',
                headers : {
                    'X-CSRFToken': csrftoken
                }
            })
            location.reload()
        } 
        catch (error) {
            console.log(error)
        }
    })
})




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
// alert('sdsdsd')

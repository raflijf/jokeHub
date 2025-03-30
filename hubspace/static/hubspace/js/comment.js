const  user_comment = document.querySelectorAll('.user_comment')
const csrftoken = document.querySelector('meta[name="csrf-token"]').content;
user_comment.forEach(item => {
    const deleteComment = item.querySelector(`.delete_comment`)
    if (deleteComment) {
        deleteComment.addEventListener('click', async function () {
            try {
                await fetch(this.value, {
                    method : 'POST',
                    headers : {
                        'X-CSRFToken': csrftoken
                    }
                }) 
                item.remove()
            } catch (error) {
                console.log(error)
            }
        })   
    }
})

const formCommnet = document.querySelector('form')
formCommnet.querySelector('textarea').addEventListener('input', function () {
    if (this.value) {
        formCommnet.querySelector('button').removeAttribute('disabled')
    } else {
        formCommnet.querySelector('button').setAttribute('disabled', '')
    }
})



const categories_list = document.querySelectorAll('#categories-list span');
const inputCategory = document.getElementById('inputCategory')
let a = ''
categories_list.forEach(e => {
    e.addEventListener('click', function () {
        const chosen = [...categories_list].find(item => item.getAttribute('data-chosen') === 'true');

        if (this.getAttribute('data-chosen') === 'false') {
            if (chosen) {
                chosen.setAttribute('data-chosen', 'false');
                chosen.classList.remove('bg-primary-navyblue');
                chosen.classList.replace('text-white','text-primary-navyblue')
            }
            this.setAttribute('data-chosen', 'true');
            this.classList.add('bg-primary-navyblue');
            this.classList.replace('text-primary-navyblue','text-white')
            inputCategory.value = this.textContent
            a = 'ado'
        } else {
            this.setAttribute('data-chosen', 'false');
            this.classList.remove('bg-primary-navyblue');
            this.classList.replace('text-white','text-primary-navyblue')
            inputCategory.value = ''
            a = 'tek'
        }

    });
});

const postForm = document.getElementById('postForm')
const errorMessage = document.getElementById('errorMessage')
const contentPost = document.getElementById('contentPost')
const submitButton = document.getElementById('submitButton')

postForm.addEventListener('submit', function (e) {
    if (contentPost.value === '' || inputCategory.value === '') {
        e.preventDefault()
        if (contentPost.value === '') {
            contentPost.classList.replace('border-primary-navyblue', 'border-red-600');
        } else {
            contentPost.classList.replace('border-red-600', 'border-primary-navyblue');
        }

        if (inputCategory.value === '') {
            errorMessage.classList.remove('hidden')
        } else {
            errorMessage.classList.add('hidden')
        }
    } 
})

contentPost.addEventListener('input', function () {
    document.getElementById('currentWord').textContent = this.value.length
})

const categoryField = document.getElementById('categoryField')
const UIcategoryField = document.getElementById('UIcategoryField')
const addCategoryForm = document.getElementById('addCategoryForm')

UIcategoryField.addEventListener('input', function ()  {
    categoryField.value = this.value
})

const data_list_category = [...categories_list].map(e => e.textContent.toLowerCase().replace(' ', ''))

addCategoryForm.addEventListener('submit', e => {
    if (!UIcategoryField.value ||  data_list_category.includes(UIcategoryField.value.toLowerCase().replace(/\s/g,''))) {
        e.preventDefault()
        console.log('dk boleh kosong kalo nak nambahke kategori')
    } 
})



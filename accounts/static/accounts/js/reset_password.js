const emailField = document.getElementById('email'); 
emailField.value = localStorage.getItem('email') || ''; 

const form = document.getElementById('form'); 
const Alert = document.getElementById('alert');

const isValidEmail = (email) => {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email); 
};

form.addEventListener('submit', function (e) {
    const email = emailField.value.trim(); 

    if (email === '') {
        Alert.textContent = "Email tidak boleh kosong!";
        Alert.classList.remove('hidden');
        e.preventDefault(); 
    } else if (!isValidEmail(email)) {
        Alert.textContent = "Format email tidak valid!";
        Alert.classList.remove('hidden');
        e.preventDefault(); 
    } else {
        Alert.classList.add('hidden');
        localStorage.setItem('email', email); 
    }
});

const hamburger = document.querySelector('.hamburger');
const mobileMenu = document.querySelector('.mobile-menu');

hamburger.addEventListener('click', (e) => {
    e.stopPropagation();
    mobileMenu.classList.toggle('hidden');
});

document.addEventListener('click', (e) => {
    if (!e.target.closest('nav')) {
        mobileMenu.classList.add('hidden');
    }
});

window.addEventListener('resize', () => {
    if (window.innerWidth > 768) {
        mobileMenu.classList.add('hidden');
    }
});

window.addEventListener('scroll', () => {
    const navTag = document.getElementById('nav');
    if (window.scrollY > 5) {
        navTag.classList.add('shadow-md');
    } else {
        navTag.classList.remove('shadow-md');
    }
});
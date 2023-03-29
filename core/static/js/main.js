// Mobile nav
mobileNavBtn = document.getElementById('mobileNavBtn');
mobileNav = document.getElementById('mobileNav');

function openNav() {
    mobileNav.classList.toggle('mobile__nav-active');
    mobileNavBtn.classList.toggle('toggle');
}

mobileNavBtn.addEventListener('click', openNav);

// spinner

spinner = document.querySelector('.preloader__wrapper');


window.addEventListener("load", () => {
    spinner.style.display = 'none';
})

// Close flash

closeFlash = document.getElementById('flash__close-svg');
flashMessage = document.getElementById('flash-message');

if (document.body.contains(flashMessage)){
    closeFlash.addEventListener('click', () => {
        flashMessage.style.display = 'none';
    });
}



// Mobile nav
mobileNavBtn = document.getElementById('mobileNavBtn');
mobileNav = document.getElementById('mobileNav');

function openNav() {
    mobileNav.classList.toggle('mobile__nav-active');
    triggerSrc = mobileNavBtn.getAttribute('src');
    if (triggerSrc == '/static/icons/bars-solid.svg') {
        mobileNavBtn.setAttribute('src', '/static/icons/menu_close.svg');
        mobileNavBtn.classList.add('open')
        mobileNavBtn.classList.remove('closed')
    } else {
        mobileNavBtn.setAttribute('src', '/static/icons/bars-solid.svg');
        mobileNavBtn.classList.remove('open')
        mobileNavBtn.classList.add('closed')
    }
}

console.log(mobileNavBtn.getAttribute('src'))
mobileNavBtn.addEventListener('click', openNav);


// Close flash

closeFlash = document.getElementById('flash__close-svg');
flashMessage = document.getElementById('flash-message');

if (document.body.contains(flashMessage)){
    closeFlash.addEventListener('click', () => {
        flashMessage.style.display = 'none';
    });
}



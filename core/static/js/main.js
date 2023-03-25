// Mobile nav
mobileNavBtn = document.getElementById('mobileNavBtn');
mobileNav = document.getElementById('mobileNav');

function openNav() {
    mobileNav.classList.toggle('mobile__nav-active');
    mobileNavBtn.classList.toggle('toggle');
}

mobileNavBtn.addEventListener('click', openNav);



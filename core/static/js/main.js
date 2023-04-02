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


// side items in on scroll
const sliders = document.querySelectorAll(".slider");

appearOptions = {
  rootMargin: "-80px 0px -80px 0px",
  threshold: 0,
};

const appearOnScroll = new IntersectionObserver((entries, appearOnScroll) => {
  entries.forEach((entry) => {
    if (!entry.isIntersecting) {
      entry.target.classList.remove("appear"); 
      return;
    } else {
      entry.target.classList.add("appear");
      appearOnScroll.unobserve(entry.target);
    }
  });
}, appearOptions);
sliders.forEach((slider) => {
  appearOnScroll.observe(slider);
});

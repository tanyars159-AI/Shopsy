let currentSlide = 0;
const slides = document.querySelectorAll('.hero');
const slider = document.querySelector('.slider');
const totalSlides = slides.length;

function showSlide(index) {
    slider.style.transform = `translateX(-${index * 100}%)`;
}

function nextSlide() {
    currentSlide = (currentSlide + 1) % totalSlides;
    showSlide(currentSlide);
}

// Auto-slide every 4 seconds
setInterval(nextSlide, 4000);

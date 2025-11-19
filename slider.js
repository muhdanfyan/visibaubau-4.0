let slideIndex = 0;

function moveSlide(n) {
    const slides = document.querySelectorAll(".slide");
    slideIndex += n;
    if (slideIndex > slides.length - 1) {
        slideIndex = 0;
    }
    if (slideIndex < 0) {
        slideIndex = slides.length - 1;
    }
    const offset = -slideIndex * 100;
    document.querySelector(".slider").style.transform = `translateX(${offset}%)`;
}
// JavaScript for SIMKES Slideshow
let slideIndex = 1; // Start with the first slide

function showSlides(n) {
    let i;
    let slides = document.getElementsByClassName("mySlides");
    let dots = document.getElementsByClassName("dot");

    if (n > slides.length) {
        slideIndex = 1;
    }
    if (n < 1) {
        slideIndex = slides.length;
    }

    // Hide all slides
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }

    // Deactivate all dots
    for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active", "");
    }

    // Display the current slide and activate the corresponding dot
    if (slides.length > 0) {
        let currentSlideElement = slides[slideIndex - 1];
        currentSlideElement.style.display = "block";
        dots[slideIndex - 1].className += " active";

        // Lazy load the image for the current slide
        let img = currentSlideElement.querySelector('img');
        if (img && img.dataset.src) {
            img.src = img.dataset.src;
            img.removeAttribute('data-src');
        }
    }
}

// Next/previous controls
function plusSlides(n) {
    showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
    showSlides(slideIndex = n);
}

// Initialize slideshow on page load
document.addEventListener("DOMContentLoaded", function() {
    if (document.getElementsByClassName("mySlides").length > 0) {
        showSlides(slideIndex); // Display the first slide
    }
});

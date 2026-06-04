document.addEventListener('DOMContentLoaded', () => {
    let currentSlide = 0;
    const slides = document.querySelectorAll('.slide');
    const totalSlides = slides.length;
    const slideCounter = document.querySelector('.slide-counter');
    const progressBar = document.querySelector('.progress-bar-inner');

    function updateUI(index) {
        // Update slide counter
        if (slideCounter) {
            slideCounter.textContent = `Slide ${index + 1} / ${totalSlides}`;
        }

        // Update progress bar
        if (progressBar) {
            const progressPercentage = ((index + 1) / totalSlides) * 100;
            progressBar.style.width = `${progressPercentage}%`;
        }
    }

    function showSlide(index) {
        const activeSlide = document.querySelector('.slide.active');
        if (activeSlide) {
            activeSlide.classList.remove('active');
        }

        currentSlide = (index + totalSlides) % totalSlides;

        slides[currentSlide].classList.add('active');
        updateUI(currentSlide);
    }

    document.querySelector('.next').addEventListener('click', () => {
        showSlide(currentSlide + 1);
    });

    document.querySelector('.prev').addEventListener('click', () => {
        showSlide(currentSlide - 1);
    });

    document.addEventListener('keydown', (e) => {
        if (e.key === 'ArrowRight') {
            showSlide(currentSlide + 1);
        } else if (e.key === 'ArrowLeft') {
            showSlide(currentSlide - 1);
        }
    });

    // Initialize the first slide
    showSlide(currentSlide);
});

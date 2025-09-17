document.addEventListener("DOMContentLoaded", function() {
  // Fetch and insert header
  fetch('templates/_header.html')
    .then(response => response.text())
    .then(data => {
      document.body.insertAdjacentHTML('afterbegin', data);
      // Set active navigation link
      const currentPage = window.location.pathname.split('/').pop();
      const navLinks = document.querySelectorAll('#nav2 .nav-item a');
      navLinks.forEach(link => {
        if (link.getAttribute('href') === currentPage) {
          link.classList.add('active');
        }
      });
    });

  // Fetch and insert footer
  fetch('templates/_footer.html')
    .then(response => response.text())
    .then(data => {
      document.body.insertAdjacentHTML('beforeend', data);
    });
});

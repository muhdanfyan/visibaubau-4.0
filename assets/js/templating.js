document.addEventListener("DOMContentLoaded", function() {
  const headerPlaceholder = document.getElementById('header-placeholder');
  const footerPlaceholder = document.getElementById('footer-placeholder');

  if (headerPlaceholder) {
    fetch('templates/_header.html')
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok ' + response.statusText);
        }
        return response.text();
      })
      .then(data => {
        headerPlaceholder.innerHTML = data;
        
        // Manually initialize Bootstrap Collapse for the dynamically loaded navbar
        const navbarToggler = headerPlaceholder.querySelector('.navbar-toggler');
        const navbarCollapseElement = headerPlaceholder.querySelector('#navbarSupportedContent2');

        if (navbarToggler && navbarCollapseElement && typeof bootstrap !== 'undefined' && bootstrap.Collapse) {
          // Create a new Bootstrap Collapse instance
          const bsCollapse = new bootstrap.Collapse(navbarCollapseElement, {
            toggle: false // Prevent immediate toggling
          });

          // Add a click listener to the toggler to manually call the toggle method
          navbarToggler.addEventListener('click', () => {
            bsCollapse.toggle();
          });
        } else if (typeof bootstrap === 'undefined') {
          console.warn('Bootstrap is not defined. Ensure bootstrap.bundle.min.js is loaded.');
        } else if (!bootstrap.Collapse) {
          console.warn('Bootstrap Collapse component not found. Ensure bootstrap.bundle.min.js is loaded correctly.');
        }

        // Manually initialize Bootstrap Dropdown for the dynamically loaded header
        const dropdownToggle = headerPlaceholder.querySelector('.nav-item.dropdown .dropdown-toggle');
        if (dropdownToggle && typeof bootstrap !== 'undefined' && bootstrap.Dropdown) {
          new bootstrap.Dropdown(dropdownToggle);
        } else if (typeof bootstrap === 'undefined') {
          console.warn('Bootstrap is not defined. Ensure bootstrap.bundle.min.js is loaded.');
        } else if (!bootstrap.Dropdown) {
          console.warn('Bootstrap Dropdown component not found. Ensure bootstrap.bundle.min.js is loaded correctly.');
        }

        // Set active navigation link
        const navContainer = headerPlaceholder.querySelector('#nav2');
        if (navContainer) {
          const currentPage = window.location.pathname.split('/').pop() || 'index.html';
          let dropdownParentActive = false; // Flag to check if any dropdown item is active

          const navLinks = navContainer.querySelectorAll('.nav-item a');
          navLinks.forEach(link => {
            const linkPage = link.getAttribute('href').split('/').pop();
            if (linkPage === currentPage) {
              link.classList.add('active');
              // Check if this active link is inside a dropdown
              if (link.closest('.dropdown-menu')) {
                dropdownParentActive = true;
              }
            }
          });

          // If any dropdown item is active, set the parent dropdown toggle to active
          if (dropdownParentActive) {
            const dropdownToggle = navContainer.querySelector('.nav-item.dropdown .dropdown-toggle');
            if (dropdownToggle) {
              dropdownToggle.classList.add('active');
            }
          }
        }
      })
      .catch(error => {
        console.error('Error fetching header:', error);
        headerPlaceholder.innerHTML = '<p style="color:red;">Error loading header.</p>';
      });
  }

  if (footerPlaceholder) {
    fetch('templates/_footer.html')
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok ' + response.statusText);
        }
        return response.text();
      })
      .then(data => {
        footerPlaceholder.innerHTML = data;
      })
      .catch(error => {
        console.error('Error fetching footer:', error);
        footerPlaceholder.innerHTML = '<p style="color:red;">Error loading footer.</p>';
      });
  }
});
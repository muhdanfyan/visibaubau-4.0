/**
 * Visi Baubau 4.0 — Main JavaScript
 * Handles: templating, scroll animations, counter, nav highlighting, back-to-top
 */

document.addEventListener('DOMContentLoaded', () => {
  // ─── Detect base path from current page depth ───
  const getBasePath = () => {
    const script = document.querySelector('script[src$="js/main.js"]');
    if (script) {
      const src = script.getAttribute('src');
      const base = src.replace('js/main.js', '');
      return base === '' ? './' : base;
    }
    return './';
  };

  const BASE = getBasePath();

  // ─── Load Components (Header, Footer) ───
  const loadComponent = (placeholderId, componentPath) => {
    const el = document.getElementById(placeholderId);
    if (!el) return Promise.resolve();

    return fetch(BASE + componentPath)
      .then(r => {
        if (!r.ok) throw new Error(`Failed to load ${componentPath}`);
        return r.text();
      })
      .then(html => {
        // Replace {{BASE}} placeholders with actual base path
        html = html.replace(/\{\{BASE\}\}/g, BASE);
        // Replace {{ASSET}} with path to root assets folder
        const assetPath = BASE + '../assets/';
        html = html.replace(/\{\{ASSET\}\}/g, assetPath);
        el.innerHTML = html;
        return el;
      })
      .catch(err => {
        console.error(err);
        el.innerHTML = `<p class="text-red-500 text-center p-4">Error loading component.</p>`;
      });
  };

  // Load header then set active nav + init mobile menu
  loadComponent('header-placeholder', 'components/header.html').then(headerEl => {
    if (!headerEl) return;
    setActiveNav(headerEl);
    initMobileMenu(headerEl);
    initStickyHeader(headerEl);
    initDropdowns(headerEl);
  });

  loadComponent('footer-placeholder', 'components/footer.html');

  // ─── Set Active Navigation Link ───
  const setActiveNav = (container) => {
    const currentPath = window.location.pathname;
    const links = container.querySelectorAll('a[href]');
    links.forEach(link => {
      const href = link.getAttribute('href');
      if (href === '#' || href.startsWith('http')) return;
      // Normalize paths for comparison
      const linkPath = href.replace(/^\.\//, '').replace(/^\.\.\//, '');
      if (currentPath.endsWith(linkPath) || 
          (linkPath === 'index.html' && (currentPath.endsWith('/new/') || currentPath.endsWith('/new')))) {
        link.classList.add('text-blue-500', 'font-semibold');
        // If inside dropdown, also highlight parent
        const dropdownParent = link.closest('[data-dropdown]');
        if (dropdownParent) {
          const trigger = dropdownParent.querySelector('[data-dropdown-trigger]');
          if (trigger) trigger.classList.add('text-blue-500');
        }
      }
    });
  };

  // ─── Mobile Menu Toggle ───
  const initMobileMenu = (container) => {
    const btn = container.querySelector('#mobile-menu-btn');
    const menu = container.querySelector('#mobile-menu');
    if (!btn || !menu) return;

    btn.addEventListener('click', () => {
      const isOpen = menu.classList.contains('hidden');
      menu.classList.toggle('hidden');
      // Animate hamburger icon
      const bars = btn.querySelectorAll('.hamburger-bar');
      bars.forEach(bar => bar.classList.toggle('active'));
      btn.setAttribute('aria-expanded', isOpen);
    });

    // Close on link click
    menu.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        menu.classList.add('hidden');
        btn.setAttribute('aria-expanded', 'false');
      });
    });

    // Mobile dropdown toggles
    menu.querySelectorAll('[data-mobile-dropdown-trigger]').forEach(trigger => {
      trigger.addEventListener('click', (e) => {
        e.preventDefault();
        const submenu = trigger.nextElementSibling;
        if (submenu) {
          submenu.classList.toggle('hidden');
          const icon = trigger.querySelector('.dropdown-icon');
          if (icon) icon.classList.toggle('rotate-180');
        }
      });
    });
  };

  // ─── Desktop Dropdown Menus ───
  const initDropdowns = (container) => {
    container.querySelectorAll('[data-dropdown]').forEach(dropdown => {
      const trigger = dropdown.querySelector('[data-dropdown-trigger]');
      const menu = dropdown.querySelector('[data-dropdown-menu]');
      if (!trigger || !menu) return;

      let timeout;
      dropdown.addEventListener('mouseenter', () => {
        clearTimeout(timeout);
        menu.classList.remove('opacity-0', 'invisible', 'scale-95');
        menu.classList.add('opacity-100', 'visible', 'scale-100');
      });
      dropdown.addEventListener('mouseleave', () => {
        timeout = setTimeout(() => {
          menu.classList.add('opacity-0', 'invisible', 'scale-95');
          menu.classList.remove('opacity-100', 'visible', 'scale-100');
        }, 150);
      });
    });
  };

  // ─── Sticky Header ───
  const initStickyHeader = (container) => {
    const header = container.querySelector('header');
    if (!header) return;
    window.addEventListener('scroll', () => {
      if (window.scrollY > 50) {
        header.classList.add('header-scrolled');
      } else {
        header.classList.remove('header-scrolled');
      }
    }, { passive: true });
  };

  // ─── Scroll Animations (Intersection Observer) ───
  const animateOnScroll = () => {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('animated');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

    document.querySelectorAll('[data-animate]').forEach(el => observer.observe(el));
  };
  // Run immediately for elements already in DOM, and again after components load
  animateOnScroll();
  setTimeout(animateOnScroll, 500);

  // ─── Counter Animation ───
  const animateCounters = () => {
    const counters = document.querySelectorAll('[data-count]');
    if (!counters.length) return;

    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const el = entry.target;
          const target = parseInt(el.getAttribute('data-count'), 10);
          const suffix = el.getAttribute('data-suffix') || '';
          let current = 0;
          const increment = Math.ceil(target / 40);
          const timer = setInterval(() => {
            current += increment;
            if (current >= target) {
              current = target;
              clearInterval(timer);
            }
            el.textContent = current + suffix;
          }, 40);
          observer.unobserve(el);
        }
      });
    }, { threshold: 0.5 });

    counters.forEach(c => observer.observe(c));
  };
  animateCounters();
  setTimeout(animateCounters, 600);

  // ─── Back to Top Button ───
  const backToTop = document.getElementById('back-to-top');
  if (backToTop) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 400) {
        backToTop.classList.add('visible');
      } else {
        backToTop.classList.remove('visible');
      }
    }, { passive: true });

    backToTop.addEventListener('click', () => {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  // ─── Video Modal ───
  const initVideoModal = () => {
    const modal = document.getElementById('video-modal');
    const iframe = document.getElementById('yt-iframe');
    if (!modal || !iframe) return;

    const videoSrc = iframe.getAttribute('data-src');

    document.querySelectorAll('[data-open-video]').forEach(btn => {
      btn.addEventListener('click', () => {
        modal.classList.remove('hidden');
        modal.classList.add('flex');
        iframe.src = videoSrc + '?autoplay=1&rel=0';
        document.body.style.overflow = 'hidden';
      });
    });

    const closeModal = () => {
      modal.classList.add('hidden');
      modal.classList.remove('flex');
      iframe.src = '';
      document.body.style.overflow = '';
    };

    modal.addEventListener('click', (e) => {
      if (e.target === modal || e.target.closest('[data-close-video]')) {
        closeModal();
      }
    });

    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && !modal.classList.contains('hidden')) {
        closeModal();
      }
    });
  };
  initVideoModal();

  // ─── Presentation Slider ───
  const initSlider = () => {
    const slider = document.getElementById('presentation-slider');
    if (!slider) return;

    const slides = slider.querySelectorAll('.slide-item');
    const prevBtn = document.getElementById('slide-prev');
    const nextBtn = document.getElementById('slide-next');
    const indicator = document.getElementById('slide-indicator');
    const totalEl = document.getElementById('slide-total');
    const currentEl = document.getElementById('slide-current');
    let current = 0;

    const showSlide = (index) => {
      slides.forEach((s, i) => {
        s.classList.toggle('hidden', i !== index);
      });
      current = index;
      if (currentEl) currentEl.textContent = current + 1;
      if (totalEl) totalEl.textContent = slides.length;

      // Update dots
      if (indicator) {
        indicator.querySelectorAll('button').forEach((dot, i) => {
          dot.classList.toggle('bg-blue-500', i === index);
          dot.classList.toggle('bg-gray-300', i !== index);
        });
      }

      // Disable buttons at edges
      if (prevBtn) prevBtn.disabled = current === 0;
      if (nextBtn) nextBtn.disabled = current === slides.length - 1;
    };

    // Build dot indicators
    if (indicator) {
      slides.forEach((_, i) => {
        const dot = document.createElement('button');
        dot.className = `w-2.5 h-2.5 rounded-full transition-all duration-300 ${i === 0 ? 'bg-blue-500 w-6' : 'bg-gray-300'}`;
        dot.addEventListener('click', () => showSlide(i));
        indicator.appendChild(dot);
      });
    }

    if (prevBtn) prevBtn.addEventListener('click', () => { if (current > 0) showSlide(current - 1); });
    if (nextBtn) nextBtn.addEventListener('click', () => { if (current < slides.length - 1) showSlide(current + 1); });

    // Keyboard navigation
    document.addEventListener('keydown', (e) => {
      if (!slider.closest('body')) return;
      if (e.key === 'ArrowLeft' && current > 0) showSlide(current - 1);
      if (e.key === 'ArrowRight' && current < slides.length - 1) showSlide(current + 1);
    });

    showSlide(0);
  };
  initSlider();
});

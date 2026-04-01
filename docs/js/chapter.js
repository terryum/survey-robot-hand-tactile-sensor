/* ============================================
   Tactile Sensing for Robot Hands — Chapter JS
   GSAP ScrollTrigger animations, sidebar nav
   ============================================ */

document.addEventListener('DOMContentLoaded', function() {

  // --- GSAP ScrollTrigger Animations ---
  if (typeof gsap !== 'undefined' && typeof ScrollTrigger !== 'undefined') {
    gsap.registerPlugin(ScrollTrigger);

    // Section enter animations
    gsap.utils.toArray('.content-section').forEach((section, i) => {
      gsap.from(section, {
        scrollTrigger: {
          trigger: section,
          start: 'top 85%',
          toggleActions: 'play none none reverse'
        },
        y: 40,
        opacity: 0,
        duration: 0.8,
        delay: i * 0.05
      });
    });

    // Chapter header animation
    const header = document.querySelector('.chapter-header');
    if (header) {
      gsap.from(header, {
        y: 30,
        opacity: 0,
        duration: 1,
        ease: 'power2.out'
      });
    }

    // Figure animations
    gsap.utils.toArray('figure').forEach(fig => {
      gsap.from(fig, {
        scrollTrigger: {
          trigger: fig,
          start: 'top 85%',
          toggleActions: 'play none none reverse'
        },
        y: 30,
        opacity: 0,
        duration: 0.6
      });
    });

    // Table animations
    gsap.utils.toArray('.styled-table').forEach(table => {
      gsap.from(table, {
        scrollTrigger: {
          trigger: table,
          start: 'top 85%',
          toggleActions: 'play none none reverse'
        },
        y: 20,
        opacity: 0,
        duration: 0.6
      });
    });
  } else {
    // Fallback: just make everything visible
    document.querySelectorAll('.content-section').forEach(el => {
      el.classList.add('visible');
    });
  }

  // --- Sidebar Dot Navigation ---
  const sidebarNav = document.querySelector('.sidebar-nav');
  const sections = document.querySelectorAll('.content-section[id]');

  if (sidebarNav && sections.length > 0) {
    // Update active dot on scroll
    const observerOptions = {
      rootMargin: '-20% 0px -70% 0px',
      threshold: 0
    };

    const sectionObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const id = entry.target.id;
          document.querySelectorAll('.sidebar-nav .nav-dot').forEach(dot => {
            dot.classList.toggle('active', dot.getAttribute('data-section') === id);
          });
        }
      });
    }, observerOptions);

    sections.forEach(section => sectionObserver.observe(section));

    // Click to scroll
    sidebarNav.querySelectorAll('.nav-dot').forEach(dot => {
      dot.addEventListener('click', () => {
        const targetId = dot.getAttribute('data-section');
        const target = document.getElementById(targetId);
        if (target) {
          target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
      });
    });
  }

  // --- Citation click: scroll reference to top with offset ---
  document.querySelectorAll('a.cite-link').forEach((link, idx) => {
    link.addEventListener('click', function(e) {
      e.preventDefault();
      const targetId = this.getAttribute('href').substring(1);
      const target = document.getElementById(targetId);
      if (!target) return;

      // Give this citation a unique back-anchor
      const backId = 'cite-back-' + targetId;
      this.closest('sup').id = backId;

      // Scroll reference into view with padding at top
      const headerOffset = 100;
      const y = target.getBoundingClientRect().top + window.pageYOffset - headerOffset;
      window.scrollTo({ top: y, behavior: 'smooth' });

      // Highlight the reference
      target.classList.add('ref-highlight');
      setTimeout(() => target.classList.remove('ref-highlight'), 3000);

      // Inject back-link if not already present
      if (!target.querySelector('.cite-backlink')) {
        const backLink = document.createElement('a');
        backLink.className = 'cite-backlink';
        backLink.href = '#' + backId;
        backLink.textContent = ' ↩';
        backLink.title = 'Back to text';
        backLink.addEventListener('click', function(ev) {
          ev.preventDefault();
          const backTarget = document.getElementById(backId);
          if (backTarget) {
            const by = backTarget.getBoundingClientRect().top + window.pageYOffset - headerOffset;
            window.scrollTo({ top: by, behavior: 'smooth' });
            backTarget.classList.add('cite-back-highlight');
            setTimeout(() => backTarget.classList.remove('cite-back-highlight'), 2000);
          }
        });
        target.appendChild(backLink);
      }
    });
  });
});

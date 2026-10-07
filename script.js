const menuButton = document.querySelector('.menu-toggle');
const mobileMenu = document.querySelector('#mobile-menu');

// Everything behind the full-screen menu; made inert so Tab stays in the header + menu.
const behindMenu = document.querySelectorAll('.skip-link, main, .site-footer');
const isMenuOpen = () => menuButton?.getAttribute('aria-expanded') === 'true';

function setMenu(open) {
  menuButton?.setAttribute('aria-expanded', String(open));
  if (mobileMenu) mobileMenu.hidden = !open;
  document.body.style.overflow = open ? 'hidden' : '';
  behindMenu.forEach((element) => { element.inert = open; });
}

function closeMenu() {
  setMenu(false);
}

menuButton?.addEventListener('click', () => {
  const willOpen = !isMenuOpen();
  setMenu(willOpen);
  if (willOpen) mobileMenu?.querySelector('a')?.focus();
});

mobileMenu?.querySelectorAll('a').forEach((link) => link.addEventListener('click', closeMenu));
matchMedia('(min-width: 861px)').addEventListener('change', (e) => e.matches && closeMenu());
document.addEventListener('keydown', (e) => {
  if (e.key !== 'Escape' || !isMenuOpen()) return;
  closeMenu();
  menuButton.focus();
});

const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
const reveals = document.querySelectorAll('.reveal');

if (reduceMotion || !('IntersectionObserver' in window)) {
  reveals.forEach((element) => element.classList.add('is-visible'));
} else {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-visible');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.14, rootMargin: '0px 0px -8% 0px' });

  reveals.forEach((element) => observer.observe(element));
}

const root = document.documentElement;
const themeToggle = document.querySelector('.theme-toggle');
const themeColor = document.querySelector('meta[name="theme-color"]');

function applyTheme(theme) {
  root.dataset.theme = theme;
  themeToggle?.setAttribute('aria-label', theme === 'dark' ? 'Switch to light mode' : 'Switch to dark mode');
  themeColor?.setAttribute('content', theme === 'dark' ? '#121210' : '#f3eee4');
}

applyTheme(root.dataset.theme === 'dark' ? 'dark' : 'light');
themeToggle?.addEventListener('click', () => {
  const next = root.dataset.theme === 'dark' ? 'light' : 'dark';
  applyTheme(next);
  try { localStorage.setItem('theme', next); } catch (e) {}
});

const header = document.querySelector('.site-header');
const onScroll = () => header?.classList.toggle('is-scrolled', window.scrollY > 8);
window.addEventListener('scroll', onScroll, { passive: true });
onScroll();

const year = document.querySelector('#year');
if (year) year.textContent = String(new Date().getFullYear());

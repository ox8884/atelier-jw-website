const root = document.documentElement;
const themeSwitch = document.querySelector('.theme-switch');
const themeColor = document.querySelector('meta[name="theme-color"]');

function applyTheme(theme) {
  root.dataset.theme = theme;
  themeSwitch?.setAttribute('aria-checked', String(theme === 'dark'));
  themeColor?.setAttribute('content', theme === 'dark' ? '#191410' : '#f8f6f3');
}

applyTheme(root.dataset.theme === 'dark' ? 'dark' : 'light');
themeSwitch?.addEventListener('click', () => {
  const next = root.dataset.theme === 'dark' ? 'light' : 'dark';
  applyTheme(next);
  try { localStorage.setItem('theme', next); } catch (e) {}
});

const year = document.querySelector('#year');
if (year) year.textContent = String(new Date().getFullYear());

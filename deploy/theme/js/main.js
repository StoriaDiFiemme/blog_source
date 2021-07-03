const button = document.querySelector('#mobile-menu-button');
const overlay = document.querySelector('#mobile-overlay');
const sidebar = document.querySelector('#sidebar');

overlay.addEventListener('click', () => {
  sidebar.classList.toggle('-translate-x-full');
  overlay.classList.toggle('hidden');
});

button.addEventListener('click', () => {
  sidebar.classList.toggle('-translate-x-full');
  overlay.classList.toggle('hidden');
});

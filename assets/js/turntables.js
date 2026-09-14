(() => {
  const images = [...document.querySelectorAll('[data-turntable]')];
  const buttons = [...document.querySelectorAll('.turntable-toggle')];
  if (!images.length) return;
  const preference = window.matchMedia('(prefers-reduced-motion: reduce)');
  let paused = preference.matches;

  function update() {
    for (const image of images) {
      image.parentElement.querySelector('source').media = 'not all';
      image.src = paused ? image.dataset.still : image.dataset.turntable;
    }
    for (const button of buttons) {
      button.hidden = false;
      button.textContent = paused ? 'Play rotations' : 'Pause rotations';
      button.setAttribute('aria-pressed', String(paused));
    }
  }

  for (const button of buttons) {
    button.addEventListener('click', () => { paused = !paused; update(); });
  }
  preference.addEventListener('change', (event) => { paused = event.matches; update(); });
  update();
})();

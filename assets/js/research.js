(() => {
  'use strict';
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  document.querySelectorAll('[data-walkthrough]').forEach(figure => {
    const stages = [...figure.querySelectorAll('[data-stage]')];
    const play = figure.querySelector('.walkthrough-play');
    const current = figure.querySelector('.walkthrough-current');
    const counter = figure.querySelector('[data-step-count]');
    const previous = figure.querySelector('[data-previous]');
    const next = figure.querySelector('[data-next]');
    let index = 0;
    let timer = null;
    let playing = false;

    const stop = () => {
      clearTimeout(timer);
      timer = null;
      playing = false;
      figure.classList.remove('is-playing');
      play.textContent = index === stages.length - 1 ? 'Replay walkthrough' : 'Play walkthrough';
    };
    const show = value => {
      index = value;
      stages.forEach((stage, i) => {
        stage.classList.toggle('is-active', i === index);
        stage.querySelector('button').setAttribute('aria-pressed', String(i === index));
      });
      current.textContent = stages[index].querySelector('.walkthrough-detail').textContent;
      counter.textContent = `${index + 1} of ${stages.length}`;
      previous.disabled = index === 0;
      next.disabled = index === stages.length - 1;
      if (!playing) play.textContent = index === stages.length - 1 ? 'Replay walkthrough' : 'Play walkthrough';
    };
    const advance = () => {
      timer = setTimeout(() => {
        if (index === stages.length - 1) { stop(); return; }
        show(index + 1);
        advance();
      }, 6500);
    };
    stages.forEach((stage, i) => {
      const button = stage.querySelector('button');
      button.disabled = false;
      button.addEventListener('click', () => { stop(); show(i); });
    });
    previous.addEventListener('click', () => { stop(); show(Math.max(0, index - 1)); });
    next.addEventListener('click', () => { stop(); show(Math.min(stages.length - 1, index + 1)); });
    play.addEventListener('click', () => {
      if (playing) { stop(); return; }
      if (index === stages.length - 1) show(0);
      playing = true;
      play.textContent = 'Pause walkthrough';
      figure.classList.add('is-playing');
      advance();
    });
    document.addEventListener('visibilitychange', () => { if (document.hidden) stop(); });
    reducedMotion.addEventListener('change', stop);
    if ('IntersectionObserver' in window) {
      new IntersectionObserver(entries => {
        if (!entries[0].isIntersecting) stop();
      }).observe(figure);
    }
    figure.classList.add('is-enhanced');
    figure.querySelector('.walkthrough-reading').hidden = false;
    play.hidden = false;
    show(0);
  });
})();

(() => {
  const diagram = document.querySelector('[data-papaw-placement]');
  if (!diagram) return;
  const walk = diagram.querySelector('[data-walk-through]');
  const door = diagram.querySelector('[data-toggle-door]');
  const person = diagram.querySelector('.placement-person');
  const motionState = diagram.querySelector('[data-motion-state]');
  const doorState = diagram.querySelector('[data-door-state]');
  const event = diagram.querySelector('[data-receiver-event]');
  const receiver = diagram.querySelector('.placement-receiver');
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  let doorOpen = false;

  function receive(message) {
    receiver.classList.add('has-received-event');
    event.textContent = message;
  }

  walk.hidden = false;
  door.hidden = false;
  walk.addEventListener('click', () => {
    walk.disabled = true;
    person.classList.add('is-walking');
    motionState.textContent = 'Approaching the doorway';
    window.setTimeout(() => {
      diagram.dataset.motionActive = 'true';
      motionState.textContent = 'Motion detected: direction is unknown';
      receive('Doorway motion → ESP-NOW → USB receiver → timestamped activity log');
    }, reducedMotion.matches ? 0 : 1000);
    window.setTimeout(() => {
      person.classList.remove('is-walking');
      diagram.dataset.motionActive = 'false';
      motionState.textContent = 'No motion reported';
      walk.disabled = false;
    }, 4200);
  });

  door.addEventListener('click', () => {
    doorOpen = !doorOpen;
    diagram.dataset.doorOpen = String(doorOpen);
    diagram.querySelector('.magnet-leader').setAttribute('d', doorOpen ? 'M284 292L309 107H169' : 'M330 141V107H169');
    door.textContent = doorOpen ? 'Close door ↙' : 'Open door ↗';
    doorState.textContent = doorOpen ? 'Door open: magnet away from sensor' : 'Door closed: magnet beside sensor';
    diagram.querySelector('[data-gap-label]').textContent = doorOpen ? 'Magnet moves away' : 'Magnet beside sensor';
    receive(`${doorOpen ? 'Door opened' : 'Door closed'} → ESP-NOW → USB receiver → timestamped activity log`);
  });
})();

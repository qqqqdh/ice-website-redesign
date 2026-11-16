// Progressive enhancement: the page content itself is static HTML.
const menuButton = document.querySelector('.menu-button');
const navigation = document.querySelector('#site-nav');
function setMenu(open) {
  navigation.dataset.open = String(open);
  menuButton.setAttribute('aria-expanded', String(open));
  menuButton.setAttribute('aria-label', open ? '메뉴 닫기' : '메뉴 열기');
  menuButton.querySelector('path').setAttribute('d', open ? 'M6 6l12 12M6 18 18 6' : 'M4 6h16M4 12h16M4 18h16');
}
menuButton.addEventListener('click', () => setMenu(navigation.dataset.open !== 'true'));
navigation.addEventListener('click', event => {
  if (event.target.closest('a')) setMenu(false);
});
document.querySelector('.site-header').addEventListener('keydown', event => {
  if (event.key === 'Escape' && navigation.dataset.open === 'true') {
    setMenu(false);
    menuButton.focus();
  }
});
const tabs = [...document.querySelectorAll('[role="tab"]')];
function selectTab(selected) {
  tabs.forEach(tab => {
    const active = tab === selected;
    tab.setAttribute('aria-selected', String(active));
    tab.tabIndex = active ? 0 : -1;
    document.getElementById(tab.getAttribute('aria-controls')).hidden = !active;
  });
}
tabs.forEach((tab, index) => {
  tab.addEventListener('click', () => selectTab(tab));
  tab.addEventListener('keydown', event => {
    let next;
    if (event.key === 'ArrowRight') next = tabs[(index + 1) % tabs.length];
    if (event.key === 'ArrowLeft') next = tabs[(index - 1 + tabs.length) % tabs.length];
    if (event.key === 'Home') next = tabs[0];
    if (event.key === 'End') next = tabs[tabs.length - 1];
    if (next) { event.preventDefault(); selectTab(next); next.focus(); }
  });
});
const dialog = document.querySelector('#detail-dialog');
let detailTrigger;
document.querySelectorAll('[data-detail]').forEach(button => {
  button.addEventListener('click', () => {
    detailTrigger = button;
    document.querySelector('#detail-title').textContent = button.dataset.title;
    document.querySelector('#detail-type').textContent = button.dataset.type;
    document.querySelector('#detail-body').textContent = button.dataset.body;
    dialog.showModal();
  });
});
dialog.addEventListener('close', () => detailTrigger?.focus());
dialog.addEventListener('click', event => {
  const rect = dialog.getBoundingClientRect();
  if (event.target === dialog && (event.clientX < rect.left || event.clientX > rect.right || event.clientY < rect.top || event.clientY > rect.bottom)) dialog.close();
});

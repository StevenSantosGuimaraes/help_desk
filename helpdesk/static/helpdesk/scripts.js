// Alternância de tema e sidebar

document.addEventListener('DOMContentLoaded', function () {
  const sidebar = document.getElementById('sidebar');
  const themeToggle = document.getElementById('theme-toggle');
  const sidebarToggle = document.getElementById('sidebar-toggle');
  const body = document.body;
  // Sidebar toggle
  if (sidebarToggle) {
    sidebarToggle.addEventListener('click', function () {
      body.classList.toggle('sidebar-collapsed');
    });
  }
  // Salvar preferência no localStorage
  function setTheme(theme) {
    if (theme === 'light') {
      sidebar.classList.remove('bg-dark', 'text-white');
      sidebar.classList.add('bg-light', 'text-dark');
      body.classList.remove('bg-dark', 'text-white');
      body.classList.add('bg-light', 'text-dark');
      themeToggle.classList.remove('btn-outline-light');
      themeToggle.classList.add('btn-outline-dark');
    } else {
      sidebar.classList.remove('bg-light', 'text-dark');
      sidebar.classList.add('bg-dark', 'text-white');
      body.classList.remove('bg-light', 'text-dark');
      body.classList.add('bg-dark', 'text-white');
      themeToggle.classList.remove('btn-outline-dark');
      themeToggle.classList.add('btn-outline-light');
    }
    localStorage.setItem('theme', theme);
  }
  // Alternar tema ao clicar
  if (themeToggle) {
    themeToggle.addEventListener('click', function () {
      const current = localStorage.getItem('theme') || 'dark';
      setTheme(current === 'dark' ? 'light' : 'dark');
    });
    // Aplicar tema salvo
    const savedTheme = localStorage.getItem('theme') || 'dark';
    setTheme(savedTheme);
  }
});

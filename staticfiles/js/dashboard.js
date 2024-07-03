// static/js/dashboard.js
document.addEventListener('DOMContentLoaded', function() {
    const sidebarToggle = document.getElementById('sidebar-toggle');
    const sidebar = document.getElementById('sidebar');
    const content = document.querySelector('.content');
    const dropdownToggle = document.querySelector('.dropdown-toggle');

    // Sidebar toggle
    sidebarToggle.addEventListener('click', function() {
        sidebar.classList.toggle('collapsed');
        content.style.marginLeft = sidebar.classList.contains('collapsed') ? '0' : '250px';
    });

    // Dropdown toggle
    dropdownToggle.addEventListener('click', function(e) {
        e.preventDefault();
        this.parentNode.classList.toggle('active');
    });
});
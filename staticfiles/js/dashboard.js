// static/js/dashboard.js
document.addEventListener('DOMContentLoaded', function() {
    const sidebarToggle = document.getElementById('sidebar-toggle');
    const sidebar = document.getElementById('sidebar');
    const content = document.querySelector('.content');
    const dropdownToggles = document.querySelectorAll('.dropdown-toggle');

    // Sidebar toggle
    sidebarToggle.addEventListener('click', function() {
        sidebar.classList.toggle('active');
        
        // Only adjust content margin on larger screens
        if (window.innerWidth > 768) {
            content.style.marginLeft = sidebar.classList.contains('active') ? '0' : '250px';
        }
    });

    // Dropdown toggles
    dropdownToggles.forEach(function(toggle) {
        toggle.addEventListener('click', function(e) {
            e.preventDefault();
            this.parentNode.classList.toggle('active');
        });
    });

    // Adjust layout on window resize
    function handleResize() {
        if (window.innerWidth > 768) {
            sidebar.classList.remove('active');
            content.style.marginLeft = '250px';
            sidebar.style.maxHeight = 'none';
        } else {
            content.style.marginLeft = '0';
            sidebar.style.maxHeight = sidebar.classList.contains('active') ? `calc(100vh - 64px)` : '0';
        }
    }

    window.addEventListener('resize', handleResize);
    handleResize(); // Call once to set initial state
});
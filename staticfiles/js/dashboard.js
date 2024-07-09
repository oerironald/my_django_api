document.addEventListener('DOMContentLoaded', function() {
    console.log('DOM content loaded');

    const sidebarToggle = document.getElementById('sidebar-toggle');
    const sidebar = document.getElementById('sidebar');
    const mainContent = document.querySelector('.main-content');

    console.log('Sidebar toggle:', sidebarToggle);
    console.log('Sidebar:', sidebar);

    // Function to toggle sidebar
    function toggleSidebar() {
        sidebar.classList.toggle('active');
        document.body.classList.toggle('sidebar-open');
        // Store the sidebar state in localStorage
        localStorage.setItem('sidebarOpen', sidebar.classList.contains('active'));
    }

    // Sidebar toggle
    if (sidebarToggle && sidebar) {
        sidebarToggle.addEventListener('click', function(e) {
            e.preventDefault();
            console.log('Toggle clicked');
            toggleSidebar();
        });
    } else {
        console.error('Sidebar toggle or sidebar not found');
    }

    // Close sidebar when clicking outside
    document.addEventListener('click', function(e) {
        if (window.innerWidth <= 768 && 
            sidebar.classList.contains('active') && 
            !sidebar.contains(e.target) && 
            e.target !== sidebarToggle) {
            toggleSidebar();
        }
    });

    // Dropdown toggles
    const dropdownToggles = document.querySelectorAll('.dropdown-toggle');
    dropdownToggles.forEach(function(toggle) {
        toggle.addEventListener('click', function(e) {
            e.preventDefault();
            this.parentNode.classList.toggle('active');
        });
    });

    // Check localStorage for sidebar state on page load
    if (localStorage.getItem('sidebarOpen') === 'true') {
        sidebar.classList.add('active');
        document.body.classList.add('sidebar-open');
    }

    // Handle window resize
    window.addEventListener('resize', function() {
        if (window.innerWidth > 768) {
            sidebar.classList.remove('active');
            document.body.classList.remove('sidebar-open');
        }
    });
});
// dashboard.js

document.addEventListener('DOMContentLoaded', (event) => {
    const sidebarToggleBtn = document.getElementById('sidebar-toggle');
    const sidebar = document.getElementById('sidebar');
    const mainContent = document.querySelector('.main-content');

    if (sidebarToggleBtn && sidebar && mainContent) {
        sidebarToggleBtn.addEventListener('click', () => {
            sidebar.classList.toggle('hide');
            mainContent.classList.toggle('responsive');
        });
    } else {
        console.error('One or more elements not found for sidebar toggle');
    }

    function handleResize() {
        if (window.innerWidth > 768) {
            sidebar.classList.remove('hide');
            mainContent.classList.remove('responsive');
        } else {
            sidebar.classList.add('hide');
            mainContent.classList.add('responsive');
        }
    }

    window.addEventListener('resize', handleResize);
    handleResize();

    // Dropdown toggle
    const dropdownToggles = document.querySelectorAll('.sidebar-menu .dropdown > a');
    
    dropdownToggles.forEach(toggle => {
        toggle.addEventListener('click', (event) => {
            event.preventDefault();
            event.stopPropagation();

            const dropdownItem = toggle.closest('.dropdown');

            // Close all other open dropdowns
            dropdownToggles.forEach(otherToggle => {
                const otherDropdownItem = otherToggle.closest('.dropdown');
                if (otherDropdownItem !== dropdownItem) {
                    otherDropdownItem.classList.remove('open');
                }
            });

            // Toggle the clicked dropdown
            dropdownItem.classList.toggle('open');

            console.log('Dropdown clicked:', dropdownItem.classList.contains('open'));
        });
    });

    // Close dropdowns when clicking outside
    document.addEventListener('click', (event) => {
        if (!event.target.closest('.dropdown')) {
            dropdownToggles.forEach(toggle => {
                const dropdownItem = toggle.closest('.dropdown');
                dropdownItem.classList.remove('open');
            });
        }
    });

    // Add keyboard accessibility
    dropdownToggles.forEach(toggle => {
        toggle.addEventListener('keydown', (event) => {
            if (event.key === 'Enter' || event.key === ' ') {
                event.preventDefault();
                toggle.click();
            }
        });
    });

    console.log('Dropdown toggles:', dropdownToggles);
});
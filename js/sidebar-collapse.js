/**
 * AICTECH - SIDEBAR COLLAPSE & EXPAND INTERACTION
 * Controla el ocultamiento / despliegue del menú lateral con animación fluida
 * hacia la izquierda y expansión total del contenido.
 */

(function () {
    'use strict';

    function initSidebarCollapse() {
        const wrapper = document.getElementById('wrapper');
        const collapseBtn = document.getElementById('btn-sidebar-collapse');

        if (!collapseBtn) {
            return;
        }

        // Recuperar preferencia de colapso almacenada
        const savedState = localStorage.getItem('aictech_sidebar_collapsed');
        if (savedState === 'true' && window.innerWidth >= 992) {
            document.body.classList.add('sidebar-collapsed');
            if (wrapper) wrapper.classList.add('sidebar-collapsed');
            collapseBtn.classList.add('is-collapsed');
            updateButtonState(true);
        } else {
            updateButtonState(false);
        }

        // Función para actualizar ícono y título del botón
        function updateButtonState(isCollapsed) {
            if (isCollapsed) {
                collapseBtn.innerHTML = '<i class="fas fa-bars"></i>';
                collapseBtn.setAttribute('title', 'Mostrar Menú Lateral (Ctrl+B o [)');
                collapseBtn.setAttribute('aria-label', 'Mostrar Menú');
            } else {
                collapseBtn.innerHTML = '<i class="fas fa-chevron-left"></i>';
                collapseBtn.setAttribute('title', 'Ocultar Menú Lateral (Ctrl+B o [)');
                collapseBtn.setAttribute('aria-label', 'Ocultar Menú');
            }
        }

        // Toggle al hacer clic
        window.toggleSidebarMenu = function () {
            const isCurrentlyCollapsed = document.body.classList.toggle('sidebar-collapsed');
            if (wrapper) wrapper.classList.toggle('sidebar-collapsed', isCurrentlyCollapsed);
            collapseBtn.classList.toggle('is-collapsed', isCurrentlyCollapsed);
            localStorage.setItem('aictech_sidebar_collapsed', isCurrentlyCollapsed ? 'true' : 'false');
            updateButtonState(isCurrentlyCollapsed);

            // Disparar evento de resize tras la animación para que slick / videos recalculen su ancho
            setTimeout(function () {
                window.dispatchEvent(new Event('resize'));
            }, 360);
        };

        collapseBtn.addEventListener('click', function (e) {
            e.preventDefault();
            e.stopPropagation();
            window.toggleSidebarMenu();
        });

        // Atajo de teclado: [ o Ctrl+B para colapsar/expandir rápidamente
        document.addEventListener('keydown', function (e) {
            if (e.target && (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA' || e.target.isContentEditable)) {
                return;
            }
            if (e.key === '[' || (e.ctrlKey && (e.key === 'b' || e.key === 'B'))) {
                e.preventDefault();
                window.toggleSidebarMenu();
            }
        });
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initSidebarCollapse);
    } else {
        initSidebarCollapse();
    }
})();

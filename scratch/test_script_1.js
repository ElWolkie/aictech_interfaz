
    // Filtro interactivo de catálogo de productos
    function filterCatalog(category, btnElem) {
        // Actualizar botones de filtro
        document.querySelectorAll('.catalog-filter-btn').forEach(btn => {
            btn.classList.remove('active');
        });
        if (btnElem) {
            btnElem.classList.add('active');
        }

        // Filtrar tarjetas
        const cards = document.querySelectorAll('.process-area-card, .engineering-special-box');
        cards.forEach(card => {
            const cardCat = card.getAttribute('data-category');
            if (category === 'all' || cardCat === category) {
                card.style.display = 'block';
                card.classList.add('is-revealed');
            } else {
                card.style.display = 'none';
            }
        });

        // Desplazamiento suave hacia la primera tarjeta si es filtro individual
        if (category !== 'all') {
            const firstVisible = Array.from(cards).find(c => c.style.display !== 'none');
            if (firstVisible) {
                firstVisible.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        }
    }

    // Modal de Video HD de Echometer
    function openEchometerVideoModal() {
        const modal = document.getElementById('video-modal-echometer');
        const modalVideo = document.getElementById('echometer-modal-video');
        const mainVideo = document.getElementById('echometer-main-video');
        if (mainVideo && !mainVideo.paused) {
            try { mainVideo.pause(); } catch(e) {}
        }
        if (modal) {
            const speedBar = document.getElementById('media-lightbox-speed-bar');
            if (video && speedBar) {
                speedBar.style.display = 'flex';
                speedBar.querySelectorAll('.speed-btn').forEach((b, idx) => {
                    if (idx === 0) b.classList.add('active');
                    else b.classList.remove('active');
                });
            } else if (speedBar) {
                speedBar.style.display = 'none';
            }
            modal.classList.add('active');
            if (modalVideo) {
                modalVideo.currentTime = 0;
                modalVideo.play().catch(e => console.log(e));
            }
        }
    }

    function closeEchometerVideoModal() {
        const modal = document.getElementById('video-modal-echometer');
        const modalVideo = document.getElementById('echometer-modal-video');
        if (modal) {
            modal.classList.remove('active');
            if (modalVideo) {
                modalVideo.pause();
            }
        }
        if (typeof syncServiceVideosOnPage === 'function') {
            syncServiceVideosOnPage();
        }
    }

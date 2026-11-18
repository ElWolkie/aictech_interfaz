/*

TemplateMo 560 Astro Motion

https://templatemo.com/tm-560-astro-motion

*/

var gallery = undefined;

function closeMenu() {
  $(".navbar-collapse").removeClass("show"); 
}

function highlightMenu(no) {
  $(".navbar .navbar-nav > .nav-item").removeClass('selected');
  $(".navbar .navbar-nav > .nav-item > .nav-link[data-no='" + no + "']").parent().addClass('selected');

  $(".sidebar-nav-custom .nav-link, .inicio-nav-btn").removeClass('selected active');
  $(".sidebar-nav-custom .nav-link[data-no='" + no + "'], .inicio-nav-btn[data-no='" + no + "']").addClass('selected active');

  // Control automático de apertura del submenú de servicios y productos
  if (no == 2) {
    $("#servicios-submenu").addClass('is-open');
    $("#servicios-chevron").addClass('is-rotated');
  } else {
    $("#servicios-submenu").removeClass('is-open');
    $("#servicios-chevron").removeClass('is-rotated');
  }

  if (no == 5) {
    $("#productos-submenu").addClass('is-open');
    $("#productos-chevron").addClass('is-rotated');
  } else {
    $("#productos-submenu").removeClass('is-open');
    $("#productos-chevron").removeClass('is-rotated');
  }
}

function setupGallery() {
  var $gallery = $('.gallery-slider');
  if ($gallery.length && $gallery.children().length > 0) {
    gallery = $gallery.slick({
      slidesToShow: 5,
      slidesToScroll: 3,
      dots: true,
      arrows: false,
      responsive: [
        {
          breakpoint: 992,
          settings: {
            slidesToShow: 4,
            slidesToScroll: 4,
            infinite: true,
            dots: true
          }
        },
        {
          breakpoint: 767,
          settings: {
            slidesToShow: 3,
            slidesToScroll: 3
          }
        },
        {
          breakpoint: 575,
          settings: {
            slidesToShow: 2,
            slidesToScroll: 2
          }
        }
      ]
    });
  }
}

function openPage(no) {
  if (document.body) {
    if (no == 1) document.body.classList.add("is-page-1");
    else document.body.classList.remove("is-page-1");
  }
  if(!no) return;
  if(no != 1) {
    window._userHasNavigated = true;
  }

  var $current = $('.cd-hero-slider > li.selected');
  var currentNo = $current.data('page-no');
  if (currentNo == no && $current.is(':visible')) {
    if (typeof handlePageVideoPlayback === 'function') {
      handlePageVideoPlayback(no);
    }
    return;
  }

  if(no == 2) {
    if(gallery !== undefined && $('.gallery-slider').hasClass('slick-initialized')) {
      $('.gallery-slider').slick('unslick');
    }
    setupGallery();
  }

  $('.cd-hero-slider > li').removeClass('selected').hide();
  var $target = $('.cd-hero-slider > li[data-page-no="' + no + '"]');
  var displayMode = (no == 2 || no == 5) ? 'block' : 'flex';
  $target.css('display', displayMode).show().addClass('selected');
  
  // Garantizar revelado inmediato de todas las tarjetas para eliminar cualquier pantalla en blanco
  $target.find('.reveal-on-scroll').addClass('is-revealed');

  window.scrollTo({ top: 0, behavior: 'instant' });
  var pageWrapper = document.getElementById('page-content-wrapper');
  if (pageWrapper) {
    pageWrapper.scrollTo({ top: 0, behavior: 'instant' });
  }

  // OPTIMIZACIÓN DE RENDIMIENTO DE VIDEOS POR PANTALLA
  if (typeof handlePageVideoPlayback === 'function') {
    handlePageVideoPlayback(no);
  } else {
    var heroVideo = document.getElementById('hero-main-video');
    if (no == 1) {
      if (heroVideo && heroVideo.paused) {
        heroVideo.muted = true;
        heroVideo.playsInline = true;
        heroVideo.play().catch(function(e) {});
      }
    } else {
      if (heroVideo) {
        try { heroVideo.pause(); } catch(e) {}
      }
    }
  }

  if (no == 2 || no == 5) {
    if (typeof checkRevealElements === 'function') {
      setTimeout(checkRevealElements, 50);
      setTimeout(checkRevealElements, 250);
    }
    if (no == 2) {
      if (typeof syncServiceVideosOnPage === 'function') {
        setTimeout(syncServiceVideosOnPage, 100);
      }
      if (typeof syncCardVideosOnPage === 'function') {
        setTimeout(syncCardVideosOnPage, 100);
      }

    }
  }
}

$(window).on('load', function() {
  $('body').addClass('loaded');
  // Solo abrir página 1 si el usuario NO ha navegado ya a otra sección
  if (!window._userHasNavigated) {
    var isOtherSelected = $('.cd-hero-slider > li.selected').length && $('.cd-hero-slider > li.selected').data('page-no') != 1;
    if (!isOtherSelected) {
      openPage(1);
      highlightMenu(1);
    }
  }
});

jQuery(function() {
    $(document).on('click', '.tm-page-link', function(e){
      window._userHasNavigated = true;
      e.preventDefault();
      var pageNo = $(this).data('page-no');
      if(pageNo) {
        openPage(pageNo);
        highlightMenu(pageNo);
      }
    });

    $(document).on('click', ".sidebar-nav-custom .nav-link, .inicio-nav-btn, .navbar .navbar-nav > .nav-item > a.nav-link", function(e){
      window._userHasNavigated = true;
      e.preventDefault();
      var pageNo = $(this).attr('data-no') || $(this).data('no');

      // Alternar (abrir/cerrar) submenú de Servicios
      if ($(this).attr('id') === 'nav-link-servicios') {
        var isSubmenuOpen2 = $("#servicios-submenu").hasClass('is-open');
        var isAlreadyPage2 = $('.cd-hero-slider > li[data-page-no="2"]').hasClass('selected');
        if (isSubmenuOpen2 && isAlreadyPage2) {
          $("#servicios-submenu").removeClass('is-open');
          $("#servicios-chevron").removeClass('is-rotated');
          return;
        } else {
          $("#servicios-submenu").addClass('is-open');
          $("#servicios-chevron").addClass('is-rotated');
          if (!isAlreadyPage2) {
            openPage(2);
            highlightMenu(2);
          }
          return;
        }
      }

      // Alternar (abrir/cerrar) submenú de Productos
      if ($(this).attr('id') === 'nav-link-productos') {
        var isSubmenuOpen5 = $("#productos-submenu").hasClass('is-open');
        var isAlreadyPage5 = $('.cd-hero-slider > li[data-page-no="5"]').hasClass('selected');
        if (isSubmenuOpen5 && isAlreadyPage5) {
          $("#productos-submenu").removeClass('is-open');
          $("#productos-chevron").removeClass('is-rotated');
          return;
        } else {
          $("#productos-submenu").addClass('is-open');
          $("#productos-chevron").addClass('is-rotated');
          if (!isAlreadyPage5) {
            openPage(5);
            highlightMenu(5);
          }
          return;
        }
      }

      if (pageNo) {
        openPage(pageNo);
        highlightMenu(pageNo);
      }
      closeMenu();     
    });

    $("html").click(function(e) {
      closeMenu();
    });
});
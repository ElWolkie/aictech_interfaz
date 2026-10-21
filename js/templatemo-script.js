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

  $(".sidebar-nav-custom .nav-link").removeClass('selected active');
  $(".sidebar-nav-custom .nav-link[data-no='" + no + "']").addClass('selected active');
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
  if(!no) return;

  if(no == 2) {
    if(gallery !== undefined && $('.gallery-slider').hasClass('slick-initialized')) {
      $('.gallery-slider').slick('unslick');
    }
    setupGallery();
  }

  $('.cd-hero-slider > li').removeClass('selected').hide();
  var $target = $('.cd-hero-slider > li[data-page-no="' + no + '"]');
  var displayMode = (no == 2 || no == 5) ? 'block' : 'flex';
  $target.css('display', displayMode).hide().fadeIn(300).addClass('selected');
  window.scrollTo({ top: 0, behavior: 'smooth' });
  var pageWrapper = document.getElementById('page-content-wrapper');
  if (pageWrapper) {
    pageWrapper.scrollTo({ top: 0, behavior: 'smooth' });
  }

  // OPTIMIZACIÓN DE RENDIMIENTO DE VIDEOS POR PANTALLA
  if (typeof handlePageVideoPlayback === 'function') {
    handlePageVideoPlayback(no);
  } else {
    var heroVideo = document.getElementById('hero-main-video');
    if (no == 1) {
      if (heroVideo) {
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
      setTimeout(checkRevealElements, 100);
      setTimeout(checkRevealElements, 400);
    }
    if (no == 2) {
      if (typeof syncServiceVideosOnPage === 'function') {
        setTimeout(syncServiceVideosOnPage, 200);
      } else if (typeof playRoxarVideo === 'function') {
        setTimeout(playRoxarVideo, 200);
      }
    }
  }
}

$(window).on('load', function() {
  $('body').addClass('loaded');
  openPage(1);
  highlightMenu(1);
});

jQuery(function() {
    $(document).on('click', '.tm-page-link', function(e){
      e.preventDefault();
      var pageNo = $(this).data('page-no');
      if(pageNo) {
        openPage(pageNo);
        highlightMenu(pageNo);
      }
    });

    $(document).on('click', ".sidebar-nav-custom .nav-link, .navbar .navbar-nav > .nav-item > a.nav-link", function(e){
      e.preventDefault();
      var pageNo = $(this).attr('data-no') || $(this).data('no');

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
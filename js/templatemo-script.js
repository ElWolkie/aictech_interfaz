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
  gallery = $('.gallery-slider').slick({
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

function openPage(no) {
  if(!no) return;

  if(no == 2) {
    if(gallery == undefined) {
      setupGallery();
    } else {
      $('.gallery-slider').slick('unslick');
      setupGallery();
    }    
  }

  $('.cd-hero-slider > li').removeClass('selected').hide();
  var $target = $('.cd-hero-slider > li[data-page-no="' + no + '"]');
  $target.css('display', 'flex').hide().fadeIn(300).addClass('selected');
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
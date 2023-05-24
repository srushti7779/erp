jQuery(function ($) {
    $(".nav-item a")
        .click(function(e) {
            var link = $(this);

            var item = link.parent("li");
            
            if (item.hasClass("active1")) {
                item.removeClass("active1").children("a").removeClass("active1");
            } else {
                item.addClass("active1").children("a").addClass("active1");
            }

            if (item.children("ul").length > 0) {
                var href = link.attr("href");
                link.attr("href", "#");
                setTimeout(function () { 
                    link.attr("href", href);
                }, 300);
                e.preventDefault();
            }
        })
        .each(function() {
            var link = $(this);
            if (link.get(0).href === location.href) {
                link.addClass("active1").parents("li").addClass("active1");
                return false;
            }
        });
});



jQuery(function ($) {
    $(".menu .nav-item a")
        .click(function(e) {
            var link = $(this);

            var item = link.parent("li");
            
            if (item.hasClass("active1")) {
                item.removeClass("active1").children("a").removeClass("active1");
            } else {
                item.addClass("active1").children("a").addClass("active1");
            }

            if (item.children("ul").length > 0) {
                var href = link.attr("href");
                link.attr("href", "#");
                setTimeout(function () { 
                    link.attr("href", href);
                }, 300);
                e.preventDefault();
            }
        })
        .each(function() {
            var link = $(this);
            if (link.get(0).href === location.href) {
                link.addClass("active1").parents("li").addClass("active1");
                return false;
            }
        });
});



$( document ).ready(function() {

    $( ".cross" ).hide();
    $( ".menu" ).hide();
    $( ".hamburger" ).click(function() {
    $( ".menu" ).slideToggle( "slow", function() {
    $( ".hamburger" ).hide();
    $( ".cross" ).show();
    });
    });
    
    $( ".cross" ).click(function() {
    $( ".menu" ).slideToggle( "slow", function() {
    $( ".cross" ).hide();
    $( ".hamburger" ).show();
    });
    });
    
});


// debounce from underscore.js
function debounce(func, wait, immediate) {
	var timeout;
	return function() {
		var context = this, args = arguments;
		var later = function() {
			timeout = null;
			if (!immediate) func.apply(context, args);
		};
		var callNow = immediate && !timeout;
		clearTimeout(timeout);
		timeout = setTimeout(later, wait);
		if (callNow) func.apply(context, args);
	};
};

// use x and y mousewheel event data to navigate flickity
function slick_handle_wheel_event(e, slick_instance, slick_is_animating) {
  // do not trigger a slide change if another is being animated
  if (!slick_is_animating) {
    // pick the larger of the two delta magnitudes (x or y) to determine nav direction
    var direction =
      Math.abs(e.deltaX) > Math.abs(e.deltaY) ? e.deltaX : e.deltaY;

    console.log("wheel scroll ", e.deltaX, e.deltaY, direction);

    if (direction > 0) {
      // next slide
      slick_instance.slick("slickNext");
    } else {
      // prev slide
      slick_instance.slick("slickPrev");
    }
  }
}

// debounce the wheel event handling since trackpads can have a lot of inertia
var slick_handle_wheel_event_debounced = debounce( 
  slick_handle_wheel_event
  , 100, true
);

// init slider 
const slick_2 = $(".slides");
slick_2.slick({
  vertical: true,
  verticalSwiping: true,
  arrows: false
});
var slick_2_is_animating = false;

slick_2.on("afterChange", function(index) {
  console.log("Slide after change " + index);
  slick_2_is_animating = false;
});

slick_2.on("beforeChange", function(index) {
  console.log("Slide before change " + index);
  slick_2_is_animating = true;
});

slick_2.on("wheel", function(e) {
  slick_handle_wheel_event_debounced(e.originalEvent, slick_2, slick_2_is_animating);  
});


$('[data-fancybox="gallery"]').fancybox({
  baseClass : 'fancybox-custom-layout',
  buttons: [
    "slideShow",
    "thumbs",
    "zoom",
    "fullScreen",
    "download",
    "share",
    "close",
  ],
  loop: false,
  protect: true
});
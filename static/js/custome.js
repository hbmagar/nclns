
// script for tesimonials carousel slider 
$(document).ready(function() {
    initializeCarousel();
    
    function initializeCarousel() {
        $("#owl-demo2").owlCarousel({
            loop: true,
            nav: false,
            margin: 50,
            responsiveClass: true,
            autoplay: true,
            autoplayTimeout: 5000,
            autoplaySpeed: 1000,
            autoplayHoverPause: false,
            responsive: {
                0: { items: 1, nav: false },
                736: { items: 1, nav: false },
                991: { items: 2, margin: 30, nav: false },
                1080: { items: 2, nav: false }
            }
        });
    }
});

//______________exprience data count____________________
(function ($) {
	$.fn.countTo = function (options) {
		options = options || {};

		return $(this).each(function () {
			// set options for current element
			var settings = $.extend({}, $.fn.countTo.defaults, {
				from: $(this).data('from'),
				to: $(this).data('to'),
				speed: $(this).data('speed'),
				refreshInterval: $(this).data('refresh-interval'),
				decimals: $(this).data('decimals')
			}, options);

			// how many times to update the value, and how much to increment the value on each update
			var loops = Math.ceil(settings.speed / settings.refreshInterval),
				increment = (settings.to - settings.from) / loops;

			// references & variables that will change with each update
			var self = this,
				$self = $(this),
				loopCount = 0,
				value = settings.from,
				data = $self.data('countTo') || {};

			$self.data('countTo', data);

			// if an existing interval can be found, clear it first
			if (data.interval) {
				clearInterval(data.interval);
			}
			data.interval = setInterval(updateTimer, settings.refreshInterval);

			// initialize the element with the starting value
			render(value);

			function updateTimer() {
				value += increment;
				loopCount++;

				render(value);

				if (typeof (settings.onUpdate) == 'function') {
					settings.onUpdate.call(self, value);
				}

				if (loopCount >= loops) {
					// remove the interval
					$self.removeData('countTo');
					clearInterval(data.interval);
					value = settings.to;

					if (typeof (settings.onComplete) == 'function') {
						settings.onComplete.call(self, value);
					}
				}
			}

			function render(value) {
				var formattedValue = settings.formatter.call(self, value, settings);
				$self.html(formattedValue);
			}
		});
	};

	$.fn.countTo.defaults = {
		from: 0,               // the number the element should start at
		to: 0,                 // the number the element should end at
		speed: 1000,           // how long it should take to count between the target numbers
		refreshInterval: 1,  // how often the element should be updated
		decimals: 0,           // the number of decimal places to show
		formatter: formatter,  // handler for formatting the value before rendering
		onUpdate: null,        // callback method for every time the element is updated
		onComplete: null       // callback method for when the element finishes updating
	};

	function formatter(value, settings) {
		return value.toFixed(settings.decimals);
	}
}(jQuery));

jQuery(function ($) {
	// custom formatting example
	$('.count-number').data('countToOptions', {
		formatter: function (value, options) {
			return value.toFixed(options.decimals).replace(/\B(?=(?:\d{3})+(?!\d))/g, ',');
		}
	});

	// start all the timers
	$('.timer').each(count);

	function count(options) {
		var $this = $(this);
		options = $.extend({}, options || {}, $this.data('countToOptions') || {});
		$this.countTo(options);
	}
});
//______________end exprience data count____________________

// slide of product
$(function() {
    $('.owl-three').owlCarousel({
        loop: true,
        stagePadding: 20,
        margin: 20,
        autoplay: true,
        autoplayTimeout: 5000,
        autoplaySpeed: 1000,
        autoplayHoverPause: false,
        nav: true,
        responsive: {
            0: { 
				items: 1 
			},
            600: { 
				items: 2
			},
            991: { 
				items: 3 
			},
            1200: { 
				items: 4 
			},
            1320: { 
				items: 5 
			}
        }
    });
});

// partner logo marquee script
$(document).ready(function () {
	// Duplicate logos for seamless scrolling
	const originalLogos = $('.partner').html();
	$('.partner').append(originalLogos);

	// Initialize marquee
	$('.partner').marquee({
		duration: 130000,
		gap: 0,
		delayBeforeStart: 0,
		direction: 'left',
		duplicated: true,
		pauseOnHover: true,
		startVisible: true
	});
});

// prouduct list at home
$(function() {
    $(".productlist").flexisel({
        visibleItems: 7,
        animationSpeed: 1000,
        autoPlay: true,
        autoPlaySpeed: 3000,
        pauseOnHover: true,
        enableResponsiveBreakpoints: true,
        responsiveBreakpoints: {
            portrait: { changePoint: 480, visibleItems: 4 },
            landscape: { changePoint: 640, visibleItems: 5 },
            tablet: { changePoint: 768, visibleItems: 6 }
        }
    });
});

// Navbar scroll effect
window.addEventListener("scroll", function () {
    const navbar = document.getElementById("main-navbar");
    const logo = document.getElementById("navbar-logo");
    
    // Get logos from data attributes
    const defaultLogo = logo.getAttribute('data-default-logo');
    const scrolledLogo = logo.getAttribute('data-scrolled-logo');
    
    if (window.scrollY > 50) {
        navbar.classList.add("scrolled");
        if (scrolledLogo) {
            logo.src = scrolledLogo;
        }
    } else {
        navbar.classList.remove("scrolled");
        if (defaultLogo) {
            logo.src = defaultLogo;
        }
    }
});

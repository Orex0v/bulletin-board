<<<<<<< HEAD
/**
 * jQuery Opacity Rollover plugin
 *
 * Copyright (c) 2009 Trent Foley (http://trentacular.com)
 * Licensed under the MIT License:
 *   http://www.opensource.org/licenses/mit-license.php
 */
;(function($) {
	var defaults = {
		mouseOutOpacity:   0.67,
		mouseOverOpacity:  1.0,
		fadeSpeed:         'fast',
		exemptionSelector: '.selected'
	};

	$.fn.opacityrollover = function(settings) {
		// Initialize the effect
=======
/**
 * jQuery Opacity Rollover plugin
 *
 * Copyright (c) 2009 Trent Foley (http://trentacular.com)
 * Licensed under the MIT License:
 *   http://www.opensource.org/licenses/mit-license.php
 */
;(function($) {
	var defaults = {
		mouseOutOpacity:   0.67,
		mouseOverOpacity:  1.0,
		fadeSpeed:         'fast',
		exemptionSelector: '.selected'
	};

	$.fn.opacityrollover = function(settings) {
		// Initialize the effect
>>>>>>> c1b0d7921e9594c488cb726004560dff0c008316
		$.extend(this, defaults, settings);

		var config = this;

		function fadeTo(element, opacity) {
			var $target = $(element);
			
			if (config.exemptionSelector)
				$target = $target.not(config.exemptionSelector);	
			
			$target.fadeTo(config.fadeSpeed, opacity);
		}

		this.css('opacity', this.mouseOutOpacity)
			.hover(
				function () {
					fadeTo(this, config.mouseOverOpacity);
				},
				function () {
					fadeTo(this, config.mouseOutOpacity);
				});
<<<<<<< HEAD

		return this;
	};
})(jQuery);
=======

		return this;
	};
})(jQuery);
>>>>>>> c1b0d7921e9594c488cb726004560dff0c008316

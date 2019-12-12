jQuery(window).on('load', function() {
    "use strict";
    
    $(".preloader").addClass("hide-preloader");
});


jQuery(document).ready(function($) {
    "use strict";
    
    $(".background-content.parallax-on").parallax({
        scalarX: 24,
        scalarY: 15,
        frictionX: 0.1,
        frictionY: 0.1,
    });
});
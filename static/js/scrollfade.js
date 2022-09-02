/* Fade #main-nav on scroll */
$(document).ready(function(){
    $(window).scroll(function(){
        $("#main-nav").css("opacity", 1 - $(window).scrollTop() / ($('#main-nav').height() / 2));
        $("#topnav").css("opacity", 1 - $(window).scrollTop() / ($('#topnav').height() / 0.01));
    });
});

/* Custom js */
$(document).ready(function(){
    // Fade #sub-nav on scroll
    $(window).scroll(function(){
        $("#sub-nav").css("opacity", 1 - $(window).scrollTop() / ($('#sub-nav').height() / 2));
        $("#topnav").css("opacity", 1 - $(window).scrollTop() / ($('#topnav').height() / 0.01));
    });

    // Dropdown list display on hover
    $('.dropdown').hover(function(){
        $('.auto-dropdown', this).trigger('click');
    });

    // Control property choice list on book/choose/ booking-choose-property.html
    $('#choice-list a').on('click', function (e) {
        e.preventDefault()
        $(this).tab('show')
    });
});

/* Fade #main-nav on scroll */
$(document).ready(function(){
    $(window).scroll(function(){
        $("#sub-nav").css("opacity", 1 - $(window).scrollTop() / ($('#sub-nav').height() / 2));
        $("#topnav").css("opacity", 1 - $(window).scrollTop() / ($('#topnav').height() / 0.01));
    });

    $('.dropdown').hover(function(){
        $('.auto-dropdown', this).trigger('click');
    });

    $('#choice-list a').on('click', function (e) {
        e.preventDefault()
        $(this).tab('show')
    });

    // $('.auto-dropdown').onload(function(){
    //     // this.style.opacity = "100%";
    //     this.style.span.hover.transition = "1.3s";
    // });
});


/* Fade in property detail on selection of search results list item */ 
// $(document).ready(function(){
//     $('#choice-list a').on('click', function (e) {
//         e.preventDefault()
//         $(this).tab('show')
//     });
// });


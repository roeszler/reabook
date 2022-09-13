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

    // // Make table rows hyperlinks
    // $('.row-hlink').on('click', function (e) {
    //     e.preventDefault()
    //     $(this).open(["{% url 'property_detail' prop.id %}"])
    //     // $(this).tab('show')
    // });

    let checkboxes = $("input[type=checkbox][name=property_to_view]")
    let selectedToView = [];
    
    // Attach a change event handler to the checkboxes.
    checkboxes.change(function viewingCheckbox() {
        selectedToView = checkboxes
            .filter(":checked") // Filter out unchecked boxes.
            .map(function () { // Extract values using jQuery map.
                return this.value;
            }).get() // Get array.
            
        // html = selectedToView.array.forEach(element => {
        //     '<th scope="row" class="row-hlink"><a href="{% url "property_detail" prop.id %}" target="_blank">{{ prop.id }}</a></th>'
        // });
        // document.getElementsByClassName("properties-to-view").innerHTML = html;
        // document.getElementsByClassName("properties-to-view").innerHTML = selectedToView;
        
        document.getElementById("properties-to-view").innerHTML = selectedToView;
        

        console.log(selectedToView);
        return selectedToView;
    });
});

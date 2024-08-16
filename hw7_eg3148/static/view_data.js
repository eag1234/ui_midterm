$(document).ready(function(){
    $(".popular-item").on('click', function () {
        let item_id = $(this).data('item-id');
        window.location.href = '/view/' + item_id;
    });

    $("#reset").on('click', function () {
        if(window.confirm("Are you sure you want to discard your changes?")){
            let item_id = $(this).data('item-id');
            window.location.href = '/view/' + item_id;
        }
        else{
            event.preventDefault();
        }
    });

    $("#button").on('click', function() {
        let item_id = $(this).data('item-id');
        window.location.href = '/edit/' + item_id;
    })

    // function highlightSearch(query) {
    //     var title = $('#highlighted-title').text();
    //     var regex = new RegExp(query, 'gi');
    //     var highlightedTitle = title.replace(regex, function (match) {
    //         return '<span class="highlight">' + match + '</span>';
    //     });
    //     $('#highlighted-title').html(highlightedTitle);
    // }
    function highlightSearch(elementId, title, query) {
        var regex = new RegExp(query, 'gi');
        var highlightedTitle = title.replace(regex, function (match) {
            return '<span class="highlight">' + match + '</span>';
        });
        $(elementId).html(highlightedTitle);
    }
    // $("#submit").on('click', function(event){
    //     event.preventDefault();  // Prevent the default form submission

    //     let formData = $(this).serialize();
    //     let item_id = $(this).data("item-id")
    //     // $.ajax({
    //     //     url: '/edit' + item_id,
    //     //     method: 'POST',
    //     //     data: formData,  
    //     //     success: function(response) {
    //     //         let viewLink = '/view/' + item_id;
    //     //         window.location.href = viewLink;
    //     //     },
    //     //     error: function(error) {
    //     //         console.error('Error adding title:', error);
    //     //     }
    //     // });
    // });

})
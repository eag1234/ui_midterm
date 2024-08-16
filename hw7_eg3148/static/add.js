$(document).ready(function(){
    $("#addform").submit(function(event){
        event.preventDefault();  // Prevent the default form submission

        let formData = $(this).serialize();
        console.log(formData)
        $.ajax({
            url: '/add',
            method: 'POST',
            data: formData,  
            success: function(response) {
                $("#successMessage").show();
                $("#addform")[0].reset();
                $("#title").focus();

                let itemId = response.result['Id'];
                let viewLink = '/view/' + itemId;
                $("#seeItHere").attr('href', viewLink);
            },
            error: function(error) {
                console.error('Error adding title:', error);
            }
        });
    });

    $("#successMessage").hide();

});
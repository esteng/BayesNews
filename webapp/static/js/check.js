$(function() {
    $('#check').click(function() {
 
        $.ajax({
            url: '/check',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                document.write(response);
            },
            error: function(error) {
                document.write(error);
            }
        });
    });
});
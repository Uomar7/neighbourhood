$(document).ready(function () {
    $('#form').submit(function (event) {
        event.preventDefault()
        form = $('#form')
        console.log(form);
        
        function create_post(){
            console.log($('#comment-text').val());

            $.ajax({
                url : '/ajax/comments/',
                type : 'POST',
                data: {the_post: $('#post-text').val()},
                dataType: 'json',
                success:function(json){
                  $('#comment-text').val('')  
                },

            })
        
        }
    }) // End of submit event

}) // End of document ready function
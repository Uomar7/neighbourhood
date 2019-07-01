$(document).ready(function () {
    $('form').submit(function (event) {
        event.preventDefault()
        form = $('form')

        $.ajax({
            'url':'/ajax/comments/',
            'type':'POST',
            'data':form.serialize(),
            'dataType':'json',
            'success':function(data){
                alert(data['success'])
            }
        })
        $('#_review').val('')
    }) // End of submit event

}) // End of document ready function
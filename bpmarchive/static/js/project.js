/* Project specific Javascript goes here. */
$(document).ready(function () {

    $('#genre-create-message').hide();

    $("#genre_select").select2({
        minimumInputLength: 2,
        placeholder: "select a genre",
        ajax: {
            //url: "/artists/genres/?format=json",
            url: "/artists/genres/search?format=json",
            dataType: 'json',
            data: function (term, page) {
                return {
                    q : term
                };
            },
            results: function (data) {
                return { results: data };
            }
        },
        formatResult: formatGenreList,
        formatSelection: function(item) {
            return item.genretype + " > " + item.name;
        }
    });

    $.fn.modal.Constructor.prototype.enforceFocus = function() {};
    $("#genre_type").select2({
        placeholder: "Select a type"
    });

    var genreFrm = $('#genre_create_form');

    genreFrm.submit(function () {
        $.ajax({
            type: "POST",
            //type: $(this).attr('method'),
            //url: $(this).attr('action'),
            url: '/artists/genreCreate/',
            data: genreFrm.serialize(),
            //data: $(this).serialize(),
            success: function (data) {
                $('#genre-create-message').show().html("<strong>Success</strong> Genre Added");
            }

        });
    });

});

function formatGenreList(data) {
    console.log(data);
    return data.genretype + " > " + data.name;
}

/* Project specific Javascript goes here. */
$(document).ready(function() {
    $("#genre_select").select2({
        minimumInputLength: 2,
        placeholder: "select a genre",
        ajax: {
            url: "/artists/genres/?form=json",
            dataType: 'json',
            /*
            data: function (term, page) {
                return {
                    q: term
                };
            },
            */
            results: function (data) {
                return { results: data };
            }
        },
        formatResult: formatGenreList
    });

});

function formatGenreList(data) {
    return data.genretype + " > " + data.name;
}

$.get('https://swapi-api.alx-tools.com/api/films/?format=json', (data) => {
    $.each(data.results, (idx, movie) => {
        $('div#list_movies').append(`<li>${movie?.title}</li>`);
        });
});

let url = 'http://swapi.co/api/films/?format=json'
$.get(url, function ( data ) {
  data.results.map(function (x) {
    $('#list_movies').append('<li>' + x.title + '</li>');
  });
});

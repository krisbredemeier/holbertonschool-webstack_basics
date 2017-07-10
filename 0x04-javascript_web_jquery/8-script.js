// $.get('http://swapi.co/api/films/?format=json', function(data) {
//   let obj = jQuery.parseJSON( '{ "title": "A New Hope" }' );
// });
$.get('http://swapi.co/api/films/?format=json', function ( data ) {
  data.results.map(fucntion (x) {
    $("#list_movies").append('<li>' + x.title + '</li>');
  });
});

$.get('http://swapi.co/api/people/5/?format=json', function(data) {
  let name = (data.name);
  $( "#character" ).text( name );
});

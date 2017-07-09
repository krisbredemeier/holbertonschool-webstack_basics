$.get('http://swapi.co/api/people/5/?format=json', function() {
  $('#character').each(function() {
    $(this).href = (this).href.replace("5", "1");
  });
});

let url = 'http://swapi.co/api/people/5/?format=json'

$('#character').each(function(){
this.href = this.href.replace("5", "1");
});

$("#add_item").on('click', function () {
  $('ul .my_list').append(
      $('<li>').html('Item'));
});

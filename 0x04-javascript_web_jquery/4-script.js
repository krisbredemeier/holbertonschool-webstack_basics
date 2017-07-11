$("#toggle_header").on('click', function () {
    let element = $('header').attr('class');
    if (element == 'green') {
        $('header').removeClass("green");
        $('header').addClass("red");
    } else {
        $('header').removeClass("red");
        $('header').addClass("green");
    }
});

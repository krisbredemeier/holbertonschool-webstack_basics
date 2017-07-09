<script>
$("#toggle_header").on('click', function () {
    let element = $(this).attr('class');
    if (element == 'green') {
        $(this).removeClass("green");
        $(this).addClass("red");
    } else {
        $(this).removeClass("red");
        $(this).addClass("green");
    }
});
</script>

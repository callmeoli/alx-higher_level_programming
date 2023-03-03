/**
 * Script that adds the class red to the <header>
 * element when the user click on the tag DIV#red_header
 */
$('DIV#red_header').click(() => {
    $('header').addClass('red');
});
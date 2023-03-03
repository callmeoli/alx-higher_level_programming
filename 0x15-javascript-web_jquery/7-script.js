/**
 * Script that fetch the character name  from  this
 */

$.ajax({
    url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
    success: result => {
        $('DIV#character').text(result.name);
    }
});

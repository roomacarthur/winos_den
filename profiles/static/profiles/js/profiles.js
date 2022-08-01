
var countrySelected = $('#id_user_country').val();
if(!countrySelected) {
    $('#id_user_country').css('color', '#aab7c4');
};
$('#id_user_country').change(function() {
    countrySelected = $(this).val();
    if(!countrySelected) {
        $(this).css('color', '#aab7c4');
    } else {
        $(this).css('color', '#046865ff');
    }
});
var stripePublicKey = $('#id_stripe_public_key').text().slice(1,-1);
var clientSecret = $('#id_client_secret').text().slice(1,-1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();
var style = {
    base: {
        color: '#5f8785',
        fontFamily: 'Verdana, Geneva, Tahoma, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};

var card = elements.create('card', {style: style});
card.mount('#card-element');

//card element real time validation error handling.
card.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('card-errors');
    //if there is an error message return html content('input')
    if (event.error) {
        var input = `
        <span class="text-danger">
            <i class="fa-solid fa-circle-exclamation"></i>
            ${event.error.message}
        </span>`;
        $(errorDiv).html(input);
    // else return empty string to display nothing.
    } else {
        errorDiv.textContent = '';
    }
});

//STRIPE form submission handling
var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev){
    ev.preventDefault();
    //disable card/submit to prevent multiple attempts.
    card.update({'disabled': true});
    $('#submit-button').attr('disabled', true);
    var saveInfo = Boolean($('#id-save-info').attr('checked'));
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    var postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
        'save_info': saveInfo,
    };
    var url = '/checkout/cache_checkout_data/';

    $.post(url, postData).done(function(){
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
                billing_details: {
                    name: $.trim(form.full_name.value),
                    phone: $.trim(form.phone_number.value),
                    email: $.trim(form.email.value),
                    address:{
                        line1: $.trim(form.street_address_1.value),
                        line2: $.trim(form.street_address_2.value),
                        city: $.trim(form.city.value),
                        country: $.trim(form.country.value),
                    }
                }
            },
            /* 
            Due to age restrictions, shipping is locked to billing address
            but with future updates and other age verification methods
            separate shipping addresses will be an option. 
            */ 
            shipping: {
                name: $.trim(form.full_name.value),
                phone: $.trim(form.phone_number.value),
                address:{
                    line1: $.trim(form.street_address_1.value),
                    line2: $.trim(form.street_address_2.value),
                    city: $.trim(form.city.value),
                    postal_code: $.trim(form.post_code.value),
                    country: $.trim(form.country.value),
                }
            },
        }).then(function(result) {
            if (result.error) {
                var errorDiv = document.getElementById('card-errors');
                var input = `
                <span class="text-danger">
                    <i class="fa-solid fa-circle-exclamation"></i>
                    ${result.error.message}
                </span>`;
                $(errorDiv).html(input);
                //if error set disabled for re attempt.
                card.update({'disabled': false});
                $('#submit-button').attr('disabled', false);
            } else {
                if (result.paymentIntent.status === 'succeeded'){
                    form.submit();
                }
            }
        });
    }).fail(function () {
        location.reload();
    });
});


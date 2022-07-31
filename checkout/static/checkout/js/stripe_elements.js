
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
card.mount('#card-element')

//card element real time validation error handling.
card.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('card-errors');
    //if there is an error message return html content('input')
    if (event.error) {
        let input = `
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
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        }
    }).then(function(result) {
        if (result.error) {
            var errorDiv = document.getElementById('card-errors');
            let input = `
            <span class="text-danger">
                <i class="fa-solid fa-circle-exclamation"></i>
                ${result.error.message}
            </span>`;
            $(errorDiv).html(input);
            //if error set disabled for re attempt.
            card.update({'disabled': false});
            $('#submit-button').attr('disabled', false);
        } else {
            if (result,intent.status === 'succeeded'){
                form.submit();
            }
        }
    });
});
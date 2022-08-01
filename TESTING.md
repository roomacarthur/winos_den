## HTML Validators

| Template | Pass? | Image|
| ------------- | -- | ------------- |
| base.html | Register an account | So That I can save my details and make purchases. |
| index.html | Register an account | So That I can save my details and make purchases. |
| contact_us.html | Register an account | So That I can save my details and make purchases. |

## CSS Validators

| Template | Pass? | Image|
| ------------- | -- | ------------- |
| style.css | Register an account | So That I can save my details and make purchases. |
| index.html | Register an account | So That I can save my details and make purchases. |
| contact_us.html | Register an account | So That I can save my details and make purchases. |


## User Stories Tests. 

1. **TEST:** Signing up functionality. 
    - **RESULT** = Successfully created a new account, received email authentication, and was able to log in after email activation. Prompted with success message when logged in.  
    [**PASS Image**](https://github.com/roomacarthur/winos_den/blob/main/documentation/images/login.png)

2. **TEST:** Log in/out
    - **RESULT** = Easily able to log into the site once Sign up is complete, Log out prompts for confirmation. Upon successful logout I was given a message to tell me I had completed logout.
    [**PASS Image**](https://github.com/roomacarthur/winos_den/blob/main/documentation/images/logout.png)
    [**PASS Image**](https://github.com/roomacarthur/winos_den/blob/main/documentation/images/logoutconfirm.png)

3. **TEST:** Reset Password.
    - **RESULT** = When logging in, I am given the option to reset forgotten password, doing so by submitting my email address allows for a reset link to be emailed to me.   
    [**PASS Image**](https://github.com/roomacarthur/winos_den/blob/main/documentation/images/passresetemail.png)

4. **TEST:** View Products.
    - **RESULT** = Easily view the products that are listed on the site. 
    [**PASS Image**](https://github.com/roomacarthur/winos_den/blob/main/documentation/images/products_list.png)

5. **TEST:** View Product details.
    - **RESULT** = when clicking on a product from the main products page, I can clearly see the product and all it's details, I have the option to select QTY and add to cart. this Functionality works flawlessly.
    [**PASS Image**](https://github.com/roomacarthur/winos_den/blob/main/documentation/images/product_details.png)

5. **TEST:** View cart
    - **RESULT** = When I have no items in my cart it shows an empty cart but as I add items they are populated into the cart, this includes qty, sub total and a cart total. I am given the option to checkout or continue shopping.
    [**PASS Image**](https://github.com/roomacarthur/winos_den/blob/main/documentation/images/cart.png)

5. **TEST:** Add details at checkout and complete purchase. 
    - **RESULT** = Payments are handled bys stripe and are very secure, Payment details are taken at the checkout page, the ability to pay twice due to miss clicks is removed and stripe webhooks listen for actions incase the internal functions miss anything. If user is logged in, they are able to save personal info for late user, this works flawlessly, upon saving info it is visible within the user profile seciton.
    **PASS**
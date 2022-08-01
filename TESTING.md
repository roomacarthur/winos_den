# HTML Validators

Django Html Syntax throws errors in the [W3C Validator](https://validator.w3.org/)

Ignoring the errors shwon from the django tags the results are as follows:

index.html -- **PASS**

contact_us.html -- **PASS**

subscribe.html -- **PASS**

product_delete.html -- **PASS**

product_details.html -- **PASS**

product_edit.html -- **PASS**

product_list.html -- **PASS**

product_new.html -- **PASS**

profile.html -- **PASS**

review.html -- **PASS**

base.html -- 2x errors - (additional closing div and p elements.) removed and  -- **PASS**

cart.html -- **PASS**

checkout.html -- **PASS**

checkout_success.html -- **PASS**



# CSS Validators

Checkout/css -- **PASS**

Profiles/css -- **PASS**

Static/css -- **PASS**

# JS Validator. 

ALL JS code passed JSHint, with the stipe_elements showing 2 errors that Template literals aren't supported in versions prior to ES6 but this isn't an issue for us and can be ignored. 


# User Stories Tests. 

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

    [**PASS Image**](https://github.com/roomacarthur/winos_den/blob/main/documentation/images/checkout.png)

    [**PASS Image**](https://github.com/roomacarthur/winos_den/blob/main/documentation/images/checkout_details.png)

    [**PASS Image**](https://github.com/roomacarthur/winos_den/blob/main/documentation/images/oder_complete.png)

    [**PASS Image**](https://github.com/roomacarthur/winos_den/blob/main/documentation/images/user_profiles_save.png)

6. **TEST** See my order history. 
    - **RESULT** = Upon clicking on user profile in the account dropdown in the navbar. I can see my saved information and also a list of my previous orders, I am able to click into each order to see the confirmation page. 

    [**PASS Image**](https://github.com/roomacarthur/winos_den/blob/main/documentation/images/user_profiles_save.png)

    [**PASS Image**](https://github.com/roomacarthur/winos_den/blob/main/documentation/images/old_order.png)

6. **TEST** Search bar functionality. 
    - **RESULT** = From the surface level the search function works flawlessly. The search query is is checked for in product name and description. To test this further, I added "merlot" to the description of a white wine.

    [**PASS Image**](https://github.com/roomacarthur/winos_den/blob/main/documentation/images/white_search.png)

    [**PASS Image**](https://github.com/roomacarthur/winos_den/blob/main/documentation/images/merlot_search.png)

6. **TEST** edit product.
    - **RESULT** = as an admin user I am able to click on a product to navigate to its product detail view, from here I have the option to edit or delete a product. Clicking on edit, opens the product's model in a form. Upon successful edit I am given a success message. If opting to delete product I am prompted with a confirmation screen giving me the option to delete or return to products. upon successful deletion I am given a success message.

    [**PASS Image**](https://github.com/roomacarthur/winos_den/blob/main/documentation/images/edit_delete.png)

    [**PASS Image**](https://github.com/roomacarthur/winos_den/blob/main/documentation/images/product_edit.png)

    [**PASS Image**](https://github.com/roomacarthur/winos_den/blob/main/documentation/images/edit_success.png)

    [**PASS Image**](https://github.com/roomacarthur/winos_den/blob/main/documentation/images/delete_conf.png)

    [**PASS Image**](https://github.com/roomacarthur/winos_den/blob/main/documentation/images/delete_success.png)

6. **TEST** Add product.
    - **RESULT** = as an admin user I am able add a product within the Front end UI without accessing the Django based AP. Clicking on "Add New Product" in the account drop down, prompts me with a new template consiting of a Product model form. 

    [**PASS Image**](https://github.com/roomacarthur/winos_den/blob/main/documentation/images/edit_delete.png)

    [**PASS Image**](https://github.com/roomacarthur/winos_den/blob/main/documentation/images/product_edit.png)

    [**PASS Image**](https://github.com/roomacarthur/winos_den/blob/main/documentation/images/edit_success.png)

    [**PASS Image**](https://github.com/roomacarthur/winos_den/blob/main/documentation/images/delete_conf.png)

    [**PASS Image**](https://github.com/roomacarthur/winos_den/blob/main/documentation/images/delete_success.png)



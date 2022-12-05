# TEST 1: Login with valid account information (Issue #19, #79) 
- Navigate to the login page
- Put in valid account info
- ## PASS: You are redirected to the home page
- ## FAIL: You are redirected back to the login page (you my have to login twice in a row)


# TEST 2: Login with invalid account information (Issue #19)
- Navigate to the login page
- Put in invalid account info
- ## PASS: You are redirected to login
- ## FAIL: You login successfully and are redirected to the home page
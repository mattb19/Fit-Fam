# Test 1: Security Questions (#5)
- After inputting acceptable user information at signup the user is redirected to the security questions page
- The user selects the two security Questions from the dropdown bars and inputs their answers to them
    - Issue: The user inputs are not sanitized
- The user selects the submit button
- They are redirected to the home page
- # Pass: They successfully set their security questions and answers
- # Fail: There inputs are not set in the db or they are not successfully redirected
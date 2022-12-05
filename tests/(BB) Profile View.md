# Test 1: ProFile View (Issue #31)
- Select the Profile page at the top of the bar from any page when logged in
- User is redirected to their profile page
- # Pass: The user can see their profile
- # Fail: The page doesn't load the correct profile or doesn't display all of the users' information

# Test 2: Profile Edit View (Issue #31)
- From the Profile Page select the edit button
- User is redirected to ProfileEdit page
- Option1:
- Input Nickname and aboutMe
    - Issue: The user inputs are not sanitized
- select the save button
- Option2:
- Select the cancel button
- Outcome:
- The user is redirected to their profile page
- with any changes they have made
- # Pass: The user is successfully redirected to their profile page
- # Fail: The page doesn't load the correct profile or doesn't display all of the users' information
    - # found Bugs
    - [#72](https://github.com/UNCW-CSC-450/csc450fa22-project-team-2/issues/72)
    - Issue #73 Closed

# Test 3: Reset Password (Issue #31)
- From the Profile page select Reset Password
- User is redirected to security questions check
- The user puts in the answers to their security questions
    - Issue: The user inputs are not sanitized
- The user selects the submit button
- The answers are sent to the backend
- If:
- They match the answers in the database
- Then:
- The user is redirected to the reset password page
- Else:
- The user is redirected back to the check security question page
- In the reset password page the user inputs their new password twice
    - Issue: The user inputs are not sanitized
- If:
- They match the each other
- Then:
- The users password is hashed and set in the db and they are redirected to their profile
- Else:
- The user is redirected back to the reset password
- # Pass: The user can reset their password and is redirected to their profile
- # Fail: The users password is not reset or the profile isn't found
    - # found bugs
    - [#80](https://github.com/UNCW-CSC-450/csc450fa22-project-team-2/issues/80)

# Test 4: Change Security Questions (Issue #31)
- From Profile page select Change Security Questions button
- The user is redirected to the security Questions page
- # Pass: The user is redirected to security Questions page
- # Fail: The user is not redirected to security Questions page
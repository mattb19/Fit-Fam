# Test 1: ProFile View (Issue #31)
- Select the Profile page at the top of the bar from home
- User is redirected to their profile page
- # Pass: the user can see their profile
- # Fail: the page doesn't load the correct profile or doesn't display all of the users' information

# Test 2: Profile Edit View (Issue #31)
- From the Profile Page select the edit button
- User is redirected to ProfileEdit page
- Option1:
- Input Nickname and aboutMe
- select the save button
- Option2:
- Select the cancel button
- Outcome:
- The user is redirected to their profile page
- with any changes they have made
- # Pass: The user is successfully redirected to their profile page
- # Fail: the page doesn't load the correct profile or doesn't display all of the users' information
    - # found Bugs
    - [#72](https://github.com/UNCW-CSC-450/csc450fa22-project-team-2/issues/72)
    - Issue #73 Closed

# Test 1: Reset Password (Issue #31)
- From the Profile page select Reset Password
- User is redirected to security questions check
- # Pass: the user can reset their password and is redirected to their profile
- # Fail: the users password is not reset or the profile isn't found
    - # found bugs
    - #80
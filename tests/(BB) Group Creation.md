# Test 1: Group Creation (Issue #1)
- Select the Groups page at the top of the bar
- Select the "+" icon at the top left of the page next to "Groups"
- Redirects to new page to enter group name
- User enters a group name
- Click "Create Group" to create new group
- User is redirected to home page
- # Pass: User can successfully create a new group that will be displayed on the groups page
- # Fail: User does not enter valid characters that can be stored in a SQL database or no group name

# Test 2: Group Name Exists (Issue #1)
- Select the Groups page at the top of the bar
- Select the "+" icon at the top left of the page next to "Groups"
- Redirects to new page to enter group name
- User enters group name that already exists for them
- Click "Create Group" to create new group
- User is redirected to home page
- # Pass: Users group is created with the same name regardless of existance already
- # Fail: User enters no group name

# Test 3: Viewing Group Feed (Issue #48)
- Select the Groups page at the top of the bar
- User clicks group that they wish to view the feed of
- The Feed is updated to match the group clicked on without refreshing the page
- # Pass: The feed updates successfully and is displayed
- # Fail: The feed does not show up or is still on the main feed

# Test 4: Adding Posts to a Group (Issue #1)
- Select the "+" at the bottom right of the page
- Fill out all required information and change the feed to which is wanted to be posted to
- Select the "Post" option and view your post in the selected feed
- # Pass: User is able to successfully view the post they made where they intended to make it
- # Fail: Post is not visible or is showing up where it is unintended

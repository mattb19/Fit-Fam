# TEST 1: Post Creation (Issue #22)
- Navigate to the create post page using the "+" button in the bottom right of global feed
- Fill out the title and description page with whatever you want
- Click "Post"
- ## PASS: The page redirects to the global feed, your post is displayed
- ## FAIL: Above doesn't happen


# TEST 2: Post Creation Character Count (Issue #22)
- Navigate to the create post page using the "+" button in the bottom right of global feed
- Fill out the title field with as many characters as possible
- Fill out the description field with as many characters as possible
- Click "Post"
- ## PASS: The text fields for title and description will limit you to 255 & 4096 characters respectively
- ## FAIL: The text fields for title and description will let you type more than 255 & 4096 characters respectively

# TEST 3: Post Creation With Image (Issue #2)
- Navigate to the create post page using the "+" button in the bottom right of global feed
- Fill out the title and description page with whatever you want
- Select an image using the "Choose File" button
- Click "Post"
- ## PASS: The page redirects to the global feed, your post is displayed with the image you uploaded
- ## FAIL: Above doesn't happen


# TEST 4: Post Creation With Tag (Issue #36)
- Navigate to the create post page using the "+" button in the bottom right of global feed
- Fill out the title and description page with whatever you want
- Select a tag from the "Choose a tag" dropdown
- Click "Post"
- ## PASS: The page redirects to the global feed, your post is displayed with the tag you selected
- ## FAIL: Above doesn't happen


# TEST 5: Empty Title/Description (Issue #62)
- Navigate to the create post page using the "+" button in the bottom right of global feed
- Leave either the title or description field blank
- Click "Post"
- ## PASS: The text turns red and "Please complete all required * fields" is displayed below "Post" button
- ## FAIL: The page redirects to global feed
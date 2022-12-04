# TEST 1: Post Creation
- Navigate to the create post page using the "+" button in the bottom right of global feed
- Fill out the title and description page with whatever you want
- Click "Post"
- ## PASS: The page redirects to the global feed, your post is displayed
- ## FAIL: Above doesn't happen


# TEST 2: Post Creation With Image
- Navigate to the create post page using the "+" button in the bottom right of global feed
- Fill out the title and description page with whatever you want
- Select an image using the "Choose File" button
- Click "Post"
- ## PASS: The page redirects to the global feed, your post is displayed with the image you uploaded
- ## FAIL: Above doesn't happen


# TEST 3: Post Creation With Tag
- Navigate to the create post page using the "+" button in the bottom right of global feed
- Fill out the title and description page with whatever you want
- Select a tag from the "Choose a tag" dropdown
- Click "Post"
- ## PASS: The page redirects to the global feed, your post is displayed with the tag you selected
- ## FAIL: Above doesn't happen


# TEST 4: Empty Title/Description
- Navigate to the create post page using the "+" button in the bottom right of global feed
- Leave either the title or description field blank
- Click "Post"
- ## PASS: The text turns red and "Please complete all required * fields" is displayed below "Post" button
- ## FAIL: The page redirects to global feed
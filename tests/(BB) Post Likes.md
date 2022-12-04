# TEST 1: Like Post
- Navigate to the global feed by clicking the "Global" button in the navigation bar
- Click the thumbs up emoji at the bottom left of any post
- Refresh the page
- ## PASS: The like count of the post you liked has incremented up by 1
- ## FAIL: Above doesn't happen

# TEST 2: Like Post Multiple Times
- Navigate to the global feed by clicking the "Global" button in the navigation bar
- Click the thumbs up emoji at the bottom left of any post more than 1 time
- Refresh the page
- ## PASS: The like count of the post you liked has incremented up by 1
- ## FAIL: The like count of the post you liked has incremented up by >1
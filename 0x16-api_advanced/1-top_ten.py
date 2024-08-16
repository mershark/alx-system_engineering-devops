#!/usr/bin/python3
"""
Module that contains a function
which queries the Reddit API
"""

import requests

def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts listed for a given subreddit.
    """
    if not subreddit or not isinstance(subreddit, str):
        print(None)
        return

    # Construct the URL for the subreddit's hot posts in JSON format
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    
    # Define headers for the HTTP request, including User-Agent
    headers = {
        "User-Agent": "Python/requests:APIproject:v1.0.0 (by /u/abukiplimo)"
    }
    
    # Define parameters for the request, limit the results to 10 posts
    params = {
        "limit": 10
    }
    
    # Send a GET request to the subreddit's hot posts page
    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        
        # Check if the response status code indicates a not-found error (404) or invalid subreddit
        if response.status_code != 200:
            print(None)
            return
        
        # Parse the JSON response and extract relevant data
        data = response.json().get("data", {})
        posts = data.get("children", [])
        
        # If no posts are found, print None
        if not posts:
            print(None)
            return
        
        # Print the titles of the first 10 hot posts
        for post in posts:
            title = post.get("data", {}).get("title", None)
            if title:
                print(title)
            else:
                print(None)
    except requests.RequestException:
        print(None)

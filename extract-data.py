from mastodon import Mastodon

# Configuration
mastodon_instance_url = "https://mastodon.social/"  # Replace with your instance URL
client_id = "1WoctrZLWQPL77NibHMl2_Z1-S-FidIGE4mWSQ9pGgQ"
client_secret = "i3ad8JJsolOwhSoQt2D7ccy9H-RvZ5YeozqBtKsyIeU"

# Initialize the Mastodon client
mastodon = Mastodon(
    client_id=client_id,
    client_secret=client_secret,
    api_base_url=mastodon_instance_url
)

# Authenticate Your Application (if needed)
# Note: Depending on instance policies, you may or may not need to authenticate.

# Data Extraction
try:
    # Retrieve the latest 10 public posts from the Mastodon instance
    timeline = mastodon.timeline_public(limit=10)

    # Data Analysis and Processing (Example: Count hashtags)
    hashtag_counts = {}
    for post in timeline:
        content = post["content"]
        hashtags = [tag for tag in content.split() if tag.startswith("#")]
        for hashtag in hashtags:
            if hashtag in hashtag_counts:
                hashtag_counts[hashtag] += 1
            else:
                hashtag_counts[hashtag] = 1

    # Print the hashtag counts
    for hashtag, count in hashtag_counts.items():
        print(f"{hashtag}: {count} times")

except Exception as e:
    print(f"An error occurred: {e}")

# Note: Implement rate limiting and pagination as needed, and handle errors robustly.

# Remember to respect the rules and policies of the Mastodon instance.

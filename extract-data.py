from mastodon import Mastodon

# # Replace these with your actual values
# client_id = "1WoctrZLWQPL77NibHMl2_Z1-S-FidIGE4mWSQ9pGgQ"
# client_secret = "i3ad8JJsolOwhSoQt2D7ccy9H-RvZ5YeozqBtKsyIeU"
# access_token = "UkzDemc6h67OZ3mguQWDDb0O0xfJhC750rZp_YgDOIA"
# redirect_uri = "https://reds.com"
# mastodon_instance_url = "https://artsculture.media/explore"

# # Create an instance of the Mastodon class
# mastodon = Mastodon(
#     client_id=client_id,
#     client_secret=client_secret,
#     access_token=access_token,
#     api_base_url=mastodon_instance_url
# )

# # Now you can use the mastodon object to interact with the Mastodon API


# # Fetch recent toots (textual data) from the home timeline
# toots = mastodon.timeline_home(limit=10)

# # Iterate through the retrieved toots and print their content and metadata
# for toot in toots:
#     print(f"Username: {toot['account']['username']}")
#     print(f"Display Name: {toot['account']['display_name']}")
#     print(f"Timestamp: {toot['created_at']}")
#     print(f"Content: {toot['content']}\n")


# # mastodon_instance_url = "https://artsculture.media/explore"
# mastodon_instance_url = "https://hhsocial.de/public"
# mastodon = Mastodon(api_base_url=mastodon_instance_url)

# mastodon.log_in(username="karimasadykova@gmail.com", password="Sojzyn-cusmus-4hynve")

# timeline = mastodon.timeline_public(limit=10)  # Retrieve the latest 10 public posts
# for post in timeline:
#     print(post["content"])  # Print the content of each post

from mastodon import Mastodon

# mastodon_instance_url = "https://hhsocial.de"
mastodon_instance_url = "https://mastodon.social/"
mastodon = Mastodon(api_base_url=mastodon_instance_url)

timeline = mastodon.timeline_public(limit=10)  # Retrieve the latest 10 public posts
for post in timeline:
    print(post["content"])  # Print the content of each post

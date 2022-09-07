from TikTokApi import TikTokApi
print("test")
with TikTokApi() as api:
    for trending_video in api.trending.videos(count=1):
        # Prints the author's username of the trending video.
        print(trending_video.author.username)
#For each channel ID it collects the channel info by making API calls

import channelIdCollector
import videoDataCollector
import requests
import creds

channelNames = []
channelTotalViews = []
channelSubscribers = []
channelVideos = []

APIkey = creds.YOUTUBE_DATA_API
baseChannelUrl = 'https://www.googleapis.com/youtube/v3/channels?'
details = 'snippet,statistics'

for channelId in channelIdCollector.channelIds:
    url = baseChannelUrl + 'part=' + details + '&id=' + channelId + '&key=' + APIkey 
    r = requests.get(url)
    data = r.json()
    channelName = data["items"][0]["snippet"]["title"]
    totalViews = data["items"][0]["statistics"]['viewCount']
    subscribers = data["items"][0]["statistics"]['subscriberCount']
    videos = data["items"][0]["statistics"]['videoCount']
    channelNames.append(channelName)
    channelTotalViews.append(totalViews)
    channelSubscribers.append(subscribers)
    channelVideos.append(videos)
    print("Channel Name: " + channelName, end=' ')
    print("Channel Id: " + channelId, end=' ')
    videoDataCollector.videoIdCollector(channelId, channelName)
    











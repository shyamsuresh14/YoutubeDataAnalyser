#For each channel each the video details are collected by making API calls and collects data of 50 channels at a time

import csvDataWriter
import requests

videoViews = []
videoLikes = []
videoDislikes = []
videoComments = []
videoCategory = []
publishDate = []

#collects video Ids
def videoIdCollector(channelId, channelName):
    VideoIds = []
    baseKeyUrl = 'https://www.googleapis.com/youtube/v3/search?'
    APIkey = 'AIzaSyAKkvtbJheEFYrRseZgyxUyBhy0KXm3wM0'
    details = 'id'
    print('Latest Video Ids: ')
    nextPageToken = ''

    while True: 
        try:
            if not nextPageToken:
                url = baseKeyUrl + 'key=' + APIkey + '&channelId=' + channelId + '&part=' + details + '&order=date&maxResults=50'
            else:
                url = baseKeyUrl + 'key=' + APIkey + '&channelId=' + channelId + '&part=' + details + '&order=date&maxResults=50&pageToken=' + nextPageToken    
            r = requests.get(url)
            data = r.json()
            #totalRes = data["pageInfo"]["totalResults"]
            try:
                nextPageToken =  data["nextPageToken"]
            except:
                print('Token Error - ' + nextPageToken)
                break    
            results = data["pageInfo"]["resultsPerPage"]    
        except:
            print(str(len(VideoIds) + 1) + '). ' + ' Error!!')     

        for i in range(results):
            try:
                if data["items"][i]["id"]["kind"] == "youtube#video":
                    vid = data["items"][i]["id"]["videoId"]
                    print(str(len(VideoIds) + 1) + '). ' + vid)
                    VideoIds.append(vid)
                else:
                    print("Not a video!")    
            except:
                print('Exception')
                break
    videoDataCollection(VideoIds, channelName)

#collects video data
def videoDataCollection(videoIds, channelName):
    categories = {1:'Film & Animation',2:'Autos & Vehicles',10:'Music',
    15:'Pets & Animals',17:'Sports',19:'Travel & Events',
    20:'Gaming',22:'People & Blogs',23:'Comedy',24:'Entertainment',
    25:'News & Politics',26:'How-to & Style',27:'Education',
    28:'Science & Technology',29:'Non-profits & Activism'}

    baseVideoUrl = 'https://www.googleapis.com/youtube/v3/videos?'
    APIkey = 'AIzaSyAKkvtbJheEFYrRseZgyxUyBhy0KXm3wM0'
    details = 'snippet,statistics'

    for videoId in videoIds:
        url = baseVideoUrl + 'part=' + details + '&id=' + videoId + '&key=' + APIkey
        try:
            r = requests.get(url)
        except:
            break    
        data = r.json()
        try: 
            category = categories[int(data["items"][0]["snippet"]["categoryId"])]
        except:
            category = 'Unknown-' + data["items"][0]["snippet"]["categoryId"]     
        try:
            views = data["items"][0]["statistics"]["viewCount"]
        except:
            views = '0'    
        try:
            likes = data["items"][0]["statistics"]["likeCount"]
        except:
            likes = '0'    
        try:
            dislikes = data["items"][0]["statistics"]["dislikeCount"]
        except:
            dislikes = '0'    
        try:
            date = data["items"][0]["snippet"]["publishedAt"]
        except:
            date = 'Nil'    
        try: 
            comments = data["items"][0]["statistics"]["commentCount"]
        except:
            comments = '0'    
        print("Category-" + category + " Views-" + views + " Likes-" + likes + " Dislikes-" + dislikes + " Comments-" + comments)
        videoCategory.append(category)
        videoViews.append(views)
        videoLikes.append(likes)
        videoDislikes.append(dislikes)
        videoComments.append(comments)
        publishDate.append(date[:date.index('T')])

    arrange(channelName)

#arranges the info in the right format to write to the excel file
def arrange(channelName):
    data = []
    for i in range(len(videoCategory)):
        d = []
        d.append(videoCategory[i])
        d.append(videoViews[i])
        d.append(videoLikes[i])
        d.append(videoDislikes[i])
        d.append(videoComments[i])
        d.append(publishDate[i])
        data.append(d)
    csvDataWriter.writer(data, channelName)    
#videoIdCollector('UCXuqSBlHAE6Xw-yeJA0Tunw')
#print(len(VideoIds)) 

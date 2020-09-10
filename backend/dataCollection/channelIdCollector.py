#For each channel in the list of 20 channels, the channel IDs are collected and stored in a list

import requests
import creds

'''channels = ['PewDiePie',
'tseries',
'kidrauhl',
'CanalKondZilla',
'corycotton',
'HolaSoyGerman',
'5-Minute Crafts',
'EdSheeran',
'WWE',
'setindia',
'whinderssonnunes',
'EminemMusic',
'KatyPerryMusic',
'taylorswift',
'elrubiusOMG',
'Rihanna',
'Fernanfloo',
'JuegaGerman',
'onedirectionchannel',
'TheEllenShow']'''
channels = [input()]
channelIds = []

baseChannelUrl = 'https://www.googleapis.com/youtube/v3/channels?'
details = 'id'
APIkey = creds.YOUTUBE_DATA_API

print('ChannelIds: ')

for channel in channels:
    try:
        url = baseChannelUrl + 'part=' + details + '&forUsername=' + channel + '&key=' + APIkey
        
        r = requests.get(url)
        data = r.json()

        cid = data["items"][0]["id"]
        channelIds.append(cid)

        print(channel + ' - ' + cid)
    except Exception as e:
        if channel == '5-Minute Crafts':
            cid = 'UC295-Dw_tDNtZXFeAPAW6Aw'
            print(channel + ' - ' + cid)
            channelIds.append(cid)
        else:    
            print(channel + ' - ' + 'Error!')


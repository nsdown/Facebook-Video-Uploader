#! /usr/bin/python
# -*- coding: utf-8 -*-


#permanent token access instructions:
#http://stackoverflow.com/questions/17197970/facebook-permanent-page-access-token
#http://terminal.jcubic.pl/



print "Content-type: application/json\n\n"
import requests
import feedparser
import json
from USATSportsFacebookDatabase import videoExists
from USATSportsFacebookDatabase  import addVideo

d = feedparser.parse('[Insert Your Feed URL here]')
response_array = []

# -- For each item in the feed
for index, post in enumerate(d.entries):
    if index >= 20:
        break
    #Here we set up a dictionary in order to extract selected data from the original brightcove "post" result
    item = {}
    item['name'] = post.title,
    item['description'] = post.description,
    item['url'] = u"%s" % post.link,
    #item['tags'] = post.media_keywords.split(",")

max_bitrate = 0
    vid_url = None
    videos = post.media_content
    
    # -- For each video in the item
    for video in videos:
        # -- If the video has a value for its bitrate
        if 'bitrate' in video:
            # -- Extract the value of this video's bitrate
            bitrate_str = video['bitrate']
            # -- and convert it to an integer (by default it is a string in the XML)
            curr_bitrate = int(bitrate_str)
            # -- If the bitrate of this video is greater than
            # -- the highest bitrate we've seen, mark this video as the one with
            # -- the highest birate.
            if curr_bitrate > max_bitrate:
                max_bitrate = curr_bitrate
                vid_url = video['url']
# -- This line simply prints out the maximum bitrate and current video URL for each iteration
#print "{} url {}".format(max_bitrate, vid_url)
#print "highest bitrate {} url {}".format(max_bitrate, vid_url)

item['url'] = vid_url
    
    response_array.append(item)
    
    videoUrl = vid_url
    videoName = item['name']
    videoDescription  = item['description']
    
    #print videoUrl
    if videoExists(videoUrl):
        print "This video has already been uploaded to Facebook."


if not videoExists(videoUrl):
    print "Haven't seen", videoUrl, "before, adding it to Facebook!"
        
        #Make our POST request to Facebook Graph API:
        access = '[Insert Your Permanent Page Access Token here]'
        fburl = 'https://graph-video.facebook.com/v2.3/[Insert your Pgae ID here]/videos?access_token='+str(access)
        payload = {'name': '%s' %(videoName), 'description': '%s' %(videoDescription), 'file_url': '%s' %(videoUrl)}
        flag = requests.post(fburl, data=payload).text
        print flag
        fb_res = json.loads(flag)
        if not "error" in fb_res:
            addVideo(videoUrl)
        else:
            print "An error occured uploading to facebook for ", videoUrl



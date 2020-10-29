#github challenge
import requests, json 
from xlwt import *


url = "https://api.github.com/users/andrewbeattycourseware/followers"

response = requests.get(url)
data = response.json()


filename = 'githubusers.json'
with open(filename, 'w') as f:
    json.dump(data, f, indent=4)

'''writing to .xls
w = Workbook()
ws =w.add_sheet('followers')
row = 0;
ws.write(row,0,"login")
ws.write(row,1,"id")
ws.write(row,2,"node_id")
ws.write(row,3,"avatar_url")
ws.write(row,4,"gravatar_id")
ws.write(row,5,"url")
ws.write(row,6,"html_url")
ws.write(row,7,"followers_url")
ws.write(row,8,"following_url")
ws.write(row,9,"gists_url")
ws.write(row,10,"starred_url")
ws.write(row,11,"subscriptions_url")
ws.write(row,12,"organizations_url")
ws.write(row,13,"repos_url")
ws.write(row,14,"events_url")
ws.write(row,15,"received_events_url")
ws.write(row,16,"type")
ws.write(row,17,"site_admin")
row += 1
for follower in data["followers"]:
    ws.write(row,0,follower["login"])
    ws.write(row,1,follower["id"])
    ws.write(row,2,follower["node_id"])
    ws.write(row,3,follower["avatar_url"])
    ws.write(row,4,follower["gravatar_id"])
    ws.write(row,5,follower["url"])
    ws.write(row,6,follower["html_url"])
    ws.write(row,7,follower["followers_url"])
    ws.write(row,8,follower["following_url"])
    ws.write(row,9,follower["gists_url"])
    ws.write(row,10,follower["starred_url"])
    ws.write(row,11,follower["subscriptions_url"])
    ws.write(row,12,follower["organizations_url"])
    ws.write(row,13,follower["repos_url"])
    ws.write(row,14,follower["events_url"])
    ws.write(row,15,follower["received_events_url"])
    ws.write(row,16,follower["type"])
    ws.write(row,17,follower["site_admin"])
    row += 1
w.save('githubusers.xls')'''

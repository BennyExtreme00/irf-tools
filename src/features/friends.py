import api
from pynotifier import Notification
import tkinter
from tkinter import messagebox
import pymsgbox

api = api.LCU()

fake_msg = """
. 
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
System message: Due to the decision of the Player Behavior & Justice, your account has been suspended permanently after this game.
"""

def CopyIcon(name):
    friend = api.get('/lol-summoner/v1/summoners?name=%s' % name).json()
    iconId = friend["profileIconId"]
    api.put('/lol-chat/v1/me', {"icon": iconId})
    pymsgbox.alert(title='IRF Tools', text="{} icon has been copied.".format(name), button='OK')

def CopyStatus(name):
    friends = api.get('/lol-chat/v1/friends').json()
    for i in range(len(friends)):
        if friends[i]["name"] == name:
            accountId = friends[i]["id"]
            break
    friendToCopy = api.get('/lol-chat/v1/friends/{}'.format(accountId)).json()
    statusMessage = friendToCopy["statusMessage"]
    data = api.put('/lol-chat/v1/me', {"statusMessage": statusMessage})
    pymsgbox.alert(title='IRF Tools', text="{} status has been copied.".format(name), button='OK')

def RemoveAllFriends():
    friends = api.get('/lol-chat/v1/friends').json()
    for i in range(len(friends)):
        api.delete('/lol-chat/v1/friends/' + friends[i]["puuid"])
    pymsgbox.alert(title='IRF Tools', text="{} friends has been removed.".format(len(friends)), button='OK')

def decline_all_friend_requests():
    friend_requests = api.get('/lol-chat/v1/friend-requests').json()
    if len(friend_requests) == 0:
        pymsgbox.alert(title='IRF Tools', text="You don't have any friend requests.", button='OK')
    else:
        for i in range(len(friend_requests)):
            api.delete('/lol-chat/v1/friend-requests/{}'.format(friend_requests[i]["id"]))
        pymsgbox.alert(title='IRF Tools', text="{} friend requests has been declined.".format(len(friend_requests)), button='OK')

def accept_all_friend_requests():
    friend_requests = api.get('/lol-chat/v1/friend-requests').json()
    if len(friend_requests) == 0:
        pymsgbox.alert(title='IRF Tools', text="You don't have any friend requests.", button='OK')
    else:
        for i in range(len(friend_requests)):
            api.post('/lol-chat/v1/friend-requests', json={
              "direction": friend_requests[i]["direction"],
              "gameName": friend_requests[i]["gameName"],
              "gameTag": friend_requests[i]["gameTag"],
              "icon": friend_requests[i]["icon"],
              "id": friend_requests[i]["id"],
              "name": friend_requests[i]["name"],
              "note": friend_requests[i]["note"],
              "pid": friend_requests[i]["pid"],
              "puuid": friend_requests[i]["puuid"],
              "summonerId": friend_requests[i]["summonerId"]
            })
        pymsgbox.alert(title='IRF Tools', text="{} friend requests has been accepted.".format(len(friend_requests)), button='OK')

def fake_ban_message(name):
    data = api.get('/lol-summoner/v1/summoners?name={}'.format(name)).json()
    send_message = api.post('/lol-chat/v1/conversations/{}/messages'.format(data["puuid"]), json={"body": fake_msg})
    if send_message.status_code != 404:
        pymsgbox.alert(title='IRF Tools', text="Fake Ban Message has been sent to {}".format(name), button='OK')

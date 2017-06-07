from spy_details import friends
from spy_friend import select_friend
from datetime import datetime

def read_old_mess():
    print "Select name of friend whoes chat history you want to view"
    friend_name = select_friend()
    for ele in friends[friend_name]['Chats']:
        print (" | Message:%s | Send by me:%s |"%(ele['message'],ele['sent_by_me']) + ele['time'].strftime("Date: %b-%d-%y   Time: %H:%M:%S"))

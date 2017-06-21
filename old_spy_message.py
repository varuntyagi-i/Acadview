from spy_details import friend_list
from spy_friend import select_friend
from termcolor import colored

def read_old_mess():
    print "Select name of friend whoes chat history you want to view"
    friend_index = select_friend()
    print "\n--Below is the chat history of your's with your friend--"
    if friend_list[friend_index].chat != []:
        for ele in friend_list[friend_index].chat:
            print (" | Message:%s | Send by me:%s |"%(ele.message,ele.sent_by_me)
                            + ele.time.strftime("Date: %b-%d-%y   Time: %H:%M:%S")       )
    else:
        print colored("\"You have no chat history with your Friend\"",'green')


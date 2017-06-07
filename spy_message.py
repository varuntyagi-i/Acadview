from steganography.steganography import Steganography
from datetime import datetime
from spy_friend import select_friend
from spy_details import friends

#Sending secret message to spy's Friend.
def send_message():
    print "Select a friend whom you want to send the message:"
    friend_choice = select_friend()
    original_image = raw_input("\nWhat is the name of the image?(D:/image1.jpg)")
    output_path = 'D:/image2.jpg'
    text = raw_input("What do you want to say?")
    Steganography.encode(original_image, output_path, text)

    new_chat = {
        "message": text,
        "time": datetime.now(),
        "sent_by_me":True
    }

    friends[friend_choice]['Chats'].append(new_chat)

    print "\nYour secret message is ready!"
    mess = friends[friend_choice]['Chats'][-1]['message']
    time = friends[friend_choice]['Chats'][-1]['time']
    print "\nSecret message sent !"
    print ("Friend's name : %s"%(friends[friend_choice]['Name']))
    print ("Secret message : %s" % (mess))
    print time.strftime("Date: %b-%d-%y   Time: %H:%M:%S\n")

#Reading spy's friend's message
def read_message():
    print "Select sender's name:"
    sender = select_friend()
    output_path = raw_input("\nWhat is the name of the file?(D:/image2.jpg)")
    secret_text = Steganography.decode(output_path)

    new_chat = {
        "message": secret_text,
        "time": datetime.now(),
        "sent_by_me":False
    }
    friends[sender]['Chats'].append(new_chat)

    print ("\nSecret message for you : %s" % (friends[sender]['Chats'][-1]['message']))
    time = friends[sender]['Chats'][-1]['time']
    print time.strftime("Date: %b-%d-%y   Time: %H:%M:%S\n")


from steganography.steganography import Steganography
from datetime import datetime
from spy_friend import select_friend
from spy_details import AddFriends, friend_list, NewChats
from termcolor import colored
import csv


#   Sending secret message to spy's Friend.
def send_message():
    print "Select a friend whom you want to send the message:"
    friend_choice = select_friend()
    original_image = raw_input("\nWhat is the path of the image?(D:\Acadview\spy_chat\image.png)")
    output_path = 'D:\Acadview\spy_chat\encrypted_image.png'
    text = raw_input("What do you want to say?")
    Steganography.encode(original_image, output_path, text)

    with open('chat_messages.csv','a') as data:
        writer = csv.writer(data)
        writer.writerow([friend_list[friend_choice].name,text,datetime.now(),True])

    # save = NewChats(text,datetime.now(),True)
    # friend_list[friend_choice].chat.append(save)
    print "\nYour secret message is ready!"
    mess = text
    time = datetime.now()
    print "\nSecret message sent !"
    print ("Friend's name : %s"%(friend_list[friend_choice].name))
    print ("Secret message : %s" % (mess))
    print time.strftime("Date: %b-%d-%y   Time: %H:%M:%S\n")


#   Reading spy's friend's message
def read_message():
    print "Sender's name:"
    sender = select_friend()
    output_path = raw_input("\nWhat is the path of the file?(D:\Acadview\spy_chat\encrypted_image.png)")
    secret_text = Steganography.decode(output_path)
    if secret_text == "":
        print colored("There is no secret message","red")
    else:
        if secret_text == "DSF":
            secret_text = "DO SOMETHING FAST"
            print colored("DO SOMETHING FAST","red")
        elif secret_text == "G7L":
            secret_text = "GOT SEASON 7 LEAKED"
            print  colored("GOT SEASON 7 LEAKED","red")

        with open('chat_messages.csv', 'a') as data:
            writer = csv.writer(data)
            writer.writerow([friend_list[sender].name, secret_text, datetime.now(), False])
        # save = NewChats(secret_text,datetime.now(),False)
        # friend_list[sender].chat.append(save)
        print ("\nSecret message for you : %s" % (secret_text))
        time = datetime.now()
        print time.strftime("Date: %b-%d-%y   Time: %H:%M:%S\n")

#   calculating average
    count = 0
    total = 0
    for ele in friend_list[sender].chat:
        count += 1
        total = len(ele.message.split()) + total
    average = total/count
#   if a spy is speaking too much it will no longer remain spy's friend
    if average >= 100:
        friend_list.pop(sender)
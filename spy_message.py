from steganography.steganography import Steganography
from datetime import datetime
from spy_friend import select_friend
from spy_details import add_friends,friend_list,new_chats
from termcolor import colored

#Sending secret message to spy's Friend.
def send_message():
    print "Select a friend whom you want to send the message:"
    friend_choice = select_friend()
    original_image = raw_input("\nWhat is the path of the image?(D:/image1.jpg)")
    output_path = 'D:/image2.jpg'
    text = raw_input("What do you want to say?")
    Steganography.encode(original_image, output_path, text)

    save = new_chats(text,datetime.now(),True)

    friend_list[friend_choice].chat.append(save)
    print "\nYour secret message is ready!"
    mess = friend_list[friend_choice].chat[-1].message
    time = friend_list[friend_choice].chat[-1].time
    print "\nSecret message sent !"
    print ("Friend's name : %s"%(friend_list[friend_choice].name))
    print ("Secret message : %s" % (mess))
    print time.strftime("Date: %b-%d-%y   Time: %H:%M:%S\n")

#Reading spy's friend's message
def read_message():
    print "Sender's name:"
    sender = select_friend()
    output_path = raw_input("\nWhat is the path of the file?(D:/image2.jpg)")
    secret_text = Steganography.decode(output_path)
    if secret_text == "":
        print colored("There is no secret message","red")
    else:
        if secret_text == "DSF":
            print colored("DO SOMETHING FAST","red")
        elif secret_text == "G7L":
            print  colored("GOT SEASON 7 LEAKED","red")

        save = new_chats(secret_text,datetime.now(),False)
        friend_list[sender].chat.append(save)
        print ("\nSecret message for you : %s" % (friend_list[sender].chat[-1].message))
        time = friend_list[sender].chat[-1].time
        print time.strftime("Date: %b-%d-%y   Time: %H:%M:%S\n")

#calculating average
    count = 0
    sum = 0
    for ele in friend_list[sender].chat:
        count += 1
        sum = len(ele.message.split( )) + sum
    average = sum/count
#if a spy is speaking too much it will no longer remain spy's friend
    if average >= 100:
        friend_list.pop(sender)
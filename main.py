from spy_details import spy_information_class
from spy_status import add_status
from spy_friend import add_friend,select_friend
from spy_message import send_message,read_message
from old_spy_message import read_old_mess
from termcolor import colored


def spy_chat():
#Diplaying spy's information:
    print colored("\nSpy_name:%s \nAge:%d \nRating:%.2f \nonline_status:%s " % (spy.name,spy.age,spy.rating,spy.online_status),'green')
    show_menu = True

    while show_menu == True:
        menu_choice = int(raw_input("\nwhat do you want to do? \n1.Add a status Update \n2.Add friend \n3.View friend's details "
                                    "\n4.Send Secret message."
                                    "\n5.Read Secret message.\n6.Read older chats from any of my spy friends\n7.Close the Application\n"))
        if menu_choice == 1:
            print "Update your Status"
            current_status_message = "None"
            current_status_message = add_status(current_status_message)
            print ("\n--Your current_status_message is--\n")+colored("%s"%(current_status_message),'green')
        elif menu_choice == 2:
            add_friend(spy.rating)
        elif menu_choice == 3:
            print "Select a friend whoes detail you want to view"
            select_friend()
        elif menu_choice == 4:
            send_message()
        elif menu_choice == 5:
            read_message()
        elif menu_choice == 6:
            read_old_mess()
        elif menu_choice == 7:
            show_menu = False
        else:
            print colored("Enter correct Choice",'red')


#Begining of our spy_application
warn = 0
#Enter choice whether you want to continue as a Default user or create new User
while True:
    choice = int(raw_input("Press\n 1. to continue as default user or \n 2. to create new user\n"))
    if choice == 1:
        spy = spy_information_class('Varun Tyagi',26,8.6,True)
        spy_chat()
        break
    elif choice == 2:
        name = raw_input("Welcome to spy chat, you must tell me your spy name first: \t")
        if len(name) == 0:
#keep executing the loop until Spy enters his name
            while True:
                print colored("WARNING: Please enter your name to continue:",'red')
                name = raw_input("Welcome to spy chat, you must tell me your spy name first: \t")
                if len(name) != 0:
                    break
                else:
                    pass

        if len(name) != 0:
            Salutation = raw_input("Should I call you Mr. or Mrs. ? :\t")
            age = int(raw_input("What is your age? : "))

            if 50>age>12:

                print ("%s %s please enter"%(Salutation,name))
                rate = float(raw_input("1.your Spy ratings :\t"))
                online_status = bool(raw_input("2.your online_status(True/False) :\t"))

#Storing Spy Details
                spy = spy_information_class(name,age,rate,online_status)
#Display Spy Details of new User
                spy_chat()
            else:
                print colored("Sorry you are not appropriate to be a spy",'green')
        break
    else:
        if warn == 0:
            print  colored("Invalid Input",'red')
            warn += 1
            pass
        elif warn == 1:
            print colored("\nDon't try to be clever.I am more smarter then you",'yellow'),colored("LAST CHANCE",'red')
            warn += 1
            pass
        else:
            break
from spy_details import info
from spy_status import add_status
from spy_friend import add_friend,select_friend
from spy_message import send_message,read_message
from old_spy_message import read_old_mess
from termcolor import colored

def spy_chat():
#Diplaying spy's information:
    print colored("\nSpy_name:%s \nAge:%d \nRating:%.2f \nonline_status:%s " % (info.name,info.age,info.rating,info.online_status),'green')
    show_menu = True

    while show_menu == True:
        menu_choice = int(raw_input("\nwhat do you want to do? \n1.Add a status Update \n2.Add friend \n3.View friend's details "
                                    "\n4.Send Secret message."
                                    "\n5.Read Secret message.\n6.Read older chats from any of my spy friends\n7.Close the Application\n"))
        if menu_choice == 1:
            if len(info.status_messages)==0:
                current_status_message = "None"
            else:
                current_status_message = info.status_messages[-1]
            current_status_message = add_status(current_status_message)
            print ("\n--Your current_status_message is--\n")+colored("%s"%(current_status_message),'green')

        elif menu_choice == 2:
            add_friend(info.rating)
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
        info.spy_info('Varun Tyagi',26,8.6,True,["gd nyt","gd morning"])
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
            while True:
                Salutation = raw_input("Should I call you Mr. or Mrs. ? :\t")
                if Salutation == "Mr." or Salutation == "Mrs.":
                    break
                else:
                    print colored("please enter correct Salutation to proceed","red")
                    pass

            age = int(raw_input("What is your age? : "))
            if 50>age>12:
                print ("%s %s please enter"%(Salutation,name))
                while True:
                    rate = float(raw_input("1.your Spy ratings(0-10) :\t"))
                    if 0<rate<=10:
                        if rate >= 8.0:
                            print colored("You are a good spy","yellow")
                        elif 5.0<rate<8.0:
                            print  colored("You are an average spy","yellow")
                        else:
                            print colored("You are below average","yellow")
                    break
                else:
                    print "Rating must be from 0.0 to 10.0"
                    pass

                online_status = bool(raw_input("2.your online_status(True/False) :\t"))

#Storing Spy Details
                info.spy_info(name,age,rate,online_status,[])
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
            print colored("\nDon't try to be clever.I am more smarter than you",'yellow'),colored("LAST CHANCE",'red')
            warn += 1
            pass
        else:
            break
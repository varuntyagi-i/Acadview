from spy_details import AddFriends, friend_list
from termcolor import colored
import csv


#   Adding spy's friend to friend's List
def add_friend(rating):
    while True:
        new_friend = AddFriends
        new_friend.name = raw_input("Please add your friend's name: ")
        salutation = raw_input("Mr. or Ms.?: ")
        new_friend.name = salutation + " " + new_friend.name

        new_friend.age = int(raw_input("Age?"))
        new_friend.rating = float(raw_input("Spy rating?"))
        new_friend.online_status = bool(raw_input("Online_Satus(True/False): "))
        if len(new_friend.name) > 0 and new_friend.age > 12 and new_friend.rating >= rating:
            #   Adding friend details to csv file.
            with open("friends.csv",'a') as friends_data:
                writer = csv.writer(friends_data)
                writer.writerow([new_friend.name, new_friend.age, new_friend.rating, new_friend.online_status])

            print "spy\'s friend added"
        else:
            print 'Sorry! Invalid entry. We can\'t add spy as your friend with the details you provided'

        choice = raw_input("Want to add more friends(y/n)?: ")
        if choice.upper()=='N':
            break
        elif choice.upper()=='Y':
            pass
        else:
            print colored("INVALID INPUT",'red')
            break
    print colored("Total number of friends are: %d" %(len(friend_list)),"green")


#   Displaying information of spy's friend
def select_friend():
    count = 0
    if len(friend_list)==0:
        print colored("Friend list is empty,please add some friend in list first",'red')
    else:
        for friend in friend_list:
            count += 1
            print ("%d.%s"%(count,friend.name))

        while True:
            friend_index = int(raw_input()) - 1
            if 0 <= friend_index < count:
                print "**Friend's Detail**"
                print ("Name:%s\nAge:%d\nRating:%.2f\nOnline Status:%r"%( friend_list[friend_index].name,friend_list[friend_index].age,
                                                                        friend_list[friend_index].rating,
                                                                        friend_list[friend_index].online_status))
                break
            else:
                print colored("You have no such friend. Select from the above mentioned friend",'yellow')

        return friend_index

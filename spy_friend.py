from spy_details import friends

#Adding spy's friend to friend's List
def add_friend(rating):
    while True:
        new_friend = {
            'Name':"",
            'Age':0,
            'Rating':0,
            'online_status':True,
            'Chats':[]
         }
        new_friend['Name'] = raw_input("Please add your friend's name: ")
        new_friend['salutation'] = raw_input("Mr. or Ms.?: ")
        new_friend['Name'] = new_friend['salutation'] + " " + new_friend['Name']

        new_friend['Age'] = int(raw_input("Age?"))
        new_friend['Rating'] = float(raw_input("Spy rating?"))
        if len(new_friend['Name']) > 0 and new_friend['Age'] > 12 and new_friend['Rating'] >= rating:
            friends.append(new_friend)
            print "spy\'s friend added"
        else:
            print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'

        choice = raw_input("Want to add more friends(y/n)?: ")
        if choice.upper()=='N':
            break
        elif choice.upper()=='Y':
            pass


#Displaying information of spy's friend
def select_friend():
    count = 0

    for friend in friends:
        count += 1
        print ("%d.%s"%(count,friend['Name']))
    friend_index = int(raw_input())-1
    if friends[friend_index] in friends:
        print ("\nName:%s\nAge:%d\nRating:%.2f\nOnline Status:%s"%( friends[friend_index]['Name'],friends[friend_index]['Age'],
                                                                    friends[friend_index]['Rating'],
                                                                    friends[friend_index]['online_status']))
    return friend_index



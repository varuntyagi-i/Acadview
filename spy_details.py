
class SpyInformationClass:
    def spy_info(self,name,age,rating,online_status,status_messages):
        self.name = name
        self.age = age
        self.rating = rating
        self.online_status = online_status
        self.status_messages = status_messages


info = SpyInformationClass()


class NewChats:
    def __init__(self,name,message,time,sent_by_me):
        self.name = name
        self.message = message;
        self.time = time;
        self.sent_by_me = sent_by_me;


class AddFriends:
    def __init__(self,name,age,rating,online_status):
        self.name = name;
        self.age = age;
        self.rating =rating;
        self.online_status = online_status;
        self.chat=[]


friend_list = []
# friend_list.append(AddFriends('Anubhav',45,9.9,True))
# friend_list.append(AddFriends('Rahul',23,8.3,True))


"""        
friends = [  {'Name':"Anubhav",
                    'Age' : 45,
                    'Rating' : 9.9,
                    'online_status':True,
                    'Chats':[]
              },

            {'Name': "Rahul",
                    'Age': 32,
                    'Rating': 9.8,
                    'online_status': True,
                    'Chats':[]
             }

          ]
"""
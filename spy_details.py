
class spy_information_class:
    def spy_info(self,name,age,rating,online_status,status_messages):
        self.name = name
        self.age = age
        self.rating = rating
        self.online_status = online_status
        self.status_messages = status_messages
info = spy_information_class()
#status_messages = ["gd nyt","gd morning"]


class new_chats:
    def __init__(self,message,time,sent_by_me):
        self.message = message;
        self.time = time;
        self.sent_by_me = sent_by_me;


class add_friends:
    def __init__(self,name,age,rating,online_status):
        self.name = name;
        self.age = age;
        self.rating =rating;
        self.online_status = online_status;
        self.chat=[]


friend2=add_friends("Rahul",23,8.3,True)

friend_list = []
friend_list.append(add_friends("Anubhav",45,9.9,True))
friend_list.append(add_friends("Rahul",23,8.3,True))
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
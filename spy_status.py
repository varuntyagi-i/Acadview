from spy_details import status_messages
from termcolor import colored

#Adding/Updating spy's status:
def add_status(current_status_message):
    if current_status_message == "None":
        default = raw_input("Do you want to select from the older status (y/n) ?: ")
        if default.upper() == 'N':
            while True:
                new_status_message = raw_input("What status message do you want to set ?")
                if len(new_status_message) > 0:
                    update_status_message = new_status_message
                    status_messages.append(update_status_message)
                    break
                else:
                    print colored("No status message received",'red')
                    pass

        elif default.upper() == 'Y':
            print "Previous Status messages are "
            item_position = 0
            for status in status_messages:
                item_position = item_position + 1
                print ("%d.%s"%(item_position,status))

            while True:
                message_selection = int(raw_input("Which status message do you want to set ?"))-1
                if 0 <= message_selection < item_position:
                    update_status_message = status_messages[message_selection]
                    status_messages.append(update_status_message)
                    status_messages.pop(message_selection)
                    break
                else:
                    print colored("Enter the correct choice from the given choices",'red')

        else:
            print colored("INVALID INPUT",'red')
            update_status_message = colored("STATUS NOT UPDATED",'red')

        return update_status_message

    else:
        print ("Your current_status_message is %s"%(current_status_message))


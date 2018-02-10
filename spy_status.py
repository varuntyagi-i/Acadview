from spy_details import info
from termcolor import colored


#   Adding/Updating spy's status:
def add_status(current_status_message):
    if current_status_message != "None":
        print "Your current_status_message is: " + colored("%s" % current_status_message, "green")
        print colored("Update your Status", "yellow")
        default = raw_input("Do you want to select from the older status (y/n) ?: ")
        if default.upper() == 'N':
            while True:
                new_status_message = raw_input("What status message do you want to set ?")
                if len(new_status_message) > 0:
                    update_status_message = new_status_message

                    info.status_messages.append(update_status_message)
                    break
                else:
                    print colored("No status message received",'red')
                    pass

        elif default.upper() == 'Y':
            print "Previous Status messages are "
            item_position = 0
            for status in info.status_messages:
                item_position = item_position + 1
                print colored("%d.%s" % (item_position, status), "green")

            while True:
                message_selection = int(raw_input("Which status message do you want to set ?"))-1
                if 0 <= message_selection < item_position:
                    update_status_message = info.status_messages[message_selection]
                    print colored("Status updated successfully", "yellow")

                    info.status_messages.append(update_status_message)
                    info.status_messages.pop(message_selection)
                    break
                else:
                    print colored("Enter the correct choice from the given choices", 'red')

        else:
            print colored("INVALID INPUT", 'red')
            update_status_message = colored("STATUS NOT UPDATED", 'red')

        return update_status_message

    else:
        print "You have no previous status message"
        while True:
            new_status_message = raw_input("What status message do you want to set ?")
            if len(new_status_message) > 0:
                update_status_message = new_status_message
                print colored("Status updated successfully", "yellow")
                info.status_messages.append(update_status_message)
                break
            else:
                print colored("No status message received", 'red')
                pass
        return update_status_message

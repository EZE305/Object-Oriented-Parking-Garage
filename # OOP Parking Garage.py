# OOP Parking Garage

# Your parking garage class should have the following methods:

# - takeTicket
# - This should decrease the amount of tickets available by 1
# - This should decrease the amount of parkingSpaces available by 1

# - payForParking
# - Display an input that waits for an amount from the user and store it in a variable
# - If the payment variable is not empty then (meaning the ticket has been paid) 
# -> display a message to the user that their ticket has been paid and they have 15mins to leave
# - This should update the "currentTicket" dictionary key "paid" to True

# # -leaveGarage
# # - If the ticket has been paid, display a message of "Thank You, have a nice day"
# # - If the ticket has not been paid, display an input prompt for payment
# # - Once paid, display message "Thank you, have a nice day!"
# # - Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
# # - Update tickets list to increase by 1 (meaning add to the tickets list)

# # You will need a few attributes as well:
# not saying if these are class or instance attributes
# # - tickets -> list
# # - parkingSpaces -> list
# # - currentTicket -> dictionary



print("Welcome to a Parking Garage. ")

# global variable tickets, and spaces left
class ParkingGarage:

# these are variables that we are putting into multiple methods
    def __init__(self, current_ticket):
        self.current_ticket = current_ticket

    def takeTicket(self):
        tickets_gone.append(tickets_left.pop())
        spaces_gone.append(spaces_left.pop())
        last_ticket_taken = tickets_left[-1]
        last_space_taken = spaces_left[-1]
        return print("There are " + str(last_ticket_taken) + " " + "tickets left, and " + str(last_space_taken) + " spaces left." )


    def payForParkingTicket(self):
        print("Please pay 5 dollars. Flat rate, no change muahaha")
        # prob_solved = False

        while self.current_ticket:
            money = input ("Type 'Pay' to shell out some coins for parking. Type 'Broke' if you have no money. ")
            if money == "Pay":
                self.current_ticket["Paid"] = True
                print ("Thanks for Paying, Have a Nice day!... you can leave now...")
                run()
            elif money == "Broke":
                print("I guess you're moving into the parking Garage huh?")
            else:
                print("I dont Understand")


    def leaveGarage(self):
        if self.current_ticket == {"Paid":False}:
            return print("Need to pay before you leave")
        elif self.current_ticket == {"Paid":True}:
            tickets_left.append(tickets_gone.pop())
            spaces_left.append(spaces_gone.pop())
            return print("Thank you, have a nice day!")      
        else:
            return print("no comprendo")
      

def run():

    while True:
        response = input ("Would you like to Park/Pay/Leave ")
            
        if response.lower() == "park":
            letsPark.takeTicket()
            print("Thanks for parking!")
                
        elif response.lower() == "pay":
            letsPark.payForParkingTicket()
                    
        elif response.lower() == "leave":
            letsPark.leaveGarage()
                
        else:
            print("Please try other input ")

# current_ticket = {}
tickets_gone = []
spaces_gone = []
tickets_left = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
spaces_left = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# key value pair will be paid true paid false 
letsPark = ParkingGarage({"Paid":False})

# print(ParkingGarage.__dict__)


run()










































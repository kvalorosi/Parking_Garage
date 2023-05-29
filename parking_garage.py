class parking_Garage():
    parking_spaces = 20
    tickets = 20
    price = 15
    strikes = 0
    

    def __init__ (self,currentTicket={"paid":False,"ticket":False,"amount_paid":0},exit=False):
        self.currentTicket = currentTicket
        self.exit = exit

    
    def take_ticket(self):
        if self.currentTicket["ticket"] == False:
            print(">Here's your ticket.")
            self.parking_spaces -= 1
            self.tickets -= 1
            self.currentTicket["ticket"] = True
        else:
            print("You already have ticket.")
    

    def pay_Parking(self):
        if self.currentTicket["ticket"] == True: 
            print("The price of a ticket is $15.")
            while True:
                amount=input("Enter amount to pay: ")
                if amount == 'q':
                    print("Come back later to pay for ticket.")
                    break
                elif amount != 'q':
                    try:
                        amount = int(amount)
                        self.currentTicket["amount_paid"] += amount 
                        if self.currentTicket["amount_paid"] >= self.price:
                            self.currentTicket["paid"] = True
                            print("Thank you for paying, you have 15 minutes to leave the garage.")
                            break
                        else: 
                            if self.strikes < 2:
                                print("ALERT: You have partially paid your ticket. Please pay the remaining amount before you leave.\n") 
                            else:
                                print("This is not a free-for-all. Pay the remainder of your ticket.")  
                    except:
                        print("ERROR: Please enter valid input.\n")
        else:
            print("Go back and take a ticket first.")        
            

    def leave(self):
        if self.currentTicket["paid"] == True:
            print("Thank you for visiting our garage, Have a splendid day!")
            self.parking_spaces += 1
            self.tickets += 1
            self.exit = True
        elif self.currentTicket["ticket"] == False:
            print("Don't come in here, if you're not gonna take a ticket! Be gone!")
            self.exit = True
        else:
            if self.strikes == 3:
                print("Alright buddy, this is your last warning")
            print("You haven't paid your ticket. Once you've paid, you can leave")
            if self.strikes == 2:
                print("Pay for your damn ticket!")
            elif self.strikes >= 4:
                print("Leave the garage immediately! We're calling the police.")
            self.strikes += 1
            print("")
            self.pay_Parking()

    def run():
        print("\nWelcome to our parking garage! Please select from the following menu to continue: \n")
        MyGarage = parking_Garage()
        while True:
            menu = input("Press 'T' for a ticket,'P' to pay, 'L' to leave the garage, and 'Q' to Quit out the Game:\n")
            if menu.upper() == 'T':
                MyGarage.take_ticket()
                print("")
            elif menu.upper() == 'P':
                MyGarage.pay_Parking()
                print("")
            elif menu.upper() == 'L':
                MyGarage.leave()
                print("")
                if MyGarage.currentTicket["paid"] != False or MyGarage.currentTicket["ticket"] == False:
                    break
            elif menu.upper() == 'Q':
                print("Thanks for visiting!")
                break
            else:
                print("ERROR: Please select a menu item", end="\n\n")





# MyGarage = parking_Garage()
# MyGarage.pay_Parking()
# MyGarage.take_ticket()
# MyGarage.leave()
# MyGarage.pay_Parking()
# MyGarage.leave()

# MyGarage.take_ticket()
# MyGarage.pay_Parking()

parking_Garage.run()





        


            

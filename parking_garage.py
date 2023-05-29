class parking_Garage():
    parking_spaces = 20
    tickets = 20
    price = 15
    

    def __init__ (self,currentTicket={"paid":False,"ticket":False,"amount_paid":0},exit=False):
        self.currentTicket = currentTicket
        self.exit = exit

    
    def take_ticket(self):
        if self.currentTicket["ticket"] == False:
            print("Here's your ticket.")
            self.parking_spaces -= 1
            self.tickets -= 1
            self.currentTicket["ticket"] = True
        else:
            print("You already have ticket.")
    

    def pay_Parking(self):
        if self.currentTicket["ticket"] == True: 
            print("The price of a ticket is $15.")
            # while self.currentTicket["amount_paid"] < self.price:
            amount=input("Enter amount to pay.")
            if amount == 'q':
                print("Come back to pay for ticket.")
                
            else:
                try:
                    amount = int(amount)
                    self.currentTicket["amount_paid"] += amount 
                    if self.currentTicket["amount_paid"] >= self.price:
                        self.currentTicket["paid"] = True
                        print("Thank you for paying, you have 15 minutes to leave the garage.")
                    else: 
                        print("You have partially paid your ticket")   
                except:
                    print("Please enter valid input.")
            
            
        else:
            print("Go back and take a ticket first.")

    def leave(self):
        if self.currentTicket["paid"] == True:
            print("Thank you for visiting our garage, Have a splendid day!")
            self.parking_spaces += 1
            self.tickets += 1
            self.exit = True
        else:
            print("You haven't paid your ticket")
            self.pay_Parking()

    

MyGarage = parking_Garage()
MyGarage.pay_Parking()
MyGarage.take_ticket()
MyGarage.leave()
MyGarage.pay_Parking()
MyGarage.leave()






        


            

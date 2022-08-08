class ATM:

    def __init__(self,cardno,pin):
        self.cardno=cardno
        self.pin=pin

    def cashWithdrawl(self,amount):
        new_amount = 50000 - amount
        print("You have withdrawn amount "+str(amount) +". Your remaining balance is "+ str(new_amount))
        
    def checkBalance(self):
        print(50000)


def main():
    cardno=input('Insert Card Number:-')
    pin=input('Insert Pin Number:-')
    user=ATM(cardno,pin)
    print('Choose An Option:-')
    print("1.Balance Enquriy   2.Withdrawl")
    activity = int(input("enter activity number :- "))
    if(activity==1):
        user.checkBalance()
    elif(activity==2):
        amount=int(input('Enter the Amount:-'))
        user.cashWithdrawl(amount)
    else:    
        print('Enter the Valid Number')
if __name__ == "__main__":
    main()


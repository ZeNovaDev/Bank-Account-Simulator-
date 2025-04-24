class Bank():
  people={}
  
  def __init__(self, name) :
    self.name=name

  
  def Deposit(self):
    user_value=float(input("How much you want to deposit? "))
    if user_value<=0:
      print("Despoit amount cannot be less than or equal to zero. ")

    else:
      current_balance=Bank.people.get(self.name,0)
      Bank.people[self.name]= current_balance+user_value 
      print(Bank.people)

  def withdraw(self):
    current_balance =Bank.people.get(self.name,0)
    user_value=float(input("Enter amount to be withdrawn: "))
    if user_value<=0:
      print("Withdraw amount cannot be less than or equal to zero. ")

    elif user_value>current_balance:
      print("Insufficient balance*")

    else: 
      Bank.people[self.name]=current_balance-user_value
      print(f"{user_value} has been withdrawn")
      print(f"Your current balance is {Bank.people.get(self.name,0)} ")

  def check_balance(self):
    print(f" Your current balance is {Bank.people.get(self.name,0)}")
  def transfer(self):
    current_balance=Bank.people.get(self.name, 0)
    transfer_person=str(input("Enter valid name to transfer your money: ")) 
    if transfer_person not in Bank.people:
      choice=input("Do you want to create account to transfer?(Y/N): ").upper()
      if choice=="Y":
        Transfer_Amount=int(input("Enter amount to transfer")) 
        if Transfer_Amount<current_balance:
          Bank.people[transfer_person]=Transfer_Amount
          Bank.people[self.name]=current_balance-Transfer_Amount

        else:
          print("Insufficient Balance*")
        
      

print("Welcome to MC Bank")
print("""**'D' for deposit 
**'W' for withdraw 
**'C' for checking balance
**'T' for transferring balance! 
""")

def get_choice():
  Yes_No=True
  while Yes_No:
    choice=str(input("Do you want to continue? (Y/N) : "))
    if choice.upper()=="Y":
      Yes_No=False
      return True

    elif choice.upper()=="N":
      Yes_No=False
      print("Thank you for coming! ")
      return False

    else:
      print("Please enter valid choice!")
    
  
  
choice=True
while choice:
  name=str(input("Enter name: "))
  if name not in Bank.people:
    print("Account has not been created yet! ")
    acc_choice=str(input("Do you want to create one? (Y/N) : ")).upper()
    if acc_choice=="Y":
      Bank.people[name]=0
      
  elif name!="":
    user_choice=str(input("What you want to do, (D/W/C/T)? ")).upper()
  
    if user_choice=="D":
      Person=Bank(name)
      Person.Deposit()
      choice=get_choice()

    elif user_choice=="W":
      Person=Bank(name)
      Person.withdraw()
      choice=get_choice()

    elif user_choice=="C":
      Person = Bank(name)
      Person.check_balance()
      choice=get_choice()

    elif user_choice=="T":
      Person=Bank(name)
      Person.transfer()
      choice=get_choice()
      
    else:
      print("Enter valid choice! ")
      choice=get_choice()

  else:
    print("Name cannot be empty! ")
  
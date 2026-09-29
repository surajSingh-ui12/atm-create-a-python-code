import getpass
# Predefined users, PINs, and balances
users = ['user1', 'user2', 'user3']
pins = ['1234', '2222', '3333']
balances = [1000, 2000, 3000]
print("Welcome to the ATM System!")
while True:
   username = input("Enter Username: ").lower()
   if username in users:
       user_index = users.index(username)
       break
   else:
       print("Invalid Username. Try again.")
# PIN validation
attempts = 0
while attempts < 3:
   pin = getpass.getpass("Enter PIN: ")
   if pin == pins[user_index]:
       print("Login Successful!")
       break
   else:
       attempts += 1
       print(f"Invalid PIN. {3 - attempts} attempt(s) left.")
else:
   print("Too many failed attempts. Exiting.")
   exit()
# Main menu
while True:
   print("\nOptions: (S)tatement | (W)ithdraw | (D)eposit | (P)IN Change | (Q)uit")
   choice = input("Choose an option: ").lower()
   if choice == 's':
       print(f"Your current balance is: €{balances[user_index]}")
   elif choice == 'w':
       amount = int(input("Enter amount to withdraw: "))
       if amount % 10 != 0:
           print("Amount must be in multiples of €10.")
       elif amount > balances[user_index]:
           print("Insufficient balance.")
       else:
           balances[user_index] -= amount
           print(f"Withdrawal successful. New balance: €{balances[user_index]}")
   elif choice == 'd':
       amount = int(input("Enter amount to deposit: "))
       if amount % 10 != 0:
           print("Amount must be in multiples of €10.")
       else:
           balances[user_index] += amount
           print(f"Deposit successful. New balance: €{balances[user_index]}")
   elif choice == 'p':
       new_pin = getpass.getpass("Enter new PIN: ")
       if len(new_pin) == 4 and new_pin.isdigit() and new_pin != pins[user_index]:
           confirm_pin = getpass.getpass("Confirm new PIN: ")
           if confirm_pin == new_pin:
               pins[user_index] = new_pin
               print("PIN changed successfully.")
           else:
               print("PIN mismatch. Try again.")
       else:
           print("Invalid PIN format or same as old PIN.")
   elif choice == 'q':
       print("Thank you for using the ATM. Goodbye!")
       break
   else:
       print("Invalid option. Please try again.")
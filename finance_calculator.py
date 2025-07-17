# 1.prompt whether to proceed with an investment or a loan(bond)

print("how may we assist")
print("1.INVESTMENT")
print("2. BOND")

# attain user input
option = input("Enter 1 or 2: ")

# Check the choice and explain action to be carried by each choice
if option == '1':
    print("\nYou chose option 1: INVESTEMNT.")
    investment_amount = float(input("enter amount to be invested: R "))
    interest_rate = float(input("enter interest rate: "))/100
    investement_period = int(input("enter the investment period(in year): "))
print("\nplease choose an option below")
print("A. S.I-simple interest")
print("B. C.I-compound interest")


#attain 2nd phase user iput
choice = input("Enter A or B: ")
if choice == "A":
    print("\nYou chose choice A: S.I-simple interest") 
    # Calculate simple interest
interest_amount= investment_amount * interest_rate * investement_period

# Calculate total amount after interest
total_amount = investment_amount + interest_amount
    
elif: print("\nYou chose choice B: C.I compound interest")

"""# Calculate compound interest
interest_amount= investment_amount * interest_rate * investement_period

# Calculate total amount after interest
total_amount = investment_amount + interest_amount

# Display the results
print(f"\nSimple Interest: R{interest_amount:.2f}")
print(f"Total Amount: R{total_amount:.2f}")"""

"""if option == '2':
    print("\nYou chose option 2: BOND.")

    investment_amount = float(input("enter amount to be invested: R "))
    interest_rate = float(input("enter interest rate: "))/100
    investement_period = int(input("enter the investment period(in year): "))
print("\nplease choose an option below")
print("A. S.I-simple interest")
print("B. C.I-compound interest")


#attain 2nd phase user iput
choice = input("Enter A or B: ")
if choice == "A":
    print("\nYou chose choice A: S.I-simple interest")"""



    
    

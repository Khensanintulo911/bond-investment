# 1.prompt whether to proceed with an investment or a loan(bond)

def get_valid_input(prompt, valid_options):
    """Get validated user input from allowed options"""
    while True:
        user_input = input(prompt).upper()
        if user_input in valid_options:
            return user_input
        print(f"Invalid input. Please enter one of: {', '.join(valid_options)}")

print("how may we assist")
print("1.INVESTMENT")
print("2. BOND")

# attain user input
option = get_valid_input("Enter 1 or 2: ", ['1', '2'])

# Check the choice and explain action to be carried by each choice
if option == '1':
    print("\nYou chose option 1: INVESTEMNT.")
    investment_amount = float(input("enter amount to be invested: R "))
    interest_rate = float(input("enter interest rate: "))/100
    investement_period = int(input("enter the investment period(in year): "))
    print("\nplease choose an option below")
    print("A. S.I-simple interest")
    print("B. C.I-compound interest")

    #attain 2nd phase user input
    choice = get_valid_input("Enter A or B: ", ['A', 'B'])
    if choice == "A":
        print("\nYou chose choice A: S.I-simple interest") 
        # Calculate simple interest
        interest_amount = investment_amount * interest_rate * investement_period
        # Calculate total amount after interest
        total_amount = investment_amount + interest_amount
        # Display the results
        print(f"\nSimple Interest: R{interest_amount:.2f}")
        print(f"Total Amount: R{total_amount:.2f}")
    else:
        print("\nYou chose choice B: C.I compound interest")
        # Calculate compound interest
        total_amount = investment_amount * (1 + interest_rate) ** investement_period
        interest_amount = total_amount - investment_amount
        # Display the results
        print(f"\nCompound Interest: R{interest_amount:.2f}")
        print(f"Total Amount: R{total_amount:.2f}")

elif option == '2':
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
        print("\nYou chose choice A: S.I-simple interest")
        # Calculate simple interest
        interest_amount= investment_amount * interest_rate * investement_period

        # Calculate total amount after interest
        total_amount = investment_amount + interest_amount

        # Display the results
        print(f"\nSimple Interest: R{interest_amount:.2f}")
        print(f"Total Amount: R{total_amount:.2f}")
    else: 
        print("\nYou chose choice B: C.I compound interest")
        # Calculate compound interest
        total_amount = investment_amount * (1 + interest_rate) ** investement_period
        interest_amount = total_amount - investment_amount

        # Display the results
        print(f"\nCompound Interest: R{interest_amount:.2f}")
        print(f"Total Amount: R{total_amount:.2f}")






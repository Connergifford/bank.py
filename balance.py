name = input("what is your name?")
starting_balance = 5000.25
print(f"welcome {name} Your starting balance is {starting_balance}")

pay_check = int(input("how much of your paycheck would you like to deposit? "))

expenditure_item = input("looks like you went shopping. what did you buy? ")
expenditure = int(input(f"how much does a banjo cost? "))

def checking_balance(user_name, balance, deposits, expense_item, expense_amount):
    ending_balance = (balance + deposits - expense_amount)
    print(f"good day, {user_name}. after spending money on {expense_item} in the amount of {expense_amount} your current checking balance is {ending_balance}")


checking_balance(name, starting_balance, pay_check, expenditure_item, expenditure)


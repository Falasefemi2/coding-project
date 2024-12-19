
MAX_lINES = 3
MAX_BET = 100
MIN_BET = 1
def deposit():
    """_summary_

    Returns:
        _type_: _description_
    """
    while True:
        amount = input("What would you like to deposit?:$")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number")
    return amount

def get_number_of_lines():
    """_summary_

    Returns:
        _type_: _description_
    """
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_lINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_lINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number")
    return lines

def get_bet():
    """_summary_

    Returns:
        _type_: _description_
    """
    while True:
        amount = input("What would you like to bet on each line?:$")
        if amount.isdigit():
            amount = int(amount)
            if MAX_lINES <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Please enter a number")
    return amount
    
    

def main():
    balance = deposit()
    lines = get_number_of_lines()
    bet = get_bet()
    total_bet = bet * lines
    
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")
    
    

main()




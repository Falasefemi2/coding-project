import random

# cONSTANT FOR THE SLOT MACHINES
MAX_LINES = 3 # The max number of rows(lines) a player can bet on
MAX_BET = 100 # Define the range of valid bet amount per line
MIN_BET = 1 # Define the range of valid bet amount per line

ROWS = 3 # Define the number of rows in the slot machine deploy (3*3 grid)
COLS = 3 # Define the number of columns in the slot machine deploy (3*3 grid) 


symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
} # Specifies how may times each symbols(A,B,C,D) can appear in the slot machine

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
} # Determine the payout multiplier for each symbol for example symbol A gives 5 times the bet if it aligns on a winning line.

# Purpose: To check which lines of the slot machine won and calculate the total winnings
# How it works:
# Loops through the selected number of lines(lines)
# Check if all symbols on a line are the same
# If all symbols match the winnings are calculated as symbol value * bet returns the total_winnings and the lines won
def check_winnings(columns, lines, bet, values):
    """To check which lines of the slot machine won and calculate the total winnings.

    Args:
        columns (int): number of col
        lines (int): _number of row
        bet (int): bet from the user
        values (_type_): _description_

    Returns:
        int: _description_
    """
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(lines + 1)
    return winnings, winning_lines

# Purpose: Generate the random slot machines configuration (the symbols in each column)
# How it works
# Starts with a list of all symbols (all_symbols) based on their counts. For each column, randomly selects symbols for its rows, ensuring no symbol is used more times than allowed
# Returns a list of columns, where each column is a list of symbol
def get_slot_machine(rows, cols, symbols):
    """Generate a random slot machine configuration.
    
    Creates a slot machine display by randomly distributing symbols across columns
    while maintaining the specified count for each symbol type.
    
    Args:
        rows (int): Number of rows in the slot machine display
        cols (int): Number of columns in the slot machine display
        symbols (dict): Dictionary mapping symbols to their total count in the machine
        
    Returns:
        list: A list of columns, where each column is a list of randomly selected symbols
    """
    all_symbols = []
    for symbol, symbol_counts in symbols.items():
        for _ in range(symbol_counts):
            all_symbols.append(symbol)
    
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        
        columns.append(column)
    return columns

# Purpose: Display the slot machine in a virtually under stateable way
# How it works
# Iterates through each row of columns
# Print each symbol, separating them with | to format them as a grid.
def print_slot_machines(columns):
    """Display the slot machine configuration in a grid format.
    
    Prints the slot machine symbols in a formatted grid with column separators.
    
    Args:
        columns (list): List of columns containing symbols to display
    """
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()
        
# Purpose: Prompts the user to enter an initial deposit amount.
# How It Works:
# Ensures the input is a valid positive number.
# Keeps asking until the user provides a valid deposit amount.
def deposit():
    """Get the initial deposit amount from the user.
    
    Repeatedly prompts the user until they enter a valid positive number
    for their initial deposit.
    
    Returns:
        int: The deposit amount entered by the user
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
            print("Please enter a number.")
    return amount

# Purpose: Asks the user how many lines they want to bet on.
# How It Works:
# Ensures the input is a number between 1 and MAX_LINES.
# Keeps asking until the user provides a valid input.
def get_number_of_lines():
    """Get the number of lines the user wants to bet on.
    
    Repeatedly prompts the user until they enter a valid number of lines
    between 1 and MAX_LINES.
    
    Returns:
        int: Number of lines to bet on
    """
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number")
    return lines
        
# Purpose: Asks the user how much they want to bet per line.
# How It Works:
# Ensures the input is a valid number within the range of MIN_BET and MAX_BET.
# Keeps asking until the user provides a valid bet amount.
def get_bet():
    """Get the bet amount per line from the user.
    
    Repeatedly prompts the user until they enter a valid bet amount
    between MIN_BET and MAX_BET.
    
    Returns:
        int: Bet amount per line
    """
    while True:
        amount = input("What would you like to bet on each line>:$")
        if amount.isdigit():
            amount = int(amount)
            if MAX_LINES <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Please enter a number")
    return amount

# Purpose: Handles a single round of the slot machine game.
# How It Works:
# Gets the number of lines and the bet amount.
# Validates that the total bet (lines * bet) does not exceed the player’s balance.
# Generates and displays the slot machine using get_slot_machine and print_slot_machines.
# Checks winnings using check_winnings.
# Returns the net result (winnings - total_bet) to adjust the balance.
def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You do not have enough have that amount, your current balance is: ${balance}")
        else:
            break
    
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")
    
    slots = get_slot_machine(ROWS, COLS, symbol_count)
    print_slot_machines(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print("You won on lines:", *winning_lines)
    return winnings - total_bet

# Purpose: The main game loop that runs the slot machine.
# How It Works:
# Starts by asking the player for an initial deposit.
# Continuously lets the player play a round by calling spin.
# Allows the player to quit the game by entering q.
# Prints the remaining balance when the game ends.
def main():
    """Main game loop for the slot machine.
    
    Handles the game flow including:
    - Getting initial deposit
    - Getting number of lines to bet on
    - Getting bet amount per line
    - Validating total bet against balance
    - Generating and displaying slot machine results
    """
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        ans = input("Press enter to play (q to quit)")
        if ans == "q":
            break
        balance = spin(balance)    
    print(f"You left with ${balance}")
main()
import random
MAX_LINES = 3
MAX_BET = 10
MIN_BET = 1 

ROWS = 3
COLS = 3
symbol_count = {
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8
}
symbol_value = {
    "A" : 5,
    "B" : 4,
    "C" : 3,
    "D" : 2
}

def check_winnings(columns,lines,bet,values):
    winnings = 0
    winnings_lines = []
    for line in range(lines):
        symbols = columns[0][line]
        for column in columns:
            symbols_to_check =column[line]
            if symbols != symbols_to_check:
                break
        else:
            winnings += values[symbols]*bet
            winnings_lines.append(line+1)
    return winnings,winnings_lines




def get_slot_machine_spin(rows,cols,symbols):
    all_symbols =[]
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
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

def print_cols(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row],end=" | ")
            else:
                print(column[row])



def deposit():
    while True:
        amount = input("wHAT WOULD YOU LIKE TO DEPOSIT $: ")
        if amount.isdigit():
            amount=int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be grater than zero ")
        else:
            print("Enter a vaild digit")
    return amount

def get_number_of_lines():
    while True:
        line = input(f"Enter the number of lines to bet on (1 - {MAX_LINES})  $: ")
        if line.isdigit():
            line=int(line)
            if 1 <= line <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("Enter a vaild digit")
    return line

def get_bet():
    while True:
        amount = input("What would you like to bet on each line $: ")
        if amount.isdigit():
            amount=int(amount)
            if MIN_BET <= amount <= MAX_BET :
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET} ")
        else:
            print("Enter a vaild digit")
    return amount

def spin(balance):
    while True:
        line = get_number_of_lines()
        bet = get_bet()
        total_bet = int(bet*line)
        while total_bet > balance:
            diff = total_bet - balance
            print(f"Your total bet amount exceeds the balace by {diff} - please enter lower bet")
            bet = get_bet()
            total_bet = bet*line
        print(f"\n\nYou are betting ${bet} on {line}lines.Total bet is ${total_bet}\n\n ")

        slots=get_slot_machine_spin(ROWS,COLS,symbol_count)
        print_cols(slots)
        winnings,winnings_line = check_winnings(slots,line,bet,symbol_value)
        print(f"You won ${winnings}.")
        print(f"You won on lines : ",*winnings_line)
        return winnings - total_bet

def main():
    balance =int(deposit())
    while True:
        print(f"current balance is ${balance}")
        spins = input("Press enter to spin (q to quit)")
        if spins == "q":
            break
        balance += spin(balance)
    print(f"You left wiht ${balance}")



main()

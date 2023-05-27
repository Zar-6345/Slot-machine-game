import random

MAX_LINES = 3
MAX_BET = 500
MIN_BET = 10

ROWS = 3
COLS = 3

symbol_count = {
    "@": 1,
    "#": 2,
    "%": 3
}

symbol_value = {
    "@": 3,
    "#": 5,
    "%": 2
}

def check_winnings(columns, lines, bet, values):
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
            winning_lines.append(line+1)

    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        # for i in range(symbol_count):
        all_symbols.append(symbol)

    columns = []
    for i in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for row in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for a, column in enumerate(columns):
            if a != len(columns) - 1:
                print(column[row], end="|")
            else:
                print(column[row], end="")

        print()

def deposit():
    while True:
        amount = input("Enter how much you are depositing:")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("please enter a number greater than zero:")
        else:
            print("please enter a integer number")
    return amount


def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines you want to bet on (1-" + str(MAX_LINES) + ")")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("please enter a valid number of lines")
        else:
            print("please enter a number")
    return lines


def get_bet():
    while True:
        bet = input(f"Enter the amount you want to bet {MIN_BET} - {MAX_BET} ")
        if not bet.isdigit():
            print("please enter a number")
        else:
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print("please enter a valid amount of bet")
    return bet

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"Your total bet {total_bet:d} is greater than current balance of {balance}")
        else:
            break

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won {winnings} ")
    print(f"you won lines:", *winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"current balance is {balance}")
        answer = input("press enter to play (q to quit)")
        if answer == "q":
            break
        balance += spin(balance)
        if balance == 0:
            break
    print(f"you're left with {balance}")

main()

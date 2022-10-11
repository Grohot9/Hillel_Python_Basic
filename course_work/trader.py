from utils import *

if __name__ == "__main__":
    launch_setup()
    command = assignment_command_argument()

    if command == "RATE":
        print(get_rate())

    elif command == "AVAILABLE":
        print(get_account_balance())

    elif command.split()[0] == "BUY":
        if command.split()[1] == "ALL":
            buy_max_usd()
        else:
            buy_usd(float(command.split()[1]))

    elif command.split()[0] == "SELL":
        if command.split()[1] == "ALL":
            sell_max_usd()
        else:
            sell_usd(float(command.split()[1]))

    elif command == "NEXT":
        change_course()

    elif command == "RESTART":
        set_default_data()

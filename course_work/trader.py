from utils import *

if __name__ == "__main__":
    exchanger = Trader()
    exchanger.launch_setup()
    command = assignment_command_argument()

    if command == "RATE":
        print(exchanger.get_rate())

    elif command == "AVAILABLE":
        print(exchanger.get_account_balance())

    elif command.split()[0] == "BUY":
        if command.split()[1] == "ALL":
            exchanger.buy_max_usd()
        else:
            exchanger.buy_usd(float(command.split()[1]))

    elif command.split()[0] == "SELL":
        if command.split()[1] == "ALL":
            exchanger.sell_max_usd()
        else:
            exchanger.sell_usd(float(command.split()[1]))

    elif command == "NEXT":
        exchanger.change_course()

    elif command == "RESTART":
        set_default_data()

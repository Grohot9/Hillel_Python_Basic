from argparse import ArgumentParser
import json
import random


def parse_argument() -> dict:
    args = ArgumentParser()
    args.add_argument("command", type=str, nargs='*')
    args = vars(args.parse_args())
    args = {"command": " ".join(args["command"])}
    return args


def assignment_command_argument() -> str:
    command = parse_argument()["command"]
    return command


def get_config_data() -> dict:
    try:
        with open("config.json", "r") as json_file:
            config_data = json.loads(json_file.read())
            return config_data
    except FileNotFoundError:
        pass


def create_config_data() -> dict:
    default_data = {"course": 26.00, "UAH": 10000.00, "USD": 0.00, "delta": 0.5}
    config_data = get_config_data()

    if config_data == default_data or config_data is None:
        return default_data
    else:
        return config_data


def create_config() -> None:
    data = create_config_data()
    with open("config.json", "w") as json_file:
        json.dump(data, json_file)


def create_global_info() -> None:
    config_data = get_config_data()
    with open("global_info.json", "w") as json_file:
        json.dump(config_data, json_file)


def create_config_and_global_info() -> None:
    create_config()
    create_global_info()


def get_current_data(filename: str = "global_info.json") -> dict:
    with open(filename, "r") as json_file:
        current_data = json.loads(json_file.read())
        return current_data


def set_default_data() -> None:
    create_global_info()


class Trader:
    def __init__(self):
        self.course = get_current_data()["course"]
        self.total_uah = get_current_data()["UAH"]
        self.total_usd = get_current_data()["USD"]
        self.delta = get_current_data()["delta"]

    def launch_setup(self):
        try:
            if get_current_data() is None:
                create_config_and_global_info()
            else:
                try:
                    if type(self.course) is not float:
                        create_config_and_global_info()
                    elif type(self.total_uah) is not float:
                        create_config_and_global_info()
                    elif type(self.total_usd) is not float:
                        create_config_and_global_info()
                    elif type(self.delta) is not float:
                        create_config_and_global_info()
                except KeyError or json.decoder.JSONDecodeError:
                    create_config_and_global_info()
        except (json.decoder.JSONDecodeError, FileNotFoundError):
            create_config_and_global_info()

    def change_global_info(self, filename: str = "global_info.json"):
        global_changes = {"course": self.course, "UAH": self.total_uah, "USD": self.total_usd, "delta": self.delta}
        with open(filename, "w") as json_file:
            json.dump(global_changes, json_file)

    def get_rate(self):
        current_course = self.course
        return current_course

    def get_account_balance(self) -> str:
        return f"USD {self.total_usd} UAH {self.total_uah}"

    def buy_usd(self, usd_amount_to_buy: float):

        if self.total_uah / self.course >= usd_amount_to_buy:
            self.total_usd += usd_amount_to_buy
            self.total_uah -= usd_amount_to_buy * self.course
            self.total_usd = round(self.total_usd, 2)
            self.total_uah = round(self.total_uah, 2)
            self.change_global_info()
        else:
            print(f"UNAVAILABLE, REQUIRED BALANCE UAH {round(usd_amount_to_buy * self.course, 2)},"
                  f" AVAILABLE {self.total_uah}")

    def sell_usd(self, usd_amount_to_sell: float):
        if self.total_usd >= usd_amount_to_sell:
            self.total_usd -= usd_amount_to_sell
            self.total_uah += usd_amount_to_sell * self.course
            self.total_usd = round(self.total_usd, 2)
            self.total_uah = round(self.total_uah, 2)
            self.change_global_info()
        else:
            print(f"UNAVAILABLE, REQUIRED BALANCE USD {usd_amount_to_sell}, AVAILABLE {self.total_usd}")

    def buy_max_usd(self):
        self.total_usd += self.total_uah / self.course
        self.total_usd = round(self.total_usd, 2)
        self.total_uah = round(self.total_uah / self.course % 1, 2)
        self.change_global_info()

    def sell_max_usd(self):
        self.total_uah += self.total_usd * self.course
        self.total_uah = round(self.total_uah, 2)
        self.total_usd = round(self.total_usd * 2 % 1, 2)
        self.change_global_info()

    def change_course(self):
        self.course = round(random.uniform(self.course - self.delta, self.course + self.delta), 2)
        self.change_global_info()

from argparse import ArgumentParser
import json
import random

if __name__ == '__main__':
    import json.decoder


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


def launch_setup() -> None:
    try:
        current_data = get_current_data()
        if current_data is None:
            create_config_and_global_info()
        else:
            try:
                if type(current_data["course"]) is not float:
                    create_config_and_global_info()
                elif type(current_data["UAH"]) is not float:
                    create_config_and_global_info()
                elif type(current_data["USD"]) is not float:
                    create_config_and_global_info()
                elif type(current_data["delta"]) is not float:
                    create_config_and_global_info()
            except KeyError or json.decoder.JSONDecodeError:
                create_config_and_global_info()
    except (json.decoder.JSONDecodeError, FileNotFoundError):
        create_config_and_global_info()


def get_current_data() -> dict:
    with open("global_info.json", "r") as json_file:
        current_data = json.loads(json_file.read())
        return current_data


def change_global_info(course=None, total_uah=None, total_usd=None, delta=None) -> None:
    current_data = get_current_data()
    if course is None:
        course = current_data["course"]
    if total_uah is None:
        total_uah = current_data["UAH"]
    if total_usd is None:
        total_usd = current_data["USD"]
    if delta is None:
        delta = current_data["delta"]
    global_changes = {"course": course, "UAH": total_uah, "USD": total_usd, "delta": delta}
    with open("global_info.json", "w") as json_file:
        json.dump(global_changes, json_file)


def get_rate() -> None:
    current_course = get_current_data()["course"]
    return current_course


def get_account_balance() -> str:
    current_data = get_current_data()
    total_usd = current_data["USD"]
    total_uah = current_data["UAH"]
    return f"USD {total_usd} UAH {total_uah}"


def buy_usd(usd_amount_to_buy: float) -> None:
    current_data = get_current_data()
    total_uah = current_data["UAH"]
    total_usd = current_data["USD"]
    course = current_data["course"]

    if total_uah / course >= usd_amount_to_buy:
        total_usd += usd_amount_to_buy
        total_uah -= usd_amount_to_buy * course
        total_usd = round(total_usd, 2)
        total_uah = round(total_uah, 2)
        change_global_info(total_usd=total_usd, total_uah=total_uah)
    else:
        print(f"UNAVAILABLE, REQUIRED BALANCE UAH {round(usd_amount_to_buy * course, 2)}, AVAILABLE {total_uah}")


def sell_usd(usd_amount_to_sell: float) -> None:
    current_data = get_current_data()
    total_uah = current_data["UAH"]
    total_usd = current_data["USD"]
    course = current_data["course"]

    if total_usd >= usd_amount_to_sell:
        total_usd -= usd_amount_to_sell
        total_uah += usd_amount_to_sell * course
        total_usd = round(total_usd, 2)
        total_uah = round(total_uah, 2)
        change_global_info(total_usd=total_usd, total_uah=total_uah)
    else:
        print(f"UNAVAILABLE, REQUIRED BALANCE USD {usd_amount_to_sell}, AVAILABLE {total_usd}")


def buy_max_usd() -> None:
    current_data = get_current_data()
    total_uah = current_data["UAH"]
    total_usd = current_data["USD"]
    course = current_data["course"]
    total_usd += total_uah / course
    total_usd = round(total_usd, 2)
    total_uah = round(total_uah / course % 1, 2)
    change_global_info(total_usd=total_usd, total_uah=total_uah)


def sell_max_usd() -> None:
    current_data = get_current_data()
    total_uah = current_data["UAH"]
    total_usd = current_data["USD"]
    course = current_data["course"]
    total_uah += total_usd * course
    total_uah = round(total_uah, 2)
    total_usd = round(total_usd * 2 % 1, 2)
    change_global_info(total_usd=total_usd, total_uah=total_uah)


def change_course() -> None:
    current_data = get_current_data()
    course = current_data["course"]
    delta = current_data["delta"]
    course_changes = round(random.uniform(course - delta, course + delta), 2)
    change_global_info(course=course_changes)


def set_default_data() -> None:
    create_global_info()

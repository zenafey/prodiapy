from colorama import Fore as f
from datetime import datetime as dt


def get_time():
    now = dt.now()
    return f"{now.hour}:{now.minute}:{now.second}.{str(now.microsecond)[:3]}"


def colored_msg(level, msg):
    print(f"{f.BLUE}prodiapy{f.RESET} {get_time()} - [{level}]: {msg}")


def logs(msg):
    print(f"{f.BLUE}prodiapy{f.RESET} - {f.LIGHTYELLOW_EX}logs{f.RESET} {get_time()}: {msg}")


def info(msg):
    colored_msg(f"{f.LIGHTMAGENTA_EX}INFO{f.RESET}", msg)


def success(msg):
    colored_msg(f"{f.LIGHTGREEN_EX}SUCCESS{f.RESET}", msg)

def warning(msg):
    colored_msg(f"{f.LIGHTYELLOW_EX}WARNING{f.RESET}", msg)


def failed(msg):
    colored_msg(f"{f.LIGHTRED_EX}FAILED{f.RESET}", msg)


def error(msg):
    colored_msg(f"{f.LIGHTRED_EX}ERROR{f.RESET}", msg)




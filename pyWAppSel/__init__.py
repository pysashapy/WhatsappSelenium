import random
import string
import urllib


class Colors:
    CEND = '\33[0m'
    CBOLD = '\33[1m'
    CITALIC = '\33[3m'
    CURL = '\33[4m'
    CBLINK = '\33[5m'
    CBLINK2 = '\33[6m'
    CSELECTED = '\33[7m'

    CBLACK = '\33[30m'
    CRED = '\33[31m'
    CGREEN = '\33[32m'
    CYELLOW = '\33[33m'
    CBLUE = '\33[34m'
    CVIOLET = '\33[35m'
    CBEIGE = '\33[36m'
    CWHITE = '\33[37m'

    CBLACKBG = '\33[40m'
    CREDBG = '\33[41m'
    CGREENBG = '\33[42m'
    CYELLOWBG = '\33[43m'
    CBLUEBG = '\33[44m'
    CVIOLETBG = '\33[45m'
    CBEIGEBG = '\33[46m'
    CWHITEBG = '\33[47m'

    CGREY = '\33[90m'
    CRED2 = '\33[91m'
    CGREEN2 = '\33[92m'
    CYELLOW2 = '\33[93m'
    CBLUE2 = '\33[94m'
    CVIOLET2 = '\33[95m'
    CBEIGE2 = '\33[96m'
    CWHITE2 = '\33[97m'

    CGREYBG = '\33[100m'
    CREDBG2 = '\33[101m'
    CGREENBG2 = '\33[102m'
    CYELLOWBG2 = '\33[103m'
    CBLUEBG2 = '\33[104m'
    CVIOLETBG2 = '\33[105m'
    CBEIGEBG2 = '\33[106m'
    CWHITEBG2 = '\33[107m'


def getQrUrl(data: str, size=300) -> str:
    return f"https://api.qrserver.com/v1/create-qr-code/?size={size}x{size}&data={urllib.parse.quote_plus(data)}"


def printQrUrl(url: str, time_out_second: int = 20):
    print(f"{Colors.CGREENBG}[Log in]{Colors.CEND} qr: {url}, time out: {time_out_second} second")


def generationToken(len_):
    letters_and_digits = string.ascii_letters + string.digits
    rand_string = ''.join(random.sample(letters_and_digits, len_))
    return rand_string


def findCommand(line: str, start_command='', is_command=True, kwarg_sep="/", *args, **kwargs):
    """
    !!!! IN PROGRESS!!!!

    """
    commands_line = line.split()
    data = {"isFind": False, "kwargs": {}, "args": []}

    if commands_line[0] == start_command or not is_command:
        data["isFind"] = True

    kwargs_keys = list(kwargs.keys())
    last_is_kwarg = ''
    for arg in range(len(commands_line)):
        arg = commands_line[arg]
        if arg[0] == kwarg_sep:
            for kwarg_ in range(len(kwargs_keys)):
                key = kwargs_keys[kwarg_]
                if key == arg[1:]:
                    data["kwargs"][key] = kwargs[key](arg[1:])
                    del kwargs_keys[kwarg_]
                    break
        else:
            for arg in range(len(args)):
                key = args[arg]
                if key == arg[0]:
                    data["kwargs"][key] = kwargs[key](arg[1:])
                    del kwargs_keys[kwarg_]
                    break

    return data

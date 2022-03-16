import random
import array


class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    WHITE = "\033[97m"


class ValueTypes:

    INTEGERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    LOWER_CHARS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                   'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                   'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                   'z']
    UPPER_CHARS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                   'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                   'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                   'Z']
    SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
               '*', '(', ')', '<']


MAX_LEN = 20

args = ["-s", "--symbols", "-n", "--no-symbols"]

combined_list_symbols = ValueTypes.INTEGERS + ValueTypes.LOWER_CHARS + \
    ValueTypes.UPPER_CHARS + ValueTypes.SYMBOLS

combined_list_no_symbols = ValueTypes.INTEGERS + ValueTypes.LOWER_CHARS + \
    ValueTypes.UPPER_CHARS

rand_integer = random.choice(ValueTypes.INTEGERS)
rand_lower_char = random.choice(ValueTypes.LOWER_CHARS)
rand_upper_char = random.choice(ValueTypes.UPPER_CHARS)
rand_symbol = random.choice(ValueTypes.SYMBOLS)


def init():
    print(Colors.WHITE + '''         
██╗░░██╗███████╗██╗░░░██╗░░░░░░░██████╗░███████╗███╗░░██╗
██║░██╔╝██╔════╝╚██╗░██╔╝░░░░░░██╔════╝░██╔════╝████╗░██║
█████═╝░█████╗░░░╚████╔╝░█████╗██║░░██╗░█████╗░░██╔██╗██║
██╔═██╗░██╔══╝░░░░╚██╔╝░░╚════╝██║░░╚██╗██╔══╝░░██║╚████║
██║░╚██╗███████╗░░░██║░░░░░░░░░╚██████╔╝███████╗██║░╚███║
╚═╝░░╚═╝╚══════╝░░░╚═╝░░░░░░░░░░╚═════╝░╚══════╝╚═╝░░╚══╝
          \n''')


def generate_password_no_symbols():

    temp_password = rand_integer + rand_lower_char + rand_upper_char

    for _value in range(MAX_LEN - 4):
        temp_password = temp_password + random.choice(combined_list_no_symbols)
        temp_password_list = array.array(
            "u", temp_password)
        random.shuffle(temp_password_list)

    generated_password = ""

    for _value in temp_password_list:
        generated_password = generated_password + _value

    print(Colors.BLUE + "GENERATED PASSWORD: " +
          Colors.GREEN + generated_password)


def generate_password_symbols():

    temp_password = rand_integer + rand_lower_char + rand_upper_char + rand_symbol

    for _value in range(MAX_LEN - 4):
        temp_password = temp_password + random.choice(combined_list_symbols)
        temp_password_list = array.array(
            "u", temp_password)
        random.shuffle(temp_password_list)

    generated_password = ""

    for _value in temp_password_list:
        generated_password = generated_password + _value

    print(Colors.BLUE + "GENERATED PASSWORD (SYMBOLS): " +
          Colors.GREEN + generated_password)


if __name__ == "__main__":
    init()
    generate_password_no_symbols()
    generate_password_symbols()

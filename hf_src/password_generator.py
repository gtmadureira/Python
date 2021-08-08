"""
Example of how to generate a password with standard libraries.
For educational purposes only.
Works on Python 3.
Source:
        https://github.com/gtmadureira/Python/blob/main/hf_src/password_generator.py
"""


from array import array
from platform import system
from random import choice, shuffle
from subprocess import check_call as run_command


# Tests the operating system type and sets the screen clear command.
if system() == "Windows":

    def clear() -> None:
        run_command("cls")

elif system() == "Darwin" or system() == "Linux":

    def clear() -> None:
        run_command("clear")


# Password generator function.
def password_generator(length: int) -> str:
    """ Return a random password. """

    # Maximum length of password needed.
    MAX_LENGTH = length

    # Declare arrays of the character that we need in out password.
    # Represented as chars to enable easy string concatenation.
    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    LOWER_CASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                             'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                             'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                             'z']

    UPPER_CASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                             'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                             'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                             'Z']

    SYMBOLS = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*',
               '+', ',', '-', '.', '/', ':', ';', '<', '=', '>',
               '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|',
               '}', '~']

    # Combines all the character arrays above to form one array.
    COMBINED_LIST = DIGITS + UPPER_CASE_CHARACTERS + LOWER_CASE_CHARACTERS + \
        SYMBOLS

    # Randomly select at least one character from each character set above.
    random_digit = choice(DIGITS)
    random_upper_case_character = choice(UPPER_CASE_CHARACTERS)
    random_lower_case_character = choice(LOWER_CASE_CHARACTERS)
    random_symbol = choice(SYMBOLS)

    # Combine the character randomly selected above,
    # at this stage, the password contains only 4 characters.
    temporary_password = random_digit + random_upper_case_character + \
        random_lower_case_character + random_symbol

    # Now that we are sure we have at least one character from each
    # set of characters, we fill the rest of the password length by
    # selecting randomly from the combined list of character above.
    for _ in range(MAX_LENGTH - 4):
        temporary_password = temporary_password + choice(COMBINED_LIST)

    # Convert temporary password into array and shuffle to
    # prevent it from having a consistent pattern
    # where the beginning of the password is predictable.
        temporary_password_list = array('u', temporary_password)
        shuffle(temporary_password_list)

    # Traverse the temporary password array and append the chars
    # to form the password.
    password = ""
    for character in temporary_password_list:
        password = password + character

    return password


if __name__ == '__main__':

    clear()

    # Asks the user for the length of the password and return the result.
    while True:
        length = input("What is the password length ? :  ")
        try:
            val = int(length)
            """
            if not a positive integer, will print message and ask for input
            again.
            """
            if val < 8 or val > 128:
                clear()
                print("The input must be from '8' to '128', try again.")
                continue
            break
        except ValueError:
            clear()
            print("Number only! You must input an integer, try again.")

    # Else all is good, val is from '8' to '128' and an integer.
    clear()
    print("\n\tHere is your password with '" +
          str(val) + "' characters of length:\n")
    print("\n\t" + password_generator(val) + "\n\n")

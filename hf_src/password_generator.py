# Example of how to generate a password with standard libraries.
# For educational purposes only.
# Works on Python 3.
# Source: https://github.com/gtmadureira/Python/blob/main/hf_src/password_generator.py


import random
import array


# Password generator function.
def passgen(length: int) -> str:
    """ Return a random password. """

    # Maximum length of password needed.
    MAX_LEN = length

    # Declare arrays of the character that we need in out password.
    # Represented as chars to enable easy string concatenation.
    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                         'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                         'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                         'z']

    UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                         'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                         'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                         'Z']

    SYMBOLS = [' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*',
               '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?',
               '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

    # Combines all the character arrays above to form one array.
    COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS

    # Randomly select at least one character from each character set above.
    rand_digit = random.choice(DIGITS)
    rand_upper = random.choice(UPCASE_CHARACTERS)
    rand_lower = random.choice(LOCASE_CHARACTERS)
    rand_symbol = random.choice(SYMBOLS)

    # Combine the character randomly selected above,
    # at this stage, the password contains only 4 characters.
    temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol

    # Now that we are sure we have at least one character from each
    # set of characters, we fill the rest of the password length by
    # selecting randomly from the combined list of character above.
    for x in range(MAX_LEN - 4):
        temp_pass = temp_pass + random.choice(COMBINED_LIST)

    # Convert temporary password into array and shuffle to
    # prevent it from having a consistent pattern
    # where the beginning of the password is predictable.
        temp_pass_list = array.array('u', temp_pass)
        random.shuffle(temp_pass_list)

    # Traverse the temporary password array and append the chars
    # to form the password.
    password = ""
    for x in temp_pass_list:
        password = password + x

    return password


# Asks the user for the length of the password and then returns the result.
def input_password_length() -> str:
    length = input("What is the password length ? :  ")
    try:
        return passgen(int(length))
    except:
        print("Number only! You must enter an integer, so try again.")
        return input_password_length()


# Print the result on the screen.
print(input_password_length())

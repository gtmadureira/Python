from typing import Dict

vowels = ['a', 'e', 'i', 'o', 'u']
word = input('Provide a word to search for vowels: ')
found: Dict[str, int] = {}

for letter in word:

    if letter in vowels:

        found.setdefault(letter, 0)
        found[letter] += 1

for k, v in sorted(found.items()):

    if v > 1:

        print('The volwel (', k, ') was found (', v, ') times.')

    else:

        print('The volwel (', k, ') was found (', v, ') time.')

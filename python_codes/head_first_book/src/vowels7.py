vowels = set('aeiou')
word = input('Provide a word to search for vowels: ')
found = vowels.intersection(set(word))
new_found = sorted(found)

for vowel in new_found:

    print(vowel)

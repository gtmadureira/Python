'''

-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

'''



vowels = ['a', 'e', 'i', 'o', 'u']
word = input('Provide a word to search for vowels: ')
found = []

for letter in word:

  if letter in vowels:

    if letter not in found:

      found.append(letter)

for vowel in found:

  print(vowel)



'''
-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEE8iavjRZ2/dKhzGiBXQppWFastkFAl6Uz/4ACgkQBXQppWFa
stkUiQ/+IB+N4s0Eh5KppSVUlUl7EmDOt9bkWsUr3Vj/jq4vawmGptLmFY8aN9bF
Ho0o3diQb9qR9+GZCX4fCgdqG4ExVHegM6UgwsGwqcGNBhVOeGPlvN42MYtn8hKk
6GHguATphhcyZvW7k2eVKB/k2hEUSz7onkAuhDCkm3JqvNSDWyCrXcwQrxuopxPn
vo8bkRgTzW5BA55kQUe/mJbJ4+ynB0/ToPMrBO2OUDvh11xFvrolMMI8dPy9fVPL
5QlNRL1HhL0r68LJkVGc9xJITbZ/8hEDSvQtiheT2tOzA4mjGZyxZ8RkRlPI/MkJ
Fk+8COQL45I7PNqfOJvaQML9YNSQ1gnelYG0XGxpDTOfrbJjQfFqeopAlGg2jdZK
UBi0LUydeADp4arDo4httWnIqRlfMoHvPGhHLdSqzJKwltVMMzbYKwLDGv+r7zHd
WtfARAZCweO9geEvGxazrIWIU8CSlkZn3hvjgjHKOAvpGW++kajkP3Z3C0jkdE5M
vYD6TkMijvVBKo4fwxROqKVNVbgJjmAbgXU1xdHpp8iT7672KPhn4CYqiqtkwAzx
mt2DfuhdAS/8oVrC3cHUSvzbpCWbn9BmHGvwQ1aaVGT0QOJFec77ik2mNHDfzNpU
IuFDx7Ml+cuETSu3Ru8YlEaf9VnNy+gK/gRDbmPlJxAysgCpbRo=
=P33T
-----END PGP SIGNATURE-----

'''

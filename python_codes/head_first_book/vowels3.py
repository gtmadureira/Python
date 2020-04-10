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

iQIzBAEBCAAdFiEEE8iavjRZ2/dKhzGiBXQppWFastkFAl6LtbIACgkQBXQppWFa
stkDOw/5Abad/FX5SFpL2i2U9pjcJVZXtFd+8rGw9egChSr2q9G+fX8EEXn3TfjZ
YDD6M7QWXw0cZhAtwRVO8GtquH1N0EcN+leaBki0aPS5Rao1WtmUr2SR9958tGGc
iRQUEPXzyjEs423gwGklSXpGZpK0aJRCyyFJZES1tyxJzarSVW5j7o/RkpW2khrZ
lkYPGRFHRq2OQBWjOVwYnaDDyqb+ODQAk+xLjAbFmCspY0EdV5GQrskPXCDXUmQ6
hHMIopovR0lpeHqJ32NUQ7zdhETPNRcqTVTMsB61AYn0AUp2mO5iEyPasaoFaawL
9xRkWUIqgWQbvjWWkueGp67ULL4PssdSjOAItIK8oHKm2zXvavCEn44Re5ZzMdB4
wpJkfloR6i0uk+nm04K4BA6a4TuEVNOAyaoK/8XiliT/tRNuUeanNO3pPmcTx+2t
0m6d8wGVoGbOLewWptD5c+UuXLvlWqPPOTYICnzNhZJ/JnNfiIn3IrT/Tj9OcvaC
cRYUkjOfPeOLAcgbtfvy3Dpllj4pcMS/ERYpQYvp1eXvXVHvkV6LMcANJykR3z6I
v9DkoYFK6ym4ZFz3EVG+9xKrniaU3nGrY7mHfQx4+iGEz+hwGD2SIJ8tZIQ9rwIS
AOjfDyp1x0yKUZcv/jSzfD6HmSfBlB0Q1Dx2DvVoV7Y2hANNWrQ=
=b4+F
-----END PGP SIGNATURE-----

'''

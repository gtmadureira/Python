'''

-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

'''



vowels = ['a', 'e', 'i', 'o', 'u']
word = input('Provide a word to search for vowels: ')
found = {}

for letter in word:

  if letter in vowels:

    found.setdefault(letter, 0)
    found[letter] += 1

for k, v in sorted(found.items()):

  if v > 1:

    print('The volwel (', k, ') was found (', v, ') times.')

  else:

    print('The volwel (', k, ') was found (', v, ') time.')



'''
-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEE8iavjRZ2/dKhzGiBXQppWFastkFAl6TwKwACgkQBXQppWFa
stkFSw/+LCkehDExriFKE9J6NlfssSidbhbinDPR6Io2Nxg+kJIugdoJBTsx3NC5
mVECfWkQ7pki2TlyHY2MJB3tjvinr0rBeXfm05sR3ThM5kzVrocsRjbdWgSaMR8U
dDTpXpBxQgWGgXytxwD7e2vWeZ0xi/O+VV0MX14Ru6IC52lvBCL4RZo4zOcvKpRl
lkIjLFZ+BvtL47nhbaULUgUG+Qm8PZiR99f7ImuXQBd4qjTMNzWPoCWfDQKWTvOX
3cAIdpJUDxmLTkdojwrWJO8pgpKxwBbihzKc/5J7j0DLTAhjANmERpAJmgpsXc+F
f+V1Ao6Uu3VLRdkqxSS1m41yZm+n6ZNLxfhWLMdH1o7OzfMSCMrQLEdNJz9ftB2H
yU8/dLKlVfNfAkRczLHGrF6K5f8gpTlI8rl9V8zZm3jxAiSm6j5Mk3F31SBhADxQ
kg3AE23nq0if+OfHsV+PAgE37xABhbl/F9M086xSivEAvyGYz3VcX/etATbsnPUC
gwIjH7RD0SpmpN31Itddu4wyyYmFYACDBeaaeKkBtuXBkBe1CtvS0n5VpT6KPBrz
52dw7c9UwiF8Gfpx9sJ1mvntEBhJtGyHtVeHc/mbIEQqAGTjK0r0bUgCePlPzaZS
m2pHTJzrL9A4l7J/z4fpXnhFN8MzXpwGmeyV5a4/kKtclbE3PWM=
=RFIo
-----END PGP SIGNATURE-----

'''

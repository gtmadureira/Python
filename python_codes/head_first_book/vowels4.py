'''

-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

'''



vowels = ['a', 'e', 'i', 'o', 'u']
word = input('Provide a word to search for vowels: ')
found = {}

found['a'] = 0
found['e'] = 0
found['i'] = 0
found['o'] = 0
found['u'] = 0

for letter in word:

  if letter in vowels:

    found[letter] += 1

for k, v in sorted(found.items()):

  print(k, 'was found', v, 'times(s)')



'''
-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEE8iavjRZ2/dKhzGiBXQppWFastkFAl6RXi4ACgkQBXQppWFa
stlwcxAAjsjofTJDixYVc3QD29qo8np++JWzR0mNcdyDteYRidkgDOHCQf9+XvKd
KmFWCIOFhF+aHzSZvHZzqSx+f7zzzlSru+6v7lQOhNZai3fRMXOub3mZbF4cEqsV
wnKdXWv254wKantgU6Eust6ZpCZPyQZL34IuIg9kDJFmoOeFGoPp6h96GlpXK6nk
5e8+k4EX4bl57ED9czVVGjaNXr+GZdiewcGgR3potEpbdBZNC5zC9a4XfIGUF0Mw
Hj0M9jDbGIJ+ay++fexyVExwtvCTEp7yzWKU9jnTz3Xd9K2vL5QmtpbtsWkuV7/d
48JtNiju25aN1GkKM3FFXT8AjcQfYNcJF/TKrprYcz7L/wCBkW+34OHReqemEft/
YjX6NWzgH/RGYuBuJo1EAkQbkIbLfdhgppDQMJdiy9E6gTKUOj4rqo4mxVfjpwgg
SrE8sLMHUnLrH0+dObcJR9OV1lvLWGfIoZsLMRydX2qXLdV4Txljk6/aT1Z5FGF3
X4dZBi2Wpz8PRwPm3/WbZxZNylKvQDO5c126CGdTYPfqK3SCd9pyi3QxBxTuLscQ
9flRa6mxvB1A/x4Sj4ljgc59G9xn6EFTE85aezGR9zFs6gds3M6PCIpi+HQw9A9T
ty2PoLtlTS0w0BJsXE4ZGo4EtBd9HjyoBuYeBVhg9DwwIi6nyD4=
=nsrK
-----END PGP SIGNATURE-----

'''

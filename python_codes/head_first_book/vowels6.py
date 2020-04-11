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

  print(k, 'was found', v, 'times(s)')



'''
-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEE8iavjRZ2/dKhzGiBXQppWFastkFAl6RDI8ACgkQBXQppWFa
stla5BAAjHU3n9ixcOVSr3z+rd/xgX00Naz3VcGeISZe/h6xl1fyS1DfTDbWfUcy
tr2Oukbo96SPHbvQXTDMfr6IKIFtbDx/NL2Y9gJgR92Q6K7NgTNSynTK16mHaiJq
YAAjSNUsS/mi3I/UlFLn5K+B+lJVWgQBkgwb0VnmC+VPf1saGmpH3k15H3b2hAiU
qZS1LHIUY/CUrlqPi8gMCJGav11O5/94Lcs/9EMoLs2WjC/+VnirwL2tzoX8ycUs
3QsxN5aiyaPprZp+aL/V7stKNzdL3YeG8YTcyKm4+fF9LbFbcIufxFLgC9DZqAfh
gox9z4JA3NACRotvPlUKL5RhI/dWYlqmWQxMFTSIL5Y9LT5bRsWUL1O8yLQODiJ2
JgXgw3LBkmdMVNELjbpalfJSrkpF7iFMAeCtyZRCgpN7/EvlLnHCqQzpvuV8CWHr
rqiljr1IcRvrSTPEhO02Cn2ouKpmgMZC0xyOr/yYHrfyTlr9bvrSNfLojy9RuNFp
1DR57vY7Cr/1/e1wRRuuqfXG0UfO5rwzRfTWCK9BbrzCrdWc8yZKmgHmn+h/RSc8
o1qX+r1SgVOJAN+iQtExiLw5g1F5vxsXxsxds6uMCNihUA87RwnR35XA+uHmZY9z
9USljgXO9LcpgI8Q/LSXte8GyhftW2cNTH8FQnH1UW69YeBih+E=
=a+RS
-----END PGP SIGNATURE-----

'''

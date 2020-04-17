"""

-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

"""



def double(arg):

    """ In the function suite a new reference to 'arg' is created, but in the code remains the same. """

    print('Before: ', arg)
    arg = arg * 2
    print('After: ', arg)


def change(arg):

    """ The reference to 'arg' remains the same, both in the function suite and in the entire code. """

    print('Before: ', arg)
    arg.append('More data')
    print('After: ', arg)



"""
-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEE8iavjRZ2/dKhzGiBXQppWFastkFAl6aOqQACgkQBXQppWFa
stkePg//Vw6YdjB6PsohATSvxlne7kPKP+e8QJTCOtebBY++BDQGe/mIhfPv+3EG
CkIm2BFeNu8z3/uQ9w/99dGUWU7vT9dDF5Md9lzEZN57JAf5TLARd42ZuT2VH1dk
WqBbDQWDjQdUVlm3ZyquJvKDigv0c9VvOwKsX/N3mQE/K2O9jkKk+3sszBERuDuC
tzixi+/pMe6gfTFpPdb0bLFO52xdZqPYDUChthGDFYfvZr4yZkecHT/W9a6olPHL
tCkxSkD6NZpIrX5jNcYq9u2wpNs+Cw5y4FU68ZKeBlM+zQYX1gG0t8heQiWfk0jC
eyGUwUbLhDVrUKK8r28mjPuIakQ4Coi7qTuJR5BdGnjoOq9V1b7+hgUiI+6ZCNZy
3vK0tg6x2aMv2bavNHlR1B1YYvh7GikjtHNCVKevEPT6/EwgFrRF9kkQHezEtmDo
Keyej+d4cXDQrm8ooTRbmsReO/sE6rT63n2zZ6Nudq6tYFhuetPCzS+ZXFA+0oao
UNWEpRjNBThJ+LfDdBDBgmcX4Py34y7mMdUbbeQzLtl2k3PXfgM15oGDafpt/px/
5b/YWNSavu+8+P9H1q8fxqQk/12kAgJonEfoCMeBc+EruJOD7J95KwrseZXEq3uW
daZtOQIGiKrKmGDRbGwn7SRNgaVP1EullN+nBJnBOLWoNy8WiH4=
=c3mX
-----END PGP SIGNATURE-----

"""

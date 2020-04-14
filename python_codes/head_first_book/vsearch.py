"""

-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

"""



def search4vowels_sorted(word):

    """ Sorted and display any vowels found in a supplied word. """

    vowels = set('aeiou')
    found = vowels.intersection(set(word))
    found = sorted(found)

    for vowel in found:

        print(vowel)


def search4vowels_unsorted(word):

    """ Display any vowels found in a supplied word. """

    vowels = set('aeiou')
    found = vowels.intersection(set(word))

    for vowel in found:

        print(vowel)



"""
-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEE8iavjRZ2/dKhzGiBXQppWFastkFAl6VSmIACgkQBXQppWFa
stkTpxAAmJjjlqurtIXz9xPmLs3j6Y71CCnYrwDOmq5vgZ4D1OiwP9kI/3de8Mky
ZR7bDxOLs9xD1+5RnsfQdAYz7a9KQlqi8T1X4XN71YwTS6GpNJJzs9R1Zl4A7cig
F1OdL6w4D0JgWobkefFM/LBVUxCOMD95evNqrNf9DCYPv9Wz57Hhx68f8iS8Bo95
MBCspOBwHqDi6KJETuQuKkK0iSfXyMaVRVfG3YuOvJQn3Gy8nYdBRhM1sEm5rWxR
HOgyGBDsFV4I9xvDJRkeV5pcjJ70IdtrvgLRIUYuV6LqIPj6lEWNXfoU62V+aazf
moho18XhZHjFN2Zk6q6oEZ7w6Aaa4b7nlqIvxLRaAaeimGbd107BAYJwavh/DZKP
z3aE99Adjp1wstHFzmXxzT2uP9YmSw2OwXzbeJlsXPGL+gpAMY7i73lt1aR0WyYq
b5MXPiJK6rgQiIAFh2ONRvCZg2eID0m7cKcAsYsDtMl54b8+EVRXErrPE12RPV2J
joTOo6/qqaGZFtPKy38QjjTjJx7EretoWNwHmDvn6aRa0tzr7YVX+59S7qcSPFX0
gHREHghL+Po6rHaBpY4OlKfRbS/Umql5Vsp5cA+fj5e85tSpt8fALXWJP4mZ8exb
2oD5pW1gyu2HXbNZgRo44eR3QqCk6d4AN4RiRpahIwVayBB5qIA=
=rogF
-----END PGP SIGNATURE-----

"""

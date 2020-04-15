"""

-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

"""



def search4vowels(phrase:str) -> set:

    """ Return any vowels found in a supplied phrase. """

    vowels = set('aeiou')

    return vowels.intersection(set(phrase))


def search4letters(phrase:str, letters:str='aeiou') -> set:

    """ Return a set of the 'letters' found in phrase. """

    return set(letters).intersection(set(phrase))



"""
-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEE8iavjRZ2/dKhzGiBXQppWFastkFAl6WhIsACgkQBXQppWFa
stmQFg/6An8MCcSneA7hNV7SVxoYZZqN4uzmd4c+lqKy5hK01yq+h3yACDeA9DZF
D/8p5DRtvu/T0zMV1frcPo+3r3bBa1rmXHy4g/wddXc+Tawves43ttI5XN7sVEH3
1Ns2c48etvF5hfkP1F0wkhp4EyDMFkdWHJmJieAccekM/hH5C7dKMJ/3GSre4JW2
Yk8+5YypL7OiPekhqlf1Y8gbmtIzZBsxjnsxIaSUQWixQa31NVLBSQKoGwpedTfq
3t+PJIP+tziF7H5Kgh7QpoQDzdX3UkZ6sTbo+5sAW8i6v1OhGAxg/zRK64dPGnSg
CKX9ItrfIOsEgpxorCM5z4aZouOntLgSSBvGSn6bRjkn5n5Inhio1qhDNZr8cifq
1omUFSZqZ/E7UwrYNAeAh5sFPcZXshU/kavc0yZDE2aFOdSmyeIhCfGN5jjDyDWt
8LoP73pKTG5EECkH/BHb8DA5H/gPzHwpYIgHdOiFDhAj7N+ac7QkdOXyjAv/eTWs
TIcLE9qEI/6NYWLJIsWBXflTkIW7vqon0ls44+UPe+DCXDmKalN0Cc1rnfTXAXsK
X7QNwLvCJtNQZF8S07IY0ZzU1zA6DKhNPbZjM1HpMC/0zFj0xngIS6R0KVb4ZIUe
lMGa+PpGSbszKt4db7GE65AY1CSIOKYyACGd59b+Zlzgmpl6XOk=
=WOHs
-----END PGP SIGNATURE-----

"""

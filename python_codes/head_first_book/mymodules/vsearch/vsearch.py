"""

-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

"""



def search4vowels(phrase: str) -> set:

    """ Return any vowels found in a supplied phrase. """

    vowels = set('aeiou')

    return vowels.intersection(set(phrase))


def search4letters(phrase: str, letters: str='aeiou') -> set:

    """ Return a set of the 'letters' found in phrase. """

    return set(letters).intersection(set(phrase))



"""
-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEE8iavjRZ2/dKhzGiBXQppWFastkFAl6aVSYACgkQBXQppWFa
stnTXg/+NgeHQSpqjLAZynZ3jJGB3Ok5XHx4AC98Q/rv8myfpfK9UG0zOsbLBVLR
r7a56dtHdj1plS98+4NlgifZUhos5kPGTW8XioUWF4UP8ZFMBStjYqIin2aCYi+r
EAsX9x0JflT23xm3GFwNRVnnOCxrtqlRwJrXHSgF8bB2ztYw4DAjNfXC/K3hmaN2
qivqvYC9K3XUvqhfMqAULPU2vumbvnmmkUguUiirzx+1etsvVOsRKoMHUg4aVXGW
JOF8XqzwlMKzMHYWZ4li2D21meuHXz1M0vFVd+M6SZYaH6w0P4Hi745ZdTS5t4uz
m8jUpHzptu9f8dz266ktuZbVfO+ndXuYaJXuSXvfqhfJSUIUf50lN4taDQoiguUy
jGpbEzVGyIg5lHtgSUvPWaONO6QcvR3aj83+asm6T8fWBjfaeD5uErpG7DEoIVz5
k9GEnJal9RiEkWMln75BI5VrlOYyF0MiJO1cLkUdjlcQylhtzAHPMOSNiEhJvYXl
akf1SoL3rhCB2anloKF8zCnmQ+3MV/YRblJ1N6vmhQ1rUBrOMHY+mxhqvbSEcADE
WtRQXZi6OLBOiy97jigTVK9+3FXv8inH9oI7u+RPz2nzaw3RKyGKSfL/wjASf12+
3ibMO5NuneiTmLIihTh7kAp3O6PvEn1Yi/B1LcTJ+nyGq8EexA8=
=WPMN
-----END PGP SIGNATURE-----

"""

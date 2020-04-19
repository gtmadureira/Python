"""

-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

"""



from flask import Flask
from vsearch import search4letters


app = Flask(__name__)


@app.route('/')
def hello() -> str:
    return 'Hello world from Flask!'


@app.route('/search4')
def do_search() -> str:
    return str(search4letters('life, the universe, and everything!', 'eiru,!'))


app.run()



"""
-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEE8iavjRZ2/dKhzGiBXQppWFastkFAl6b2qAACgkQBXQppWFa
stnjsQ/9EJ2k6w6xWVu4th3O43ju8wBiOo3DuTpNurwMFpHxsWsZlz33lDRkhBmf
bplWzw9l6to77J4aXTJONrw5QcucU/CQEzecu7Uxt0YAs7dYzFM8gNRiO9sEg2/n
c6pHRb2Nmajpd7ujA2uf0pJ20U/pixiRkkHY/RlyyuxvarNwaz08qoG7R3jUliBR
LUSQ46iXx92R01J3xH61E1QcSlyR2+ez+cAg648l9Ki1K+tirsoXq3QSo89xwjpM
BLAjTGD0eKV3DFMCUI1dj7fWzm6HH1mjtIS9iYh976X9iV6YARtry7i3cEdvggO3
UfepJ0zxMzrOLCtGp00E6ZhXt5sEIHYLDm43ferzUQ8aZQA+Tb9Xy5phGsu2x8Tl
PnkqPDjwOzW5qDywCmXMn3IrQglwMNEjISBuEQnr1ADQnXsSHWw4QmKM3kKUrLKZ
jMV6/8n6ncgImFRf3t5pre4MHutV29V7z57gSziAJRE3CvrBuYh9SFCVn9b0VDhO
vplHXBhwD4NmENGxuk6dh7TywmJmho3NnNahWsb39lvNM/JdZa5+miGgARJ9hE3x
Q22rb7qFoykvajj9IoQlawGC2dHQeBnC4qKhtcZystpzUHkXF6Qy8PGwnG9KKF3K
a4JHL525Lis+tBilLxRX2yBIivU3WsdB6cn2iJGZ/ALZ181i7Qs=
=aWkD
-----END PGP SIGNATURE-----

"""

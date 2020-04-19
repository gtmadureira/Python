"""

-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

"""



from flask import Flask, render_template, request
from vsearch import search4letters


app = Flask(__name__)


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(search4letters(phrase, letters))
    return render_template('results.html', the_title=title, the_phrase=phrase, the_letters=letters, the_results=results)


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Welcome to search4letters on the web!')


if __name__ == '__main__':
    app.run(debug=True)



"""
-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEE8iavjRZ2/dKhzGiBXQppWFastkFAl6cysUACgkQBXQppWFa
stlGWA/9EVLHeGj1I9cm4fbQz9WW871ork7IML5yItTBXP6tR8TwFJ4BiFttEzGy
yYZLrinU8SOi6WYNSss3/BbK33keNNGqMJenfeFTNThf6q65xZepEP7SxWUdtBat
/EQ0uKliw0SWN0PvmsYjaltIj11GtkqK5wJPrFfwKF0rqKRjpbapMxzjpQPVfNtg
MI8ePQzExG9TmQixk7YNb3HZgz53R3AGD2hUy6DG+rmTKqS5uE4MEtX8W/8OSN9J
npdLnwrYPn60VEgHElb+VcADA1BcZ0K0sLW1nqfx/EZUniI8t8Nv3qEZJF3LVxDH
lDHPXHukGfIm9smj80CfKO1jBUxZV6XlhPiCwGgKSyVIZKUZZNfpNL37G1ZDI8XR
cBLZyIencCZLNUdaIezen0BbiDyIsMvdviEW5xbFKxUXvHpOUXwgv72owl8S2C/1
MgzhEQ08u3z3uve04J9WowOwQiqNiL+3+Lp5JVkW/yQy0rYcKyWcoEJNj79p+bYl
eWZAUP2INvZBukB7y+fdiHnHZBkqPd8DzY8v+WZLP9W8pLRva8MXILZVu48lnS12
mHHDQitKKy9mSWCdDn9BuineOXZeZNIJKS7pbDwwtvCiUo89gcziV7e2I2uE3UZR
BI56NSx5AvNju50IZFcfODrMpQgUtksFMRs/2ZgnXv+pxVfN4mQ=
=TP4q
-----END PGP SIGNATURE-----

"""

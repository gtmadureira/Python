"""

-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

"""



from flask import Flask, render_template, request
from vsearch import search4letters


app = Flask(__name__)


@app.route('/')
def hello() -> str:
    return 'Hello world from Flask!'


@app.route('/search4', methods=['POST'])
def do_search() -> str:
    phrase = request.form['phrase']
    letters = request.form['letters']
    return str(search4letters(phrase, letters))


@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Welcome to search4letters on the web!')


app.run(debug=True)



"""
-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEE8iavjRZ2/dKhzGiBXQppWFastkFAl6b22oACgkQBXQppWFa
stmDOQ//XDbzOAVaoKK9TMaorpvxWstzt0jSv+M0I0gC7LhuA+zL/1IcfwA95x6W
jBCtmUZi9Z9JpqUgUNPvr9rm0vPTCy2aX4VgzYJU7iF3WFaVUCmQry3/Tvnswovn
exFJJUIovTBzKzOIkR+aRHKjoKbD2qGwM8z2b0s7jAoUFe5USwPRQIgdG/6Kyn+E
O0MOs9BZywueuXabS2DtaBhSj7DC6uhq5Ka4t41lxP042U1rZMHR7K6CWmN8Roxq
Z2tnUMSBeSk+ZQGpetOxrw9XQmUTL9N35nGvnQ9ImTKNuorQt3ZYy9EF5yNxyehc
kjtSWEEqA+A+7B/W8E5BKyhl9C71fspdBkllgF7ALkGYMW+gylmdO9MJqBhHZyES
W8g5v2INakjIrFUKGgKDkVnpuUYsQBTad/7DIxbxiMRlNOcRZr5qzRCxWi/Mk+0J
ZOsjkrkBR7Cd9oCgxkQGS/d1OUXds+r4xEPY1jqWyyMTJCzWjWxGhKWj+v8EI1My
l4Sv1z5LTMaZLqYLFO2BFtmmnQ5aVUxcHhB1xqZ+wl8UBaBo2wLGpm4xFPvV+96D
m8ty/wvot0yXibK5qLbGDp0jgzqgszOEgu3hSJVCL3oNOilZjjXk/CNNOVcIDxWV
0Pvor8+ZgvnVppGH2aWxtJqH8o4ZnlkU1PKE3wTgtZIb4rDO4W0=
=Inal
-----END PGP SIGNATURE-----

"""

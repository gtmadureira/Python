"""

-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

"""



from flask import Flask, render_template, request, escape
from vsearch import search4letters


app = Flask(__name__)


def log_request(req: 'flask_request', res: str) -> None:
    """Log details of the web request and the results."""
    with open('vsearch.log', 'a') as log:
        print(req.form, file=log)
        print(req.remote_addr, file=log)
        print(req.user_agent, file=log)
        print(res, file=log)


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    """Extract the posted data; perform the search; return results."""
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(search4letters(phrase, letters))
    log_request(request, results)
    return render_template('results.html', the_title=title, the_phrase=phrase, the_letters=letters, the_results=results)


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    """Display this webapp's HTML form."""
    return render_template('entry.html', the_title='Welcome to search4letters on the web!')


@app.route('/viewlog')
def view_the_log() -> str:
    """Display the contents of the log file as plain text."""
    with open('vsearch.log') as log:
        contents = log.read()
    return escape(contents)


if __name__ == '__main__':
    app.run(debug=True)



"""
-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEE8iavjRZ2/dKhzGiBXQppWFastkFAl6edCgACgkQBXQppWFa
stllLQ/8CGS86/edn7769gLyFUhWm8fWgFb4xpoFG+VmYA2w8FZh9HEHQBWwASmE
8TE+ccMgWPrg8l1HJAnjTaJlJBsNCX0rLOfCIbbkkjGWwlSJWnoJ8fTzSl0cXABw
jpTW3vlckLYk+D3FNBx4duWgKXuBNPopfSXkvyjH/jKMeWVo21+ZPLTnRNA2Nzkk
OgYi5UgggVVhIypHjlqst69IbLx15zOELosQZaWNPMIUjYzI+rN+NPrsj0V+n3V9
5PPwa1/bO451+VR3QRvfYGpCdUPimWbLS5uj57TqPj2mGsx5SxIzPI8lOcOR2vzP
b4F29n18ddBUNGVbWTXR0GDeKO2iE7G4HI1+nr/O/+ppwKrojyxXIaaqNyAMV1VP
cifL4QHyHf32xAdJWJk+CHiNTBCSs2AdAyp2RJZOL/arlv2uasOmXu/tEjXg2WVc
Pt0ZaS54uVx4IGUfeWFlJdrws4lj6Y85/VYsnS/snnNNxyicDTg6H58va6yJycdf
e0Pcwi4SyTerYaFAU8NV2LVnV9ljqJtKCu/1I302ZNfOe0qmAG9UijVVrj2lv20e
5xjlmxQyRWWmPqaV0yFB6P37Ru2BSm4LLZ1+dwFEGw793Nz49KOYk6EiGO1Z/fRV
Rc7BV5BRiKsQnqtOZ3gio9fG9YoZ0If0+gs59J3pxtCVX6fg1AM=
=Y6Yp
-----END PGP SIGNATURE-----

"""

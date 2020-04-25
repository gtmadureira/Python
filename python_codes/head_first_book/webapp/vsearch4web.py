"""

-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

"""



from flask import Flask, render_template, request, escape
from vsearch import search4letters
from DBcm import UseDatabase


app = Flask(__name__)


app.config['dbconfig'] = { 'host': '127.0.0.1',
                           'user': 'vsearch',
                           'password': 'vsearchpasswd',
                           'database': 'vsearchlogDB', }


def log_request(req: 'flask_request', res: str) -> None:
    """Log details of the web request and the results."""

    with UseDatabase(app.config['dbconfig']) as cursor:
        vSQL = """insert into log
                  (phrase, letters, ip, browser_string, results)
                  values
                  (%s, %s, %s, %s, %s)"""
        cursor.execute(vSQL, (req.form['phrase'],
                              req.form['letters'],
                              req.remote_addr,
                              req.user_agent.browser,
                              res, ))


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    """Extract the posted data; perform the search; return results."""

    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(search4letters(phrase, letters))
    log_request(request, results)
    return render_template('results.html',
                           the_title=title,
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=results)


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    """Display this webapp's HTML form."""

    return render_template('entry.html',
                           the_title='Welcome to search4letters on the web!')


@app.route('/viewlog')
def view_the_log() -> 'html':
    """Display the contents of the log file as a HTML table."""

    contents = []
    with open('vsearch.log') as log:
        for line in log:
            contents.append([])
            for item in line.split('|'):
                contents[-1].append(escape(item))
    titles = ('Form Data', 'Remote_addr', 'User_agent', 'Results')
    return render_template('viewlog.html',
                           the_title='View Log:',
                           the_row_titles=titles,
                           the_data=contents)


if __name__ == '__main__':
    app.run(debug=True)



"""
-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEE8iavjRZ2/dKhzGiBXQppWFastkFAl6jleAACgkQBXQppWFa
stk2KA/+Lb0UKwxhzmmWTJ1NmYIfIfqRRNhY9FTicGtrbXDZHyEKVhD2ML08npuC
5yNPfmHSxeoc8bS5kimminZFDXsIN4Vh9Obv52c4rX9du2ttzeXrHnqeh6sYLwMc
ze9dMxx0SiZXoQBrx6ohwfnLLsXG9RYsi37rLCLLQKwaNlO6dlAaBK4n4Zc34dIi
xCHP1cNnY8OdP51f/u28cwnWBCKn/bU8NPHPwPbqFAigFxLKmIzlo0TTzXAJovbq
jUL63NdqkrwsAiBQx4mvLGNsBlIIxfrX3lXx69LB7rk4C1mCFFfVTGioEZyjBOVs
u2i1qdGcaKCI+1bngp7kj39LT1qRCqKXGPxxq6TZ+eJSTpu3TcTuFMqJkBbP7dPm
YQnrHn3OR8gVO6wYjo70aZFKEhoOdwMjBxiSYcZWTziq88JfynyQES/qzBashug8
vjgAxwavtVZtVzO2xiUfC7cbqIje1pRnBZ9/9eQIsTO4M5wQajwI9yQiYCjGnEcU
ns+VuLbuFOW3thf7oOjlHlcsb4QBnyRjhxwnx4VJfQ1l1VIJTUgU1BQ4fkQBjOkY
A9A8GeY5JFPvGTA/nXj7EzNaR9V0a19cvJoFesov1wcvLQp5QWg4leJP+UDe4Ok2
NksAgmTYikIw2ubNf+K76RXvByHpHJ64ao4qXfy/a57Q0OYRozU=
=LjH+
-----END PGP SIGNATURE-----

"""

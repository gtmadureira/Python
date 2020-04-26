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
                           'password': 'Vse@rchpasswd86',
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

iQIzBAEBCAAdFiEEE8iavjRZ2/dKhzGiBXQppWFastkFAl6k0PwACgkQBXQppWFa
stkJiRAAjRUTYF3KensOiLsPJrM/B3Sn5Regjom+BdtvVMqkUxf8hmaQxeLnaOzD
OO9rQ6CR4G0vytzoDdbshNSNc7yj8nixZM08UFSnjSkb55L3vIwg2PpmvuZiW+Po
xwdj2Pra92BCpey4aYQUSZ1HFE4gduq2uLhsS9/atjvLzK7JgSTzWnm1X6SkOynx
R5/RF8kfrihNvxg1EH9bPaVrVR5Ny3UxqmvilA7pi1Q0nDZFtS4IG6KHU+Vv4Qfp
W5xSQ1SDy0Gl6Lfgi03xqBYiQKhGx/NSDBI7YPZSEdeHfcola8Jm0c90bIg9IgZ0
CME75WsoAdVPMsgV6ve143HYvMIdQwLtK3R3Nc/KukXhVJGCLmK0dUTy9BlimU5W
KQTD1KZYR2hFLCf2nmw/VcD9rtpC1mxdUjjThhhxRth9nKz30dtUW8vuQSO3Hhdf
RLx+jWQwRgmHCj1cMmlBcSlPyqxDLt49P14E4a8ifbPmNbkaTO9EKw7DxXPvpTbL
NsvWeICvokksT9jgZo2NDyQnsJwuKmAs0eMMACBbv3QPtiC+ElSgu4Wb8c/pj2Yb
ZlBOZRPB+FtRO4NJ6m4kA2RoCTqzVBKxKV3BCuSizVQqTv81wcx7MDD+eI8g7pSs
Fc4fwJ0ErbktXo+SzF7gQgWGaw0XrldA5si1mz5BR6MGHNKVohY=
=Y4w1
-----END PGP SIGNATURE-----

"""

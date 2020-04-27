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

    with UseDatabase(app.config['dbconfig']) as cursor:
        vSQL ="""select id, ts, phrase, letters, ip, browser_string, results
                 from log"""
        cursor.execute(vSQL)
        contents = cursor.fetchall()
    titles = ('ID', 'Datetime', 'Phrase', 'Letters', 'IP Address', 'Web browser', 'Results')
    return render_template('viewlog.html',
                           the_title='View Log:',
                           the_row_titles=titles,
                           the_data=contents)


if __name__ == '__main__':
    app.run(debug=True)



"""
-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEE8iavjRZ2/dKhzGiBXQppWFastkFAl6mJ0wACgkQBXQppWFa
stkMkg//bWVpLmhJmOrcYn/rmgz+EzIF0lgb+6YCbCUbJMDPPPD6eZwUdUFyHfvT
hG71XD8iY+BcPt6hVp2R6eUAgQFOqOuY/z7NmNR2FFxxsVR0djsxNfI5r69+Yud0
VAsIGg7hi4pHSqa+axEQ7rZZOOiUuP2zvIUb/0ShiIZ15fiwTSQ8Z75fch6r5mUz
CS1SKhrhuPMkAKEZN58QfKg5M875q1P+ROwY6gGHCn9imyhyMQHAHxfUi3GbPqJ5
p+FJhZ7zwSE/u2oBKHp/r/7YP05XKls0sZrQKvzduz22r2kvg6qIcxi/kNoQXu9F
q+ODoMwuaLFenkWCrbsTMPRD+c0CB1Y3SOK6Jzpud00cnT58HhdWg96k1kH/gUGj
XBl5eDlcMklDr58xgc0KTGjndlobq9LTXg3FOtd2K080Znj3uTQFXqBlAsWgmzBY
3O9qkSdBevCngZwoCOAByCyPR+fhgelCQ6XlSqxxu3GHYnJVg1xxVrt51FnCFGKl
A/ajv09BhPisOiOVL4Et2fotWuZp093z1lPogR0t8/ISCeQTlVc3U1z4EZ8mUhVC
JvTp4rPVLdHq464JcwRJaa4kFlFrp3d7rO+WdcgNRsG8uSOiOZJZBFz7JM+zm4Ri
NEuBmF3EBymgIA35DZ001ZIyO1PhdkUgMyvyXVZ9d0QaPb8+rT8=
=N+YR
-----END PGP SIGNATURE-----

"""

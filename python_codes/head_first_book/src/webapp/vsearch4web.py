from flask import Flask, render_template, request, session
from vsearch import search4letters
from DBcm import UseDatabase
from checker import check_logged_in

app = Flask(__name__)

app.config['dbconfig'] = {'host': '127.0.0.1',
                          'user': 'vsearch',
                          'password': 'Vse@rchpasswd86',
                          'database': 'vsearchlogDB', }

app.secret_key = 'SecretKeyHere'


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    """Display this webapp's HTML form."""

    return render_template('entry.html',
                           the_title='Welcome to search4letters on the web!')


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    """Extract the posted data; perform the search;
       send posted and serach data to log_request(); return results."""

    title = 'Here are your results:'
    phrase = request.form['phrase']
    letters = request.form['letters']
    results = str(search4letters(phrase, letters))
    log_request(request, results)

    return render_template('results.html',
                           the_title=title,
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=results)


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


@app.route('/viewlog')
@check_logged_in
def view_the_log() -> 'html':
    """Display the contents from database(log table) as a HTML table."""

    with UseDatabase(app.config['dbconfig']) as cursor:

        vSQL = """select id, ts, phrase, letters, ip, browser_string, results
                  from log"""
        cursor.execute(vSQL)

        contents = cursor.fetchall()

    titles = ('ID', 'Datetime', 'Phrase', 'Letters',
              'IP Address', 'Web browser', 'Results')

    return render_template('viewlog.html',
                           the_title='View Log:',
                           the_row_titles=titles,
                           the_data=contents)


@app.route('/login', methods=['POST'])
def do_login() -> 'redirect':
    """Login procedure."""

    with UseDatabase(app.config['dbconfig']) as cursor:

        usr = request.form['user']
        passwd = request.form['password']

        vSQL = """select user, password from users where
                  user=%s and password =%s"""
        cursor.execute(vSQL, (usr, passwd))

        list_contents = cursor.fetchall()

        posted_user = [usr, passwd]
        user_found = []

        for tuple_user in list_contents:
            for item in tuple_user:
                user_found.append(item)

        if user_found == posted_user:
            session['logged_in'] = True
            return view_the_log()
        return render_template('login.html',
                               the_title="""Welcome to search4letters
                                            on the web!""",
                               the_error="Invalid 'User' and/or 'Password'.")


@app.route('/logout')
def do_logout() -> 'redirect':
    """Logout procedure."""

    if 'logged_in' in session:
        session.pop('logged_in')
        return view_the_log()
    return view_the_log()


if __name__ == '__main__':
    app.run(debug=True)

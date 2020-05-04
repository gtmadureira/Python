from flask import Flask, render_template, request, session
from vsearch import search4letters
from DBcm import UseDatabase, ConnectionError
from checker import check_logged_in
from string import capwords


app = Flask(__name__)

app.config['dbconfig'] = {'host': '127.0.0.1',
                          'user': 'vsearch',
                          'password': 'Vse@rchpasswd86',
                          'database': 'vsearchlogDB'}

app.secret_key = 'SecretKeyHere'

# The variables below are for providing argument values
# for the error () function.
t1 = 'Welcome to search4letters on the web!'
t2 = 'Welcome to view log'
e1 = '** System temporarily unavailable. Try later !'
e2 = "Invalid 'User' and/or 'Password'."


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    """Display this webapp's HTML form."""

    return render_template('entry.html',
                           the_title='Welcome to search4letters on the web!')


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    """Extract the posted data; perform the search;
       send posted and searched data to log_request(); return results."""

    title = 'Here are your results:'
    phrase = request.form['phrase']
    letters = request.form['letters']
    results = str(search4letters(phrase, letters))

    try:

        log_request(request, results)

    except ConnectionError as err:

        print('Is your database switched on? Error:', str(err))
        return error('', 'entry', t1, e1)

    except Exception as err:

        print('***** Logging failed with this error:', str(err))
        return error('', 'entry', t1, e1)

    return render_template('results.html',
                           the_title=title,
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=results)


def log_request(req: 'flask_request', res: str) -> None:
    """Record of the log details from web request and the results,
       on the database."""

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

    user = capwords(session.get("USERNAME"))

    try:

        with UseDatabase(app.config['dbconfig']) as cursor:
            vSQL = """select id, ts, phrase, letters, ip, browser_string, results
                      from log"""
            cursor.execute(vSQL)
            contents = cursor.fetchall()

    except ConnectionError as err:

        print('Is your database switched on? Error:', str(err))
        return error(user, 'viewlog', t2, e1)

    except Exception as err:

        print('***** Login failed with this error:', str(err))
        return error(user, 'viewlog', t2, e1)

    titles = ('ID', 'Datetime', 'Phrase', 'Letters',
              'IP Address', 'Web browser', 'Results')

    return render_template('viewlog.html',
                           the_title=t2,
                           the_row_titles=titles,
                           the_user=user,
                           the_data=contents)


def error(user: str, url: str, title: str, error: str) -> 'html':
    """Input/Show erros in the current page."""

    return render_template(url+'.html',
                           the_title=title,
                           the_user=user,
                           the_error=error)


@app.route('/login', methods=['POST'])
def do_login() -> 'redirect':
    """Login procedure."""

    usr = request.form['user']
    passwd = request.form['password']

    try:

        with UseDatabase(app.config['dbconfig']) as cursor:
            vSQL = """select user, password from users where
                      user=%s and password =%s"""
            cursor.execute(vSQL, (usr, passwd))
            list_contents = cursor.fetchall()

    except ConnectionError as err:

        print('Is your database switched on? Error:', str(err))
        return error('', 'login', t2, e1)

    except Exception as err:

        print('***** Login failed with this error:', str(err))
        return error('', 'login', t2, e1)

    posted_user = [usr, passwd]
    user_found = []

    for tuple_user in list_contents:
        for item in tuple_user:
            user_found.append(item)

    if user_found == posted_user:
        session['logged_in'] = True
        session['USERNAME'] = user_found[0]
        return view_the_log()
    return render_template('login.html',
                           the_title=t2,
                           the_error=e2)


@app.route('/logout')
def do_logout() -> 'redirect':
    """Logout procedure."""

    if 'logged_in' in session:
        session.pop('logged_in')
        return view_the_log()
    return view_the_log()


if __name__ == '__main__':
    app.run(debug=True)

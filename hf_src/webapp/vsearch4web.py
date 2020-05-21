from flask import Flask, render_template, request, session
from flask import copy_current_request_context
from threading import Thread
from string import capwords
from typing import Any
from dbcm import UseDatabase
from checker import check_logged_in
from vsearch import search4letters

###############################################################################

app = Flask(__name__)

app.config['dbconfig'] = {'host': '127.0.0.1',
                          'user': 'vsearch',
                          'password': 'Vse@rchpasswd86',
                          'database': 'vsearchlogDB'}

app.secret_key = 'SecretKeyHere'

# The variables below are for providing argument values
# for the error() function.
title_1 = 'Welcome to view log'
error_1 = '** System temporarily unavailable. Try later!'
error_2 = '*** Something went wrong --> '

###############################################################################


@app.route('/')
@app.route('/entry')
def entry_page() -> Any:
    """Display this webapp's HTML form."""

    return render_template('entry.html',
                           the_title='Welcome to search4letters on the web!')


###############################################################################


@app.route('/search4', methods=['POST'])
def do_search() -> Any:
    """Extract the posted data; perform the search;
       send posted and searched data to log_request(); return results."""

    @copy_current_request_context
    def log_request(req: Any, res: str) -> None:
        """Record of the log details from web request and the
           results on database."""

        try:
            with UseDatabase(app.config['dbconfig']) as cursor:
                vSQL = """insert into log
                          (phrase, letters, ip, browser_string, results)
                          values
                          (%s, %s, %s, %s, %s)"""
                cursor.execute(vSQL, (req.form['phrase'],
                                      req.form['letters'],
                                      req.remote_addr,
                                      req.user_agent.browser,
                                      res))

        except Exception as err:
            print()
            print('{}   *** Something went wrong --> {}{}'.format(
                  '\033[1;31m', str(err), '\033[m'))
            print()

    title = 'Here are your results:'
    phrase = request.form['phrase']
    letters = request.form['letters']
    results = str(search4letters(phrase, letters))

    try:
        tr = Thread(target=log_request, args=(request, results))
        tr.start()

    except Exception as err:
        print()
        print('{}   *** Something went wrong --> {}{}'.format(
              '\033[1;31m', str(err), '\033[m'))
        print()

    return render_template('results.html',
                           the_title=title,
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=results)


###############################################################################


@app.route('/viewlog')
@check_logged_in
def view_the_log() -> Any:
    """Display the contents from database(log table) as a HTML table."""

    user = capwords(session.get("USERNAME"))

    try:
        with UseDatabase(app.config['dbconfig']) as cursor:
            vSQL = """select id, ts, phrase, letters, ip, browser_string,
                      results from log"""
            cursor.execute(vSQL)
            contents = cursor.fetchall()
            titles = ('ID', 'Datetime', 'Phrase', 'Letters',
                      'IP Address', 'Web browser', 'Results')
            return render_template('viewlog.html',
                                   the_title='Welcome to view log',
                                   the_row_titles=titles,
                                   the_user=user,
                                   the_data=contents)

    except Exception as err:
        print()
        print('{}   *** Something went wrong --> {}{}'.format(
              '\033[1;31m', str(err), '\033[m'))
        print()
        return error(user, 'viewlog', title_1, error_2, str(err))


###############################################################################


def error(user: str, url: str, title: str,
          error: str, error_exc: str) -> Any:
    """Input/Show errors in the current page."""

    return render_template(url+'.html',
                           the_title=title,
                           the_user=user,
                           the_error=error,
                           the_error_exc=error_exc)


###############################################################################


@app.route('/login', methods=['POST'])
def do_login() -> Any:
    """Login procedure."""

    try:
        usr = request.form['user']
        passwd = request.form['password']
        with UseDatabase(app.config['dbconfig']) as cursor:
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
            session['USERNAME'] = user_found[0]
            return view_the_log()
        return render_template('login.html',
                               the_title='Welcome to view log',
                               the_user=usr,
                               the_password=passwd,
                               the_error="Invalid 'User' and/or 'Password'.")

    except Exception as err:
        print()
        print('{}   *** Something went wrong --> {}{}'.format(
              '\033[1;31m', str(err), '\033[m'))
        print()
        return error('', 'login', title_1, error_1, '')


###############################################################################


@app.route('/logout')
def do_logout() -> Any:
    """Logout procedure."""

    if 'logged_in' in session:
        session.pop('logged_in')
        return view_the_log()
    return view_the_log()


###############################################################################


if __name__ == '__main__':
    app.run(debug=True)

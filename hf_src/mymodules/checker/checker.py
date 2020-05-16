from typing import Any
from flask import session, render_template
from functools import wraps


def check_logged_in(func):
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        if 'logged_in' in session:
            return func(*args, **kwargs)
        return render_template('login.html',
                               the_title='Welcome to view log')

    return wrapper

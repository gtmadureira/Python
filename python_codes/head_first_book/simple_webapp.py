"""

-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

"""



from flask import Flask, session


app = Flask(__name__)


@app.route('/login')
def do_login() -> str:
    session['logged_in'] = True
    return 'You are now logged in.'


@app.route('/logout')
def do_logout() -> str:
    if 'logged_in' in session:
        session.pop('logged_in')
        return 'You are now logged out.'
    return 'You are currently logged out.'


@app.route('/status')
def check_status() -> str:
    if 'logged_in' in session:
        return 'You are currently logged in.'
    return 'You are NOT logged in.'


@app.route('/')
def hello() -> str:
    return 'Hello from the simple webapp.'


@app.route('/page1')
def page1() -> str:
    return 'This is page 1.'


@app.route('/page2')
def page2() -> str:
    return 'This is page 2.'


@app.route('/page3')
def page3() -> str:
    return 'This is page 3.'


app.secret_key = '123456'


if __name__ ==  '__main__':
    app.run(debug=True)



"""
-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEE8iavjRZ2/dKhzGiBXQppWFastkFAl6nbq8ACgkQBXQppWFa
stlc/A/8CBQucHsvR1mK5jqgUBoX3Tsu72CWnULyVH9nC4AFgClXoh7Th/tTIBRP
qhPttkxZa6px9507ySCgBqH4ela+VygJIzWgJlm+0+J6y2YX8dL6Zho8n9s2aT4q
Z8i6tQJMvxUE2DcWUpv2qeU3czRMbE8CAkqhtQHr9RUr67Zo+yJkQGM2ZgJwd68R
wSEtS5pqy7dPtFe3YZoFRaJeD07wFzCVNvjr9uP6IgYOkUSij3bweFIthWNCW8i8
QYck3h3QBLBu3m1L0toAG6GcYqvr9T56mAfOShuxvKCLTQAOCd6vfvvsdgMDiN9G
DMQBI4riicXUPjm8EdxwFsMWAq6fN4r+Uw8enZj30SY0Sy5Y17UIA1/aLGrZIMfA
LkxNpEj5klcb/0pvTXX3tjgRBCM8Q7OAb5MUegwLGpXqJfdnRwdkFHPj8pjNZXp8
MCS6sZoT+E9fcFTkck459Un8X7kb70w4J0MuMU4Rxzgm/+Ydfm13bcTO7tXmYCYP
KxTSCqh01WqahF5rnFZzV0Wy3jgPR/qLc0ReGNvEEaxkNmAhjTxE4ZG/OIC7y1BB
7oa3koc+RbRwBrvrefwjz9QSqMuYo0GFW6lkJih53/0/kKc37+BC48Ut1Zhg1ZVy
VJd8LumN4usPk0sxegsKuyMwf2J78gMwCaHFgQZAFDAhnxaZJrc=
=gCDC
-----END PGP SIGNATURE-----

"""

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
        print(req.form, req.remote_addr, req.user_agent, res,
              file=log, sep='|')


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

iQIzBAEBCAAdFiEEE8iavjRZ2/dKhzGiBXQppWFastkFAl6fmaoACgkQBXQppWFa
stm57Q/+JnmZHP2PYJfiDxQsTBdtPWUXz0LX3QjPXOMUPZiIDAnTx9Il2MaYzwef
rv0By2EM5skhGGQ3Tpv3aRGZcSdNxN6dIb8VmBVMWDrAbmNFL6Bnn/N08kSxcUV5
XkhBF7YgiBJjOyv2B0mREIxVnt9YmBVq/Br8COfBpHSv9FZ2EFIChr40kSa++2Zk
uvNQt2W/Q3Cv5v4csWBTHmHqpdgzpgWr9m88sw8lCHheg0hPoc37Ep9tg2kiZsaN
9vKkriVoiHpBGdUpFkIwzhrIa+7g3vJlTVrSFmIhnPGPtYOzKqXP9vVOOJHBWZ8l
ObAVKWKsxQH+47x1JSAuqIdKTR14TqdQORZwSAh87lr+2dD0tkFv3N1FVSRlZEgf
h0iLm/QGEb9V39hQFv7M1+xFnURI9XBbss6b/SaHFpu/aBWYvrXYq61qDPxBrHM/
VTavqYzlCTZXjjmVB0nLl3+MsRDJBhH9WEPfr1nC6rP1y9kEe00y7dOb8CaoRiM0
j1hMKLvhChpUnGcZ3LLVcSKckkohR1lOsL2k7KfCl4kyAqIh3+eCns8Ixy6JjnF7
xjNWLdRMB1gtVJGJ8rnrbPfkcXmdr8a37EZBMdF3FBLuxW6nzbE+mo5mo9vvn5/G
LKYsKfx4GmJ7cRV0GzhxibCqmnknQON6NYHl6fCoXTRTCmDEil4=
=FBkE
-----END PGP SIGNATURE-----

"""

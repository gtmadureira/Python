"""

-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

"""



from flask import Flask, session

app = Flask(__name__)

app.secret_key = '123456'

@app.route('/setuser/<user>')
def setuser(user: str) -> str:
    session['user'] = user
    return 'User value set to: ' + session['user']

@app.route('/getuser')
def getuser() -> str:
    return 'User value is currently set to: ' + session['user']

if __name__ == '__main__':
    app.run(debug=True)



"""
-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEE8iavjRZ2/dKhzGiBXQppWFastkFAl6nW6QACgkQBXQppWFa
stm4nA//c3wPeuunYF7iPuNv2Jbl5YXXNWFfSiC23hxJdj5HIyWr/+tJQ+UwZc4/
n0aBHxg/30XaD64VwIfKi/GLKmSIW5dfSmxVCxwEzUh84NiTnkRIKhO6ZGjfqqdy
fpMd0YD8ZZM92x8fR1oXdiiPz0ImxHjdLcHp+DhbqSIyxOnxax+hItLHu9KV3USQ
CmAzMH3scunqcW3SNz2UjcWa7W41P4SvWfJTIT1WywKbiIrq5BOvo/F79hY1P2ah
S97jW5QZfHov3L1nH+B8qYMZP7t1qLN0WiwHOtjTT9g91VwZHPK1/7VQ6KJs733G
LK+dId/wQKnltpw4jjW2SYbV45txVFzFRms7Est+kEdDAVg0AR95GTiBqITCIm+V
YgmszVR5kgZThfn6gLH+ryQ4oSZageYp5LtTHb7aODGknfqSIG8NcZfB12EMWlC1
o/5E0tnGDSPrswvc8byZX2L1bDhkRSYZB66xggRc45hwBQH+L9hggb35IdTnxlTf
C19hJU8u9DCLiZymdHgYoyDlqtny9c0RobnnRi2csgcO9khg/XqdGrMEuTdFVZeq
KVl3Q0ThThAbclJKq5MShcNe9BIpvbbYU/BKxB81OX3V5llnMLTX1dCYEyfADdjr
pRJMRiNSucjd5mayJzO1/RzbhlLTxTpcJ86ZFIUkHe92WPkKe3A=
=LAV2
-----END PGP SIGNATURE-----

"""

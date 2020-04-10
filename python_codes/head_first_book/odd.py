'''

-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

'''



from datetime import datetime

odds = [ 1,  3,  5,  7,  9, 11, 13, 15, 17, 19,
    21, 23, 25, 27, 29, 31, 33, 35, 37, 39,
    41, 43, 45, 47, 49, 51, 53, 55, 57, 59 ]

right_this_minute = datetime.today().minute

if right_this_minute in odds:
  print("This minute seems a little odd.")
else:
  print("Not an odd minute.")



'''
-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEE8iavjRZ2/dKhzGiBXQppWFastkFAl6Gv1IACgkQBXQppWFa
stlxBA/9F/f6KD/gYJADvPfCdiaxSEbsaw3ijYwmFnnq+d11pyMLn2LAWibu9P2I
QzcoZQzWZJl0dLYWHVsqUv6VOhRwR78fD3J16kq1oO5amlNazdPhhtHr3nMKH1VX
AWoUcRA5Nwr6cC71txU1+mjc2TcH4fuos+DQLvdG3Pd8jwhN3+il4F+EpOtEvaHF
AIlDMXkGRIYGRu5tZCNQLFKDnt7uAKucPat7kt5/ZBbeNXYfwiyaBRhcmLwPi3h+
uAoG1GqzxBJO98yiDYLaNHviE0Yj8b4GgGzxVSXZoiktdOAORhTKQPDslolt/7a2
smaRZk1IX3zSuSe0AEWWXPikrfwSF6/nN4ybNdpBHk7L4ZnMDQgcH0dmK/df/XzR
Uep4uRGX2pazxurYrK7CTzvPYG8wxe2HopP2b9jmxtKoS1cCzOa3Bgj6V0E6szvi
Xkj9pI7sdUyuioecWtHynYO/wmw/cx4/CoPceXMJKnTv2tZn393urX4QzxPfu58p
3rXRBP2MyHqkHDKpWoHCnOS4JaNyuap3wrUH39OV5dYxetJfmFi7fTdel0gSoNQ3
PfuO84cTf0VRNZ8Gt1NysmAP4McRCCnLZYzKDM2Mzcaj+MA2dcj+7NZoy6fpfqMi
cX8ZaKncBL/z0XrAS+ArWCKWviBXMiUzTRrEL7Tbqvnms7gGtQA=
=TJ8Z
-----END PGP SIGNATURE-----

'''

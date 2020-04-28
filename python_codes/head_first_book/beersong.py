"""

-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

"""



word = 'bottles'

for beer_num in range(99, 0, -1):

    print(beer_num, word, 'of beer on the wall.')
    print(beer_num, word, 'of beer.')
    print('Take one down.')
    print('Pass it around')

    if beer_num == 1:

        print('No more bottles of beer on the wall.')

    else:

        new_num = beer_num - 1

        if new_num == 1:

            word = 'bottle'

        print(new_num, word, 'of beer on the wall.')

    print()



"""
-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEE8iavjRZ2/dKhzGiBXQppWFastkFAl6ns9sACgkQBXQppWFa
stkQOQ/9EOss4dMATrWxwE1w5ijBgdyjUDyCQeBk3kHohAPIPRrRn4WmgxizENeQ
1wA1Z6xknFYadvAE1KCiRmq6590PsN0hvFUhJTz1APOTma6O7axh6rM7ZyX1f3CX
ffS+UrT1c/iGohumS24Luaoa3LhfuPCinTNP2KVe9LnHrQoN7SNXsHcSzNxUVuti
XDRnIqPdCrcPBsZnrJ3Z0OZ3sh/xhWrQu5pTxpWLsrS8CuIwYe8l4MFN8UpYbb0q
fSirO9jQqiIAAnq1jrBYzKh3zk98F24JHO+m9Wpod86LRXmeL0+hhGgMW37Mxrxe
ryH4yu8A584AHVtjzXpVF1VINjYooLZvB/QzULogM7nevM9WgKyho0g+qPh3UcQr
D3TGucCQKC0hMkbgly+QPvXU78ZlDq3NW0JsL5Ku2GXAfaCTyxL7w2JTFeq0HcBJ
AaOxrrYE7Z0JTGwC+cxrhkk5LPddUv6MYn2YYpKZLp+0tdpfBYZcXuC7Kl9nIYEx
x0fY5d4WT6YOIo+YMBUhmS+3YJqejB+wUwiI6rWpo55m31aIl0rZ0bDGmugPM5ql
77ZYWR/6lAgQWhY2XfC+u3yZ6T4c2kX99tVshqp7bLkIzDmKoPEE1sGJ+Ce0cG4u
zuMLl5HoBfmu1ntUJjRfrg69TdqrJPgJgRcZHv1S2UifsysjmZI=
=BVE5
-----END PGP SIGNATURE-----

"""

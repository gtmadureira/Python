'''

-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

'''



word = 'bottles'

for beer_num in range(99, 0, -1):

    print(beer_num, word, 'of beer on the wall.')
    print(beer_num, word, 'of beer.')
    print('Take one down.')
    print('Pass it around')

    if beer_num == 1:

        print('No more bottles of beer on the wall.')

    else:

        new_num = beer_num -1

        if new_num == 1:

            word = 'bottle'

        print(new_num, word, 'of beer on the wall.')

    print()



'''
-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEE8iavjRZ2/dKhzGiBXQppWFastkFAl6KM1AACgkQBXQppWFa
stmqWRAAhmlbftJvhcchofDjIpTk6Dj/34Pi+6nLRtVr7KAZiQZJHrJBY4LwFsso
9gVsnr/XnQCRgMYM9PXbWz5dFIKi27+StKC9hO5h+XbID/DE8rRloc3uV07MFM4+
yibaQKfq9No6Z3W26uivNLxgjDBRvVnGoz9gx9j2zBtNgXU1NB/bpbF2TMN/lMHC
oPGrexkKIAkck9pcg9VlPiiGmqZm31f8pSE2m61p69aVjGWz10tvbzgxvU7c7i80
lVYzlIaLkwbo7KJOaXPqvIKwRGBpuUWBaoADB0Ri2o6aW7u0VZo1pNl/UEf5XbqG
WubHX4Yyu6vjUto+dIwc7BdhFf+8N/VwFWgp84doLaQ+jYnr3Zd5LRehyU30tr/1
EJmPy+CePnZFqy6Xhi6ZIeVG4i7H3AFmOHMTAp4IxMbnzqlZRlN0mccgVknYm5X/
v6rtPezXBuQD4buM7wdkbURkLuyXvNOun2uxQOHTTaU86lxADbvnWMUkzBgifN0b
SVe7WB1Jx4n3yXXajIJ63HkX/wg1xqfwxVNGsk079SzOsPAAUJOdxR7hvLIio+Lj
OjOH/HlOM5VLhvVB+WUI/Q3uyZmgRmQqgR6U0dBhVembLj8E90lQOMo3UNLk357/
R46MtglR9Qx+7tE3bdICEgYJPUKCL4cDdLT3EyyuA9Trzu8YdAA=
=QAVy
-----END PGP SIGNATURE-----

'''

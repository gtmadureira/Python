'''

-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

'''



vowels = ['a', 'e', 'i', 'o', 'u']
word = input('Provide a word to search for vowels: ')
found = {}

for letter in word:

  if letter in vowels:

    found[letter] += 1

for k, v in sorted(found.items()):

  print(k, 'was found', v, 'times(s)')



'''
-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEE8iavjRZ2/dKhzGiBXQppWFastkFAl6RYU8ACgkQBXQppWFa
stmvdg/8CUk6ZV+U3KlLt+PzPTS6ZdrNPpon5304/XLxee6XDPvXJCu9vtxm9Vjc
vAJeBOiztu+l+SLZvG0pdZPTvx38v1ysqbMhVg48MAMe+XJdJYEvDYK8jnxoeWkR
3BEGnmT5MzmtOJfHN5/mKLVMrNpEGRLNar/H1S/4829YSFczJSVlmybVmdMDYtwk
7FHaqIPDhf/+mtWwYLp8gVVPgbg+DKU3u1h7Jbhl3i8sUUNEp16Uj3WmA+1eILuh
e3o7GTAOHNNJ9Kn4kxRnnp5XHz2rCuf4RAEJgqRh6zuoOjGCHRcssPYC7nEdox5i
ABabrJJN43t+x8/YlJu90R6f5HiGsCwkuhAEv5Kggo2778oVpLPGzjvoe0kSg8cI
zU/Et2lgrTltay3kzxSaaZcy+UWE6HoOE/giBUuJztp+mQjJznY4+5SZXRgF8DuX
87ekZy/gLkATGtho+TfxRv4e76OhIpmR3EMeGSi9xAIw5hxuhoLH9iFhDwPcGSbj
dCj/jnnc7pYHcPfoHEdUJlqZrOAs1XAyIkb29pcoaX7yh1Xyod3Y0MeWGWwELPzm
vFJaloxD4SAe3MzBjqHYlOLEz1lqbZI5Wi1dLLSPKh+1SuE5CLP6KZZEhBF++jJ+
8iAbm6FsKXvW/MKUniI8pplekIB9VEc4ttA9ZbxzkC6KBtx6/Kc=
=c9WS
-----END PGP SIGNATURE-----

'''

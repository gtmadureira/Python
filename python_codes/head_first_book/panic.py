'''

-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

'''



phrase = "Don't panic!"
plist = list(phrase)

print(phrase)
print(plist)

for i in range(4):

  plist.pop()

plist.pop(0)
plist.remove("'")
plist.extend([plist.pop(), plist.pop()])
plist.insert(2, plist.pop(3))

new_phrase = ''.join(plist)

print(plist)
print(new_phrase)



'''
-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEE8iavjRZ2/dKhzGiBXQppWFastkFAl6L+z8ACgkQBXQppWFa
stngqg/+MwxVjrL6uAjAOg2vuZVOu19+xIHQCRcXu67OyQwAqTbqVS7D6aL7EImA
sm+49Qw5a/I5P0RNZKvDtoV8lPW7IWP1VRajrOdLlpulaabJKe5OT0TKkqDX5Nwg
hOZrjwFveSMIAqGYgoHjHYzLPnAmRBP2DBYr6KyiDmlWdUVzOzp5NFAgIhs61T2T
JDXyxXEXMI6UZ9QHRwtu28O4dGBnOwZBgvAPGclsrfWZInrULEw/4j0F1yVSp004
uXSQV+QM/0uGGFJl4wbS7q0B4cCsh3Y2lBtqJyyn3YtaSkaLFWpx+Ao4KMhF+dvZ
9jRN2tMqiNoq69ei4RJ/A4e0zOkMYlZrmjaequmPrDp7C5CaDfXeyJ10gtFINUaa
kjknSNej2+nOCo+F87QQZKVlBgiHbCU+9qe0mipcGmvBlIwx5e8Dc4y0L7YtsM5F
RjndxmliXTem4X0XxORLxG5s7Kq7nifY9HfiFEPWAq+duNostXGbKmG5urWISxS2
pCUK0p3d5DTJJ1zVOwMo1G9RL8qjhRg8doHgnVVu9orJKATdJbZh7KyCBWdTGZLd
4DUCZvAEVkyiGGsxHgMWQN+FNcbD9bWa8TdpVSt0pAJCtlJkVw5ODIA1cmU/CTcP
iqPYfwfN6iK8GEd8H3dHrDN2Jj7fBqRvg/CN02nZfVlxo3C3ILQ=
=BY43
-----END PGP SIGNATURE-----

'''

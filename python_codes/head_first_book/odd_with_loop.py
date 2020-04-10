'''

-----BEGIN PGP SIGNED MESSAGE-----
Hash: SHA256

'''



from datetime import datetime
import random
import time

odds = [ 1,  3,  5,  7,  9, 11, 13, 15, 17, 19,
        21, 23, 25, 27, 29, 31, 33, 35, 37, 39,
        41, 43, 45, 47, 49, 51, 53, 55, 57, 59 ]

wait_time = 0

for i in range(5):

  right_this_minute = datetime.today().minute

  if right_this_minute in odds:

    print('This minute seems a little odd. --> ',wait_time,' expected second(s)')

  else:

    print('Not an odd minute. --> ',wait_time,' expected second(s) ')

  wait_time = random.randint(1,60)

  if i == 4:

    print('Good Bye !')

  else:

    time.sleep(wait_time)



'''
-----BEGIN PGP SIGNATURE-----

iQIzBAEBCAAdFiEEE8iavjRZ2/dKhzGiBXQppWFastkFAl6JRiMACgkQBXQppWFa
stnQQhAAoU3uj43eBUJeooblXymZ7hCFYD7LDryTssIaZfcg0FaabcCuB6zMGVmX
w6vKAVtEewu6hpLAvRefFdsd1RxkEf1ufADC0XsXoG+2nJzJOCaQniutgEM4/iEy
VfcbWytp9U89I1JxCxlDRuEswZu8Zjw9/ejHzFxa95RG4tNRp+OpXM7XMNCtBZhc
b/u7aw3VoL5KMu885iJzBfZjw3rXwYbHftBJ0/9LlFlF8GaXlH3TKceYlp5U8rIw
LeU5GeOBLkFKbyl8M3Um059/emOlpMM7z055ywmUjuQOPljmCnCRp852wGaBzuCM
S5iNX+ObD88EZX+MEGCAdoCdpSF4gOcT0kvFSKIz+Rp+ykcSmfjVksBCmCrE3OXB
dpfNcxH4uxLwR33WPO3hpE5qNAxhOz1C7nkjYYwlLVTQHf7eBA8TpjQrT7GBIS39
l6RPWRDxW+oWoPKQWgnWsQpYsho26k9Pnoh4z1Cc6gWc9cz9xz87V/mERVqmzlTm
vb2K6AB5cZj9jbviIJKkvXAi8KXO7WlCeufrevTk1vv4m69XV6VbvrITU8+SmaI3
8BHlWuy6Yp9PKiO7z+VEUufqyYhOjkoqpc23xeIhjrhfq5ha99mxN9MsxrDXts6D
GvBH9oqqSBE87TF2GU77pVZFMRXtbP2FXaB+yb+w7j5utw/W+EM=
=3RMK
-----END PGP SIGNATURE-----

'''

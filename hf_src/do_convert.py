from datetime import datetime
from pprint import pprint


def convert2ampm(time24: str) -> str:
    return datetime.strptime(time24, '%H:%M').strftime('%I:%M%p')


with open('buzzers.csv') as data:
    ignore = data.readline()
    flights = {}
    for line in data:
        k, v = line.strip().split(',')
        flights[k] = v


print()
pprint(flights)
"""
{'09:35': 'FREEPORT',
 '09:55': 'WEST END',
 '10:45': 'TREASURE CAY',
 '11:45': 'ROCK SOUND',
 '12:00': 'TREASURE CAY',
 '17:00': 'FREEPORT',
 '17:55': 'ROCK SOUND',
 '19:00': 'WEST END'}
 """

print()


fts = {convert2ampm(k): v.title() for k, v in flights.items()}

pprint(fts)
"""
{'05:00PM': 'Freeport',
 '05:55PM': 'Rock Sound',
 '07:00PM': 'West End',
 '09:35AM': 'Freeport',
 '09:55AM': 'West End',
 '10:45AM': 'Treasure Cay',
 '11:45AM': 'Rock Sound',
 '12:00PM': 'Treasure Cay'}
"""

print()


when = {dest: [k for k, v in fts.items() if v == dest]
        for dest in set(fts.values())}

pprint(when)
"""
{'Freeport': ['09:35AM', '05:00PM'],
 'Rock Sound': ['11:45AM', '05:55PM'],
 'Treasure Cay': ['10:45AM', '12:00PM'],
 'West End': ['09:55AM', '07:00PM']}
"""

print()

import json

f = open('data.json', 'r')

info = json.loads(f.read())

type(info)

print("Number of Presidents", len(info))

for item in info:
    print("\r")
    print('Name:', item['nm'])
    print('Party:', item['pp'])
    print('Years:', item['tm'])
import json

myRecord = json.load(open('summary.json'))
print(myRecord)

myRecord['kcalories'] = 1200.0

j = json.dumps(myRecord)
with open('summary.json', 'w') as f:
    f.write(j)
    f.close()
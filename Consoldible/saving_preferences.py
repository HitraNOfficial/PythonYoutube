import json

myRecord = json.load(open('shared_preferences.json'))
print(myRecord)

myRecord['currentPage'] = 70

j = json.dumps(myRecord)
with open('shared_preferences.json', 'w') as f:
    f.write(j)
    f.close()
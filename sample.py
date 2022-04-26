from Massey_and_Colley.Massey_and_Colley import Massey, Colley
import json

with open('data/sample.json','r') as f:
    data = json.load(f)

massey = Massey(data)
colley = Colley(data)

key = massey.keys
massey.get_rating()
colley.get_rating()

print('----------RESULT-------------')
print('=======Massey=========')
for e in list(zip(*[massey.keys,massey.get_rating()])):
    print(e)
print('=======Colley=========')
for e in list(zip(*[colley.keys,colley.get_rating()])):
    print(e)
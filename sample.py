from Massey_and_Colley.Massey_and_Colley import Massey, Colley
import json

with open('data/rlcs10.json','r') as f:
    data = json.load(f)

massey = Massey(data)
colley = Colley(data)

key = massey.keys
#massey.get_rating()
#massey.get_defensive_and_offensive_rating()
#colley.get_rating()
print("=======COLLEY'S MODEL=========")
print("vec_b",colley.vector_b)
print("mat_c",colley.matrix)

print('----------RESULT-------------')
print('=======Massey=========')
d,f = massey.get_defensive_and_offensive_rating()
for e in list(zip(*[massey.keys,massey.get_rating(),d,f])):
    print(e)
print('=======Colley=========')
for e in list(zip(*[colley.keys,colley.get_rating()])):
    print(e)


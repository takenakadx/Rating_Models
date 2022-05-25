from itertools import combinations
import tqdm

data = {}
res = ["movieA,movieB,score,userid"]
with open('movie_data.csv','r') as f:
    for d in [e.split(',') for e in f.read().split("\n")]:
        user_id = int(d[0])
        movie_id = d[1]
        rate = d[2]
        if not user_id in data:
            data[user_id] = []
        data[user_id].append(d[1] + "," + d[2])

for user_id in tqdm.tqdm(data):
    for match in combinations(data[user_id],2):
        movieA,scoreA = match[0].split(",")
        movieB,scoreB = match[1].split(",")
        res.append('{0},{1},{2},{3}'.format(movieA,movieB,f"{scoreA}-{scoreB}",user_id))

with open('movie_data_converted.csv','w') as f:
    f.write('\n'.join(res))
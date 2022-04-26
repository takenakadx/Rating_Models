import pandas
import json
import argparse
import os
import traceback

def input_data(data,teamA,teamB,point):
    if not teamA in data:
        data[teamA] = {}
    if not teamB in data[teamA]:
        data[teamA][teamB] = []
    data[teamA][teamB].append(point)

def input_match_to_data(data,teamA,teamB,point):
    pointA = point
    pointB = "-".join(point.split("-")[::-1])
    input_data(data,teamA,teamB,pointA)
    input_data(data,teamB,teamA,pointB)

def load_match_csv(filename,header=None):
    try:
        df = pandas.read_csv(filename,header=header)
        data = {}
    except FileNotFoundError:
        print(f'There is no such file "{filename}"')
        return
    for i,r in df.iterrows():
        input_match_to_data(data,r['teamA'],r['teamB'],r['score'])
    with open(os.path.splitext(filename)[0]+'.json','w') as f:
        json.dump(data,f,indent=4)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="""
        使い方 : 
            python data_convert -f <file name.csv> --header(optional) 0
    """)
    parser.add_argument('-f',help='file name (relative path)')
    parser.add_argument('-hd','--header',help='optional : if csv has header, select the line',type=int,default=None)
    args = parser.parse_args()
    try:
        load_match_csv(args.f,header=args.header)
    except AttributeError:
        traceback.print_exc()
        print('specify the filename \n Usage : python data_convert -f <filename> --header(optional) 0')
# Rating_Models

# 必要ライブラリ
- numpy
- argparse
- pandas

# MasseyとColleyの方法
## 使い方
次のような形式のデータを作成する

``data.csv``
```
teamA,teamB,score
AAA,BBB,4-1
AAA,CCC,3-2
```

これをdata_convertで変換する

``` shell
python data_convert.py -f data.csv
```

同じディレクトリにdata.jsonが生成されるので、これを使って次のようなプログラムを作成する

``` python
from Massey_andColley import Massey, Colley
import json

with open('data.json',r) as f:
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
```

以上
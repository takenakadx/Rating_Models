# やるべき事
# - get_defensive_and_offensive_rating関数の実装
# - 映画のcsvからjsonに変換するプログラムの作成
# - 修正が正しいか確認
import numpy as np
import json

def is_win(vec):
    return 0 if vec[0] < vec[1] else 1

def is_lose(vec):
    return 0 if vec[0] > vec[1] else 1 

class Massey:
    def __init__(self,scores):
        self.scores = scores
        self.keys = list(scores.keys())
        self.matrix_size = len(self.keys)
        self.matrix_m = np.zeros((self.matrix_size,self.matrix_size))
        self.matrix_t = self.matrix_m.copy()
        self.matrix_p = self.matrix_m.copy()
        self.vector_f = np.array([0 for i in self.keys])
        self.vector_a = np.array([0 for i in self.keys])
        for i,key1 in enumerate(self.keys):
            match_len = 0
            for j,key2 in enumerate(self.keys):
                try:
                    for score in self.scores[key1][key2]:
                        score_array = np.array(list(map(int,score.split('-'))))
                        self.vector_f[i] += score_array[0]
                        self.vector_a[i] += score_array[1]
                except KeyError:
                    pass
                self.matrix_p[i][j] = len(self.scores[key1][key2]) if key2 in self.scores[key1] else 0
                match_len += self.matrix_p[i][j]
            self.matrix_t[i][i] = match_len
        self.vector_p = self.vector_f - self.vector_a
        self.matrix_m = self.matrix_t - self.matrix_p

    def get_rating(self):
        mat = self.matrix_m.copy()
        p = self.vector_p.copy()
        for i in range(len(mat[0])):
            mat[0][i] = 1
        p[0] = 0
        return np.linalg.inv(mat)@p

    def get_defensive_and_offensive_rating(self):
        r = self.get_rating()
        d = np.linalg.inv(self.matrix_t+self.matrix_p)@(self.matrix_t@r - self.vector_f)
        o = r - d
        return d,o

class Colley:
    def __init__(self,scores):
        DOT_ARRAY = np.array([1,-1])
        self.scores = scores
        self.keys = list(scores.keys())
        self.matrix_size = len(self.keys)
        self.matrix = np.zeros((self.matrix_size,self.matrix_size))
        self.vector_b = np.array([0 for i in self.keys])
        for i,key1 in enumerate(self.keys):
            match_len = 0
            lose_len = 0
            win_len = 0
            for j,key2 in enumerate(self.keys):
                try:
                    for score in self.scores[key1][key2]:
                        score_vec = list(map(int,score.split("-")))
                        lose_len += is_lose(score_vec)
                        win_len += is_win(score_vec)
                except KeyError:
                    pass
                self.matrix[i][j] = - len(self.scores[key1][key2]) if key2 in self.scores[key1] else 0
                match_len -= self.matrix[i][j]
            self.matrix[i][i] = match_len + 2
            self.vector_b[i] = 1 + (win_len - lose_len)/2

    def get_rating(self):
        mat = self.matrix.copy()
        b = self.vector_b.copy()
        return np.linalg.inv(mat)@b

if __name__=='__main__':
    """
    with open('football.json','r') as f:
        data = json.load(f)
        massey = Massey(data)
    rating = massey.get_rating()
    print(rating)
    """
    #"""
    with open('rlcs10.json','r') as f:
        data = json.load(f)
        massey = Massey(data)
        colley = Colley(data)
    print(massey.vector_a)
    print(massey.vector_f)
    print(massey.vector_p)
    rating = list(zip(*[massey.keys,massey.get_rating()]))
    [print(e) for e in rating]
    defence,offence = massey.get_defensive_and_offensive_rating()
    print(defence)
    print(offence)
    #"""
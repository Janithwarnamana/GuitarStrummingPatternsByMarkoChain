import pandas as pd

from markovchain import MarkovChain

data = pd.read_excel('ss.xls')

st = ['D', '&', 'v', '^', 'v^', '^v', '&^', '&v']
n = len(st)
array2d = [[0 for i in range(n)]] * n
rowLen = len(data.index)
strum_positions = 4


def preprocess(_data):
    arr = [[0 for i in range(strum_positions)] for j in range(rowLen)]
    for i, row in _data.iterrows():
        row_ = row[:-2]
        for j, val in enumerate(row_):
            arr[i][j] = st.index(val)
    return arr


def transition_probability_matrix(_data):
    _tp_matrix = [[0] * n for _ in range(n)]
    for transitions in _data:
        for (i, j) in zip(transitions, transitions[1:]):
            _tp_matrix[i][j] += 1

    # convert to probabilities:
    for row in _tp_matrix:
        s = sum(row)
        if s > 0:
            row[:] = [f / s for f in row]
    return _tp_matrix


def emission_probability_matrix(_data):
    _ep_matrix = [[0 for i in range(strum_positions)] for j in range(rowLen)]
    for strums in _data:
        for j, pos in enumerate(strums):
            _ep_matrix[pos][j] += 1

    # 2d matrix transpose
    trans_tuple = [*zip(*_ep_matrix)]

    trans_matrix = [[*row] for row in trans_tuple]
    # convert to probabilities:
    for row in trans_matrix:
        s = sum(row)
        if s > 0:
            row[:] = [f / s for f in row]

    return [[*row] for row in [*zip(*trans_matrix)]]


print(preprocess(data))

tp_matrix = transition_probability_matrix(preprocess(data))
tp_matrix_df = pd.DataFrame(tp_matrix)
print(tp_matrix_df)
#
# ep_matrix = emission_probability_matrix(preprocess(data))
# ep_matrix_df = pd.DataFrame(ep_matrix)
# print(ep_matrix_df)
frame, path = MarkovChain.generate_markov_chain(tp_matrix, 4)

print(pd.DataFrame(frame))
print(pd.DataFrame(path))


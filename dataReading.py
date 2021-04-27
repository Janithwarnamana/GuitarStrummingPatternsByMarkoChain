import pandas as pd

from markovchain import MarkovChain

data = pd.read_excel('ss2.xls')

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
prob, path = MarkovChain.generate_markov_chain(tp_matrix, 4)

print(pd.DataFrame(prob))
print(pd.DataFrame(path))


def matrix_transpose_inverse(list_):
    list_ = [[*row] for row in [*zip(*list_)]]
    list2 = [[0 for _ in range(len(list_[0]))] for j in range(len(list_))]
    for i, _ in enumerate(list_):
        list2[len(list_) - i - 1] = list_[i]
    return list2


def backtrack(_prob, _path):
    backtrack_path = [-1, -1, -1, -1]
    inverse_path = matrix_transpose_inverse(path)
    transpose_tp = matrix_transpose_inverse(prob)
    max1 = 0
    # find maximum likelihood path end
    for x, val in enumerate(transpose_tp[0]):
        if val > max1:
            max1 = val
            backtrack_path[3] = x
    remaining_path_length = len(backtrack_path) - 1

    # backtracking
    for x in range(remaining_path_length):
        backtrack_path[remaining_path_length - 1 - x] = inverse_path[x][backtrack_path[remaining_path_length - x]]
    return backtrack_path


print(backtrack(prob, path))

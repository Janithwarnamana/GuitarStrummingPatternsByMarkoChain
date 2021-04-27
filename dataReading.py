import pandas as pd

data = pd.read_excel('D:\ss.xls')

st = ['D', '&', 'v', '^', 'v^', '^v', '&^', '&v']
n = len(st)
array2d = [[0 for i in range(n)]] * n
rowLen = len(data.index)


def transition_probability_matrix(_data):
    tp_matrix = [[0] * n for _ in range(n)]
    for transitions in _data:
        for (i, j) in zip(transitions, transitions[1:]):
            tp_matrix[i][j] += 1

    # now convert to probabilities:
    for row in tp_matrix:
        s = sum(row)
        if s > 0:
            row[:] = [f / s for f in row]
    return tp_matrix


def preprocess(_data):
    arr = [[0 for i in range(4)] for j in range(rowLen)]
    for i, row in _data.iterrows():
        row_ = row[:-2]
        for j, val in enumerate(row_):
            arr[i][j] = st.index(val)
        return arr


# for index, row in data.iterrows():
#     print(str(index) + " " + str(row))
print(preprocess(data))

# print(st.index('v'))

# print(list(zip(path.loc[1], path.loc[1][1:-2])))
matrix = transition_probability_matrix(preprocess(data))
df = pd.DataFrame(matrix)
print(df)
# print(len(path.index) - 1)
# print(path[0])

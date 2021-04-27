import pandas as pd


class MarkovChain:

    @staticmethod
    def generate_markov_chain(_transition_matrix, _strum_positions):

        tpm_length = len(_transition_matrix)
        # 1 st Strum always a Down strum
        # e.g.3x3
        #               1 0 0 0
        #   start(1)    _ 0 0 0    end
        #               _ 0 0 0
        # matrix chain initialize1:  all zeros
        m_chain_prob = [[0 for i in range(_strum_positions)] for j in range(len(_transition_matrix))]
        m_chain_path = [[-1 for i in range(len(_transition_matrix))] for j in range(_strum_positions)]
        # matrix chain initialize2: 1st element 1 for Down Strum
        m_chain_prob[0][0] = 1

        # 2d matrix transpose
        # e.g.3x3
        #               start(1)
        #               1 - -
        #               2 2 2
        #               3 3 3
        #               4 4 4
        #               end
        m_chain_prob = [[*row] for row in [*zip(*m_chain_prob)]]

        for i, i_val in enumerate(m_chain_prob):
            for j, j_val in enumerate(i_val):
                if i > 0:
                    max1 = 0
                    for x in range(tpm_length):
                        temp = m_chain_prob[i - 1][x] * _transition_matrix[x][j]
                        if temp > max1:
                            max1 = temp
                            m_chain_path[i][j] = x
                    m_chain_prob[i][j] = max1

        return [[*row] for row in [*zip(*m_chain_prob)]], [[*row] for row in [*zip(*m_chain_path)]]


# st = ['D', '&', 'v', '^', 'v^', '^v', '&^', '&v']
# strum_positions = 4
#
# # tp_matrix
# # e.g.3x3
# # [.2, .2, .3]
# # [.3, .2, .3]
# # [.3, .1, .2]
# tp = [[0.2, 0.2, 0.3], [0.3, 0.2, 0.3], [0.3, 0.1, 0.2]]
# print(len(tp))
#
# #    0    1     2      3
# # 0  1  0.2  0.06  0.018
# # 1  0  0.3  0.06  0.018
# # 2  0  0.3  0.03  0.012
# chain, path = MarkovChain.generate_markov_chain(tp, strum_positions)
# print(pd.DataFrame(chain))
# print(pd.DataFrame(path))

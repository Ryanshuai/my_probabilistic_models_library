import numpy as np

from randomvariable import RandomVariable, p

L0 = RandomVariable([0.3333333, 0.3333333, 0.333333])
C = RandomVariable([0.5, 0.5])

mat = [[0.95, 0.05],
       [0.10, 0.90],
       [0.10, 0.90]]
SL0 = RandomVariable(mat, parents=(L0,))

mat = [[0.95, 0.05],
       [0.10, 0.90],
       [0.95, 0.05]]
SR0 = RandomVariable(mat, parents=(L0,))

mat = [[[1, 0, 0],
        [0.1, 0.9, 0]],
       [[0.9, 0.1, 0],
        [0, 0.1, 0.9]],
       [[0, 0.9, 0.1],
        [0, 0, 1]]]

L1 = RandomVariable(mat, parents=(L0, C))

mat = [[0.95, 0.05],
       [0.10, 0.90],
       [0.10, 0.90]]
SL1 = RandomVariable(mat, parents=(L1,))

mat = [[0.95, 0.05],
       [0.10, 0.90],
       [0.95, 0.05]]
SR1 = RandomVariable(mat, parents=(L1,))

T = RandomVariable([0.2, 0.8])

mat = [[[[1, 0],
         [1, 0]],
        [[0, 1],
         [0, 1]]],
       [[[1, 0],
         [0, 1]],
        [[1, 0],
         [0, 1]]]]
RL = RandomVariable(mat, parents=(T, SL0, SL1))

mat = [[[[1, 0],
         [1, 0]],
        [[0, 1],
         [0, 1]]],
       [[[1, 0],
         [0, 1]],
        [[1, 0],
         [0, 1]]]]
RR = RandomVariable(mat, parents=(T, SR0, SR1))

p1 = p(({C: 1, RR: 1, RL: 1}))
print(p1)

p2 = p(({RR: 1, RL: 1}))
print(p2)

print(p1 / p2)

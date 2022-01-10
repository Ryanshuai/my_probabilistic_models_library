from randomvariable import RandomVariable

E = RandomVariable("E", 2, [0.998, 0.002])
B = RandomVariable("B", 2, [0.999, 0.001])

pa_mat = [[[0.999, 0.001], [0.06, 0.94]], [[0.71, 0.29], [0.05, 0.95]]]
A = RandomVariable("A", 2, pa_mat, (E, B))

pm_mat = [[0.95, 0.05], [0.1, 0.9]]
M = RandomVariable("M", 2, pm_mat, (A,))

print(M.p({"M": 1}))
print(A.p({"A": 1}))

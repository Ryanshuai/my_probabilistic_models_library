from randomvariable_v2 import RandomVariable, p

E = RandomVariable([0.998, 0.002])
B = RandomVariable([0.999, 0.001])

pa_mat = [[[0.999, 0.001], [0.06, 0.94]], [[0.71, 0.29], [0.05, 0.95]]]
A = RandomVariable(pa_mat, (E, B))

pm_mat = [[0.95, 0.05], [0.1, 0.9]]
M = RandomVariable(pm_mat, (A,))

print(p({M: 1}))
print(p({A: 1}))

print(p({B: 1, A: 1}) / p({A: 1}))
print(p({B: 1, A: 1, E: 1}) / p({A: 1, E: 1}))
print(p({B: 1, M: 1}) / p({M: 1}))
print(p({B: 1, M: 1, E: 1}) / p({M: 1, E: 1}))

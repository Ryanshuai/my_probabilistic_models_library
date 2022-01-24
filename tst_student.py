from randomvariable import RandomVariable, p

D = RandomVariable([0.6, 0.4])
I = RandomVariable([0.7, 0.3])

mat = [[[0.3, 0.4, 0.3], [0.05, 0.25, 0.7]], [[0.9, 0.08, 0.02], [0.5, 0.3, 0.2]]]
G = RandomVariable(mat, (I, D))

mat = [[0.95, 0.05], [0.2, 0.8]]
S = RandomVariable(mat, (I,))

mat = [[0.1, 0.9], [0.4, 0.6], [0.99, 0.01]]
L = RandomVariable(mat, (G,))

for i in range(2):
    for s in range(2):
        for l in range(2):
            print(i, s, l, "\t", p({I: i, L: l, S: s}) / p({L: l, S: s}))

print("-----------------------------------------")
print(p({S: 0, D: 0, L: 1}) / p({D: 0, L: 1}))
print(p({S: 1, D: 0, L: 1}) / p({D: 0, L: 1}))

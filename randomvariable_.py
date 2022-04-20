import numpy as np
from itertools import product
from functools import reduce
from operator import mul


class RandomVariable:
    def __init__(self, p_matrix, ordered_parents=None):
        assert ordered_parents is None or isinstance(ordered_parents, tuple)
        self.p_matrix = np.array(p_matrix)
        assert np.max(np.abs(np.sum(self.p_matrix, axis=-1) - 1)) < 1e-5
        assert ordered_parents is None or len(ordered_parents) == self.p_matrix.ndim - 1

        self.cardinality = self.p_matrix.shape[-1]
        self.parents = ordered_parents

        self.probability = None if ordered_parents else self.p_matrix
        self.p_xu_matrix = np.array(self.p_matrix)
        self.M_matrix = np.zeros_like(self.p_matrix)

    def reset(self, p_matrix):
        self.p_matrix = np.array(p_matrix)
        self.p_xu_matrix = np.array(self.p_matrix)
        self.M_matrix = np.zeros_like(self.p_matrix)
        self.probability = None if self.parents else self.p_matrix

    def calculate_probability(self):
        if self.probability is not None:
            return self.probability

        comb_prob_dict = self.parents_combination_probability()
        for comb, prob in comb_prob_dict.items():
            self.p_xu_matrix[comb] *= prob
        self.probability = np.sum(self.p_xu_matrix, axis=tuple(range(self.p_xu_matrix.ndim - 1)))
        return self.probability

    def parents_combination_probability(self):
        parents_keys = [range(parent.cardinality) for parent in self.parents]
        parents_values = [parent.calculate_probability() for parent in self.parents]
        parents_combination = list(product(*parents_keys))
        parents_combination_probability = [reduce(mul, ps) for ps in list(product(*parents_values))]
        return dict(zip(parents_combination, parents_combination_probability))

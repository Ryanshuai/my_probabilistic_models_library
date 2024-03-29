import numpy as np
import itertools
from functools import reduce


class RandomVariable:
    def __init__(self, p_matrix, parents=None):
        assert parents is None or isinstance(parents, tuple)
        self.p_matrix = np.array(p_matrix)
        assert np.max(np.abs(np.sum(self.p_matrix, axis=-1) - 1)) < 1e-5
        assert parents is None or len(parents) == self.p_matrix.ndim - 1

        self.cardinality = self.p_matrix.shape[-1]
        self.parents = parents or ()
        self.possible_value = tuple(range(self.cardinality))
        self.dependent_rv = None

    def p_edge(self, rv_to_value):
        p_matrix = self.p_matrix
        for parent in self.parents:
            parent_rv_value = rv_to_value[parent]
            p_matrix = p_matrix[parent_rv_value]

        return p_matrix[rv_to_value[self]]

    def find_all_dependent_rv(self):
        dependent_rv = {self}
        for parent in self.parents:
            dependent_rv |= parent.find_all_dependent_rv()
        self.dependent_rv = dependent_rv
        return self.dependent_rv


def p(specify_dict):
    relevant_rvs = set()
    for rv, value in specify_dict.items():
        rv.possible_value = (value,)
        relevant_rvs |= rv.find_all_dependent_rv()

    possible_combinations = itertools.product(*[rv.possible_value for rv in relevant_rvs])
    p_res = 0
    for possible_combination in possible_combinations:
        rv_to_value = dict(zip(relevant_rvs, possible_combination))
        p_s = [rv.p_edge(rv_to_value) for rv in relevant_rvs]
        p_combination = reduce(lambda x, y: x * y, p_s)
        p_res += p_combination

    for rv, value in specify_dict.items():
        rv.possible_value = tuple(range(rv.cardinality))
    return p_res

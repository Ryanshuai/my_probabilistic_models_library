import numpy as np
import itertools
from functools import reduce


class RandomVariable:
    def __init__(self, name, cardinality, p_matrix, parents=None):
        assert parents is None or isinstance(parents, tuple)
        self.name = name
        self.cardinality = cardinality
        self.p_matrix = np.array(p_matrix)
        self.parents = parents or ()
        self.possible_value = tuple(range(cardinality))
        self.relied_rv = None

    def __str__(self):
        return self.name

    def check_p_matrix(self):
        pass  # TODO

    def p_edge(self, rv_name_to_value):
        p_matrix = self.p_matrix
        for parent in self.parents:
            parent_rv_name = parent.name
            parent_rv_value = rv_name_to_value[parent_rv_name]
            p_matrix = p_matrix[parent_rv_value]

        return p_matrix[rv_name_to_value[self.name]]

    def find_all_relevant_rv(self):
        relevant_rv = {self.name: self}
        for parent in self.parents:
            relevant_rv.update(parent.find_all_relevant_rv())
        self.relied_rv = relevant_rv
        return relevant_rv

    def find_combinations(self, rvs):
        names = rvs.keys()
        possible_combinations = itertools.product(*[rv.possible_value for rv in rvs.values()])
        return names, possible_combinations

    def reset_possible_values(self):
        self.possible_value = tuple(range(self.cardinality))
        for parent in self.parents:
            parent.possible_value = tuple(range(parent.cardinality))
            parent.reset_possible_values()

    def p(self, specify_dict=None):
        specify_dict = specify_dict or dict()
        self.find_all_relevant_rv()
        for name, value in specify_dict.items():
            self.relied_rv[name].possible_value = (value,)
        names, combs = self.find_combinations(self.relied_rv)
        p_res = 0
        for comb in combs:
            rv_name_to_value = dict(zip(names, comb))
            p_s = [rv.p_edge(rv_name_to_value) for rv in self.relied_rv.values()]
            p_comb = reduce(lambda x, y: x * y, p_s)
            p_res += p_comb
        self.reset_possible_values()
        return p_res


class Graph:
    def __init__(self, nodes):
        nodes = None

    def p(self, specify_dict):
        pass

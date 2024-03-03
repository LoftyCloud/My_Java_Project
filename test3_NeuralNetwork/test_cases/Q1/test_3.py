import numpy as np
import matplotlib.pyplot as plt
import os
import test_utils
#import util

import neural_network

def max_score():
    return 3

def timeout():
    return 60

def test():
    alpha = np.array([0.5] * 18).reshape(3, 6)
    alpha[:, 0] = 0
    beta = np.array([0.5] * 40).reshape(10, 4)
    beta[:, 0] = 0
    x = np.array([0,1,2,3,4,5]).reshape(6,1)

    test_params = {"x": x, "y": 9, "alpha":  alpha, "beta": beta}
    expected = {"expected": "Q1_forward10.npz"}
    return test_utils.run_and_testforward(test_params, expected, max_score())

if __name__ == "__main__":
    test()

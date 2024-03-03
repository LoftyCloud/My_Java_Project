import numpy as np
import matplotlib.pyplot as plt
import os
import test_utils
#import util

import neural_network

def max_score():
    return 4

def timeout():
    return 60

def test():
    alpha = np.linspace(0,1,18).reshape(3,6)
    alpha[:, 0] = 0
    beta = np.linspace(0,1,40).reshape(10,4)
    beta[:, 0] = 0
    x = np.array([0,0,0,0,0,0]).reshape(6,1)

    test_params = {"x": x, "y": 2, "alpha":  alpha, "beta": beta, "other": "Q1_forward01.npz"}
    expected = {"expected": "Q2_backward01.npz"}
    return test_utils.run_and_testbackward(test_params, expected, max_score())

if __name__ == "__main__":
    test()

import numpy as np
import matplotlib.pyplot as plt
import os
import test_utils
#import util

import neural_network

def max_score():
    return 2

def timeout():
    return 60

def test():
    test_params = {"num_epoch" : 1, "num_hidden": 3, "init_rand": False, "learning_rate": 0.1}
    expected = {"expected_err_train": 0.802, "expected_err_val": 0.8,
                "expected_y_hat_train": "check1_train_out.labels","expected_y_hat_val": "check1_test_out.labels",
                "expected_params": "check1_params.npz"}
    return test_utils.run_and_testprediction(test_params, expected, max_score())

if __name__ == "__main__":
    test()

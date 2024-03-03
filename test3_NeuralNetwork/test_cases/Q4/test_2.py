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
    test_params = {"num_epoch" : 5, "num_hidden": 4, "init_rand": False, "learning_rate": 0.1}
    expected = {"expected_err_train": 0.728, "expected_err_val": 0.77,
                "expected_y_hat_train": "check2_train_out.labels","expected_y_hat_val": "check2_test_out.labels",
                "expected_params": "check2_params.npz"}
    return test_utils.run_and_testprediction(test_params, expected, max_score())

if __name__ == "__main__":
    test()

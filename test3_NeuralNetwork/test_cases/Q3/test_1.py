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
    test_params = {"num_epoch" : 1, "num_hidden": 3, "init_rand": False, "learning_rate": 0.1}
    expected = {"expected_loss_per_epoch_train": [2.20621883449], "expected_loss_per_epoch_val": [2.20882948975],
                "expected_params": "check1_params.npz"}
    return test_utils.run_and_testSGD(test_params, expected, max_score())

if __name__ == "__main__":
    test()

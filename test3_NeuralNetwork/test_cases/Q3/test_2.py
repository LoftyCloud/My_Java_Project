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
    test_params = {"num_epoch" : 5, "num_hidden": 4, "init_rand": False, "learning_rate": 0.1}
    expected = {"expected_loss_per_epoch_train": [2.18506276114,1.90103257727,1.8066109847,1.75713392877,1.72508257456],
                "expected_loss_per_epoch_val": [2.18827302588,1.91363803461,1.8286100067,1.78588295296,1.75834415284],
                "expected_params": "check2_params.npz"}
    return test_utils.run_and_testSGD(test_params, expected, max_score())

if __name__ == "__main__":
    test()

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
    test_params = {"num_epoch" : 10, "num_hidden": 3, "init_rand": True, "learning_rate": 0.1}
    expected = {"expected_loss_per_epoch_train": [2.13519332839,1.76996211138,1.55387795897,1.41147271246,1.28852706403,1.20167355834,1.15100059406,1.10987629638,1.08041943631,1.05238886696],
                   "expected_loss_per_epoch_val": [2.14740321309,1.82483114606,1.64415458222,1.55112352604,1.50111771342,1.47148368086,1.46419730344,1.4644623612,1.45379240211,1.47432155656]}
    return test_utils.run_and_testSGD(test_params, expected, max_score())

if __name__ == "__main__":
    test()

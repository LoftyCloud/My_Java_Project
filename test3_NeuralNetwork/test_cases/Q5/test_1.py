import numpy as np
import matplotlib.pyplot as plt
import os
import test_utils
# import util

import neural_network

def max_score():
    return 4

def timeout():
    return 60

def test():
    test_params = {"num_epoch" : 10, "num_hidden": 100, "init_rand": False, "learning_rate": 0.2}
    expected = {"expected_loss_per_epoch_train": [1.9460229984,1.78968791726,1.70890452855,1.65178850742,1.60753288393,1.57148388072,1.54149276208,1.51669022547,1.49640381826,1.47973929805], 
                   "expected_loss_per_epoch_val": [1.96198795399,1.81906319375,1.74904236545,1.70332862975,1.67179860844,1.64906682145,1.6318912785,1.61880186166,1.6092444253,1.60280318786], 
                   "expected_err_train": 0.582, "expected_err_val": 0.61,
                   "expected_y_hat_train": "check3_train_out.labels","expected_y_hat_val": "check3_test_out.labels"}
    return test_utils.run_and_testNN(test_params, expected, max_score())

if __name__ == "__main__":
    test()

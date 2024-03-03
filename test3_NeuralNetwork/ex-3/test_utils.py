import numpy as np
import matplotlib.pyplot as plt
import os

import neural_network


def max_score():
    return 2


def timeout():
    return 60


def load_labels(filename):
    f = open(filename, 'r', encoding="UTF8").readlines()
    labels = []
    for s in f:
        curlabel = int(s[:s.find('\n')])
        labels.append(curlabel)
    return labels


def check_metrics(expec, actua, tol):
    correct_count = 0
    total_count = len(expec)
    for i in range(total_count):
        e_metric = expec[i]
        a_metric = actua[i]
        error = abs(e_metric - a_metric) / (e_metric + 0.0000000000000001)
        if error <= tol:
            correct_count += 1
    score = float(correct_count) / float(total_count)
    return score


def check_param(expec, actua, tol):
    expec = expec.flatten()
    actua = actua.flatten()
    correct_count = 0
    total_count = len(expec)
    for i in range(total_count):
        e_metric = expec[i]
        a_metric = actua[i]
        error = abs(e_metric - a_metric) / (e_metric + 0.0000000000000001)
        if error <= tol:
            correct_count += 1
    score = float(correct_count) / float(total_count)
    return score


def check_labels(expec, actua):
    match = np.sum((expec == actua).astype(float))
    total_count = len(expec)
    score = float(match) / float(total_count)
    return score


def run_and_testbackward(test_params, expected, max_points):
    x, y, alpha, beta = test_params['x'], test_params['y'], test_params['alpha'], test_params['beta']
    others = np.load('Reference_Outputs/' + test_params['other'])
    z, y_hat = others['z'], others['y']

    result = neural_network.NNBackward(x, y, alpha, beta, z, y_hat)
    actual_alpha, actual_beta = result[0], result[1]
    actual_g_b, actual_g_z, actual_g_a = result[2], result[3], result[4]

    expected_vals = np.load('Reference_Outputs/' + expected['expected'])
    expected_alpha, expected_beta = expected_vals['g_alpha'], expected_vals['g_beta']
    expected_g_b, expected_g_z, expected_g_a = expected_vals['g_b'], expected_vals['g_z'], expected_vals['g_a']

    score = 0
    num_checks = 0
    msg_list = ['']

    # check g_b
    assert (
            expected_g_b.shape == actual_g_b.shape), 'Incorrect size found for g_b (softmaxBackward). \nExpected: \n{}\n\nFound: \n{}\n'.format(
        expected_g_b.shape, actual_g_b.shape)
    if np.allclose(expected_g_b, actual_g_b, rtol=0.001):
        score += 1
    else:
        msg_list.append(
            'Incorrect g_b (softmaxBackward). \nExpected: \n{}\n\nFound actual: \n{}\n'.format(expected_g_b,
                                                                                               actual_g_b))
    num_checks += 1

    # check g_beta
    assert (
            expected_beta.shape == actual_beta.shape), 'Incorrect size found for g_beta. \nExpected: \n{}\n\nFound: \n{}\n'.format(
        expected_beta.shape, actual_beta.shape)
    if np.allclose(expected_beta, actual_beta, rtol=0.001):
        score += 1
    else:
        msg_list.append(
            'Incorrect g_beta. \nExpected: \n{}\n\nFound actual: \n{}\n'.format(expected_beta, actual_beta))
    num_checks += 1

    # check g_z
    assert (
            expected_g_z.shape == actual_g_z.shape), 'Incorrect size found for g_z (linearBackward). \nExpected: \n{}\n\nFound: \n{}\n'.format(
        expected_g_z.shape, actual_g_z.shape)
    if np.allclose(expected_g_z, actual_g_z, rtol=0.001):
        score += 1
    else:
        msg_list.append(
            'Incorrect g_z (linearBackward). \nExpected: \n{}\n\nFound actual: \n{}\n'.format(expected_g_z, actual_g_z))
    num_checks += 1

    # check g_a
    assert (
            expected_g_a.shape == actual_g_a.shape), 'Incorrect size found for g_a (sigmoidBackward). \nExpected: \n{}\n\nFound: \n{}\n'.format(
        expected_g_a.shape, actual_g_a.shape)
    if np.allclose(expected_g_a, actual_g_a, rtol=0.001):
        score += 1
    else:
        msg_list.append(
            'Incorrect g_a (sigmoidBackward). \nExpected: \n{}\n\nFound actual: \n{}\n'.format(expected_g_a,
                                                                                               actual_g_a))
    num_checks += 1

    # check g_alpha
    assert (
                expected_alpha.shape == actual_alpha.shape), 'Incorrect size found for g_alpha. \nExpected: \n{}\n\nFound: \n{}\n'.format(
        expected_alpha.shape, actual_alpha.shape)
    if np.allclose(expected_alpha, actual_alpha, rtol=0.001):
        score += 1
    else:
        msg_list.append(
            'Incorrect g_alpha. \nExpected: \n{}\n\nFound actual: \n{}\n'.format(expected_alpha, actual_alpha))
    num_checks += 1

    test_score = score / num_checks * max_points

    # test_score = score
    if len(msg_list) == 1:
        test_output = 'PASS\n'
    else:
        test_output = '\n'.join(msg_list)

    return int(test_score), test_output


def run_and_testforward(test_params, expected, max_points):
    x, y, alpha, beta = test_params['x'], test_params['y'], test_params['alpha'], test_params['beta']
    result = neural_network.NNForward(x, y, alpha, beta)

    actual_x, actual_a, actual_z = result[0], result[1], result[2]
    actual_b, actual_y, actual_J = result[3], result[4], result[5]

    expected_vals = np.load('Reference_Outputs/' + expected['expected'])
    expected_x, expected_a, expected_z = expected_vals['x'], expected_vals['a'], expected_vals['z']
    expected_b, expected_y, expected_J = expected_vals['b'], expected_vals['y'], expected_vals['J']

    score = 0
    num_checks = 0
    msg_list = ['']

    # check x
    assert (expected_x.shape == actual_x.shape), 'Incorrect size found for x. \nExpected: \n{}\n\nFound: \n{}\n'.format(
        expected_x.shape, actual_x.shape)
    if np.allclose(expected_x, actual_x, rtol=0.001):  # if np.allclose(expected_x, actual_x, rtol=0.001)
        score += 1
    else:
        msg_list.append(
            'Incorrect x. \nExpected: \n{}\n\nFound actual: \n{}\n'.format(expected_x, actual_x))
    num_checks += 1

    # check a (first linear forward)
    assert (
                expected_a.shape == actual_a.shape), 'Incorrect size found for a (first linear forward). \nExpected: \n{}\n\nFound: \n{}\n'.format(
        expected_a.shape, actual_a.shape)
    if np.allclose(expected_a, actual_a, rtol=0.001):
        score += 1
    else:
        msg_list.append(
            'Incorrect a (first linear forward). \nExpected: \n{}\n\nFound actual: \n{}\n'.format(expected_a, actual_a))
    num_checks += 1

    # check z (sigmoid forward)
    assert (
                expected_z.shape == actual_z.shape), 'Incorrect size found for z (sigmoid forward). \nExpected: \n{}\n\nFound: \n{}\n'.format(
        expected_z.shape, actual_z.shape)
    if np.allclose(expected_z, actual_z, rtol=0.001):
        score += 1
    else:
        msg_list.append(
            'Incorrect z (sigmoid forward). \nExpected: \n{}\n\nFound actual: \n{}\n'.format(expected_z, actual_z))
    num_checks += 1

    # check b (second linear forward)
    assert (expected_b.shape == actual_b.shape), 'Incorrect size found for b. \nExpected: \n{}\n\nFound: \n{}\n'.format(
        expected_b.shape, actual_b.shape)
    if np.allclose(expected_b, actual_b, rtol=0.001):
        score += 1
    else:
        msg_list.append(
            'Incorrect b (second linear forward). \nExpected: \n{}\n\nFound actual: \n{}\n'.format(expected_b,
                                                                                                   actual_b))
    num_checks += 1

    # check y (softmax forward)
    assert (expected_y.shape == actual_y.shape), 'Incorrect size found for y. \nExpected: \n{}\n\nFound: \n{}\n'.format(
        expected_y.shape, actual_y.shape)
    if np.allclose(expected_y, actual_y, rtol=0.001):
        score += 1
    else:
        msg_list.append(
            'Incorrect y (softmax forward). \nExpected: \n{}\n\nFound actual: \n{}\n'.format(expected_y, actual_y))
    num_checks += 1

    # check J (cross entropy forward)

    assert (isinstance(actual_J, (int, float))), 'Incorrect type found for J. Expected int/float, found {}.'.format(
        type(actual_J))
    if np.allclose(expected_J, actual_J, rtol=0.001):
        score += 1
    else:
        msg_list.append(
            'Incorrect J (cross-entropy forward). \nExpected: \n{}\n\nFound actual: \n{}\n'.format(expected_J,
                                                                                                   actual_J))
    num_checks += 1

    test_score = score / num_checks * max_points

    # test_score = score
    if len(msg_list) == 1:
        test_output = 'PASS\n'
    else:
        test_output = '\n'.join(msg_list)

    return int(test_score), test_output


def run_and_testprediction(test_params, expected, max_points):
    X_train, y_train, X_val, y_val = neural_network.load_data_small()
    init_rand = test_params["init_rand"]
    params = np.load('Reference_Outputs/' + expected['expected_params'])
    result = neural_network.prediction(X_train, y_train, X_val, y_val, params['alpha'], params['beta'])

    actual_err_train = result[0]
    actual_err_val = result[1]
    actual_y_hat_train = result[2]
    actual_y_hat_val = result[3]

    if not init_rand:
        expected_err_train = expected["expected_err_train"]
        expected_err_val = expected["expected_err_val"]
        expected_train_labels_list = load_labels("Reference_Outputs/" + expected["expected_y_hat_train"])
        expected_y_hat_train = np.asarray(expected_train_labels_list)
        expected_val_labels_list = load_labels("Reference_Outputs/" + expected["expected_y_hat_val"])
        expected_y_hat_val = np.asarray(expected_val_labels_list)

    score = 0
    num_checks = 0
    tol = 0.01
    if init_rand:
        tol = 0.15

    msg_list = ['']
    if init_rand:
        exp_acc = 0.95
    else:
        exp_acc = 1.0

    # checking error rates
    if not init_rand:
        assert (isinstance(actual_err_train,
                           (int, float))), 'Incorrect type found for Train error. Expected int/float, found {}.'.format(
            type(actual_err_train))
        cur_score = abs(expected_err_train - actual_err_train) / (expected_err_train + 0.0000000000000001)
        if cur_score <= tol:
            cur_score = 1.0
        if abs(actual_err_train) > 1.0 or actual_err_train < 0:
            cur_score = 0
        score += cur_score
        if abs(cur_score - 1) > 0.000001:
            msg_list.append(
                'Incorrect error rate found in Train error. \nExpected: \n{}\n\nFound actual: \n{}\n'.format(
                    expected_err_train, actual_err_train))
        num_checks += 1

        assert (isinstance(actual_err_val,
                           (int,
                            float))), 'Incorrect type found for Validation error. Expected int/float, found {}.'.format(
            type(actual_err_val))
        cur_score = abs(expected_err_val - actual_err_val) / (expected_err_val + 0.0000000000000001)
        if cur_score <= tol:
            cur_score = 1.0
        if abs(actual_err_val) > 1.0 or actual_err_val < 0:
            cur_score = 0
        score += cur_score
        if abs(cur_score - 1) > 0.000001:
            msg_list.append(
                'Incorrect error rate found in Validation error. \nExpected: \n{}\n\nFound actual: \n{}\n'.format(
                    expected_err_val, actual_err_val))
        num_checks += 1

    # checking labels
    if not init_rand:
        assert (len(expected_y_hat_train) == len(
            actual_y_hat_train)), 'Incorrect length found for Train Labels. \nExpected: \n{}\n\nFound: \n{}\n'.format(
            len(expected_y_hat_train), len(actual_y_hat_train))
        match = check_labels(expected_y_hat_train, actual_y_hat_train)
        cur_score = 0
        if match >= 0.65:
            cur_score = (match - 0.65) / 0.35
        if abs(cur_score - 1) > 0.000001:
            msg_list.append(
                'Incorrect prediction found for Train Labels. Expected matching accuracy {}, found actual accuracy {}.'.format(
                    exp_acc, cur_score))
        num_checks += 1
        score += cur_score

        # assert abs(train_labels_diff) < 0.01, 'Incorrect prediction found for Train Labels. {} labels are predicted incorrectly'.format(train_labels_diff)
        assert (len(expected_y_hat_val) == len(
            actual_y_hat_val)), 'Incorrect length found for Validation Labels. \nExpected: \n{}\n\nFound: \n{}\n'.format(
            len(expected_y_hat_val), len(actual_y_hat_val))
        match_test = check_labels(expected_y_hat_val, actual_y_hat_val)
        cur_score = 0
        if match_test >= 0.65:
            cur_score = (match_test - 0.65) / 0.35
        num_checks += 1
        if abs(cur_score - 1) > 0.000001:
            msg_list.append(
                'Incorrect prediction found for Validation Labels. Expected matching accuracy {}, found actual accuracy {}.'.format(
                    exp_acc, cur_score))
        score += cur_score

    test_score = score / num_checks * max_points

    # test_score = score
    if len(msg_list) == 1:
        test_output = 'PASS\n'
    else:
        test_output = '\n'.join(msg_list)

    return int(test_score), test_output


def run_and_testSGD(test_params, expected, max_points):
    X_train, y_train, X_val, y_val = neural_network.load_data_small()
    num_epoch = test_params["num_epoch"]
    num_hidden = test_params["num_hidden"]
    init_rand = test_params["init_rand"]
    learning_rate = test_params["learning_rate"]
    result = neural_network.SGD(X_train, y_train, X_val, y_val,
                                num_hidden, num_epoch, init_rand, learning_rate)

    actual_alpha = result[0]
    actual_beta = result[1]
    actual_loss_per_epoch_train = result[2]
    actual_loss_per_epoch_val = result[3]

    expected_loss_per_epoch_train = expected["expected_loss_per_epoch_train"]
    expected_loss_per_epoch_val = expected["expected_loss_per_epoch_val"]
    if not init_rand:
        params = np.load('Reference_Outputs/' + expected['expected_params'])
        expected_alpha = params['alpha']
        expected_beta = params['beta']

    score = 0
    num_checks = 0
    tol = 0.01
    if init_rand:
        tol = 0.15

    msg_list = ['']
    if init_rand:
        exp_acc = 0.95
    else:
        exp_acc = 1.0

    # checking alpha and beta
    if not init_rand:
        assert (
                    expected_alpha.shape == actual_alpha.shape), 'Incorrect shape found for alpha. \nExpected: \n{}\n\nFound: \n{}\n'.format(
            expected_alpha.shape, actual_alpha.shape)
        cur_score = check_param(expected_alpha, actual_alpha, tol)
        if init_rand and cur_score >= 0.95:
            cur_score = 1.0
        score += cur_score
        if abs(cur_score - 1) > 0.000001:
            msg_list.append(
                'Incorrect alpha found from SGD. \nExpected: \n{}\n\nFound: \n{}\n'.format(
                    expected_alpha, actual_alpha))
        num_checks += 1

    if not init_rand:
        assert (
                    expected_beta.shape == actual_beta.shape), 'Incorrect shape found for beta. \nExpected: \n{}\n\nFound: \n{}\n'.format(
            expected_beta.shape, actual_beta.shape)
        cur_score = check_param(expected_beta, actual_beta, tol)
        if init_rand and cur_score >= 0.95:
            cur_score = 1.0
        score += cur_score
        if abs(cur_score - 1) > 0.000001:
            msg_list.append(
                'Incorrect beta found from SGD. \nExpected: \n{}\n\nFound: \n{}\n'.format(
                    expected_beta, actual_beta))
        num_checks += 1

    # checking training metrics
    assert (len(actual_loss_per_epoch_train) == len(
        expected_loss_per_epoch_train)), 'Incorrect length found for Train Loss. \nExpected: \n{}\n\nFound: \n{}\n'.format(
        len(expected_loss_per_epoch_train), len(actual_loss_per_epoch_train))
    cur_score = check_metrics(expected_loss_per_epoch_train, actual_loss_per_epoch_train, tol)
    if init_rand and cur_score >= 0.95:
        cur_score = 1.0
    score += cur_score
    if abs(cur_score - 1) > 0.000001:
        msg_list.append(
            'Incorrect cross entropy loss found in Train Loss. Expected matching accuracy {}, found actual accuracy {}.'.format(
                exp_acc, cur_score))
    num_checks += 1

    # checking validation metrics
    assert (len(actual_loss_per_epoch_val) == len(
        expected_loss_per_epoch_val)), 'Incorrect length found for Validation Loss. \nExpected: \n{}\n\nFound: \n{}\n'.format(
        len(expected_loss_per_epoch_val), len(actual_loss_per_epoch_val))
    cur_score = check_metrics(expected_loss_per_epoch_val, actual_loss_per_epoch_val, tol)
    if init_rand and cur_score >= 0.95:
        cur_score = 1.0
    score += cur_score
    if abs(cur_score - 1) > 0.0000000000000001:
        msg_list.append(
            'Incorrect cross entropy loss found in Validation Loss. Expected matching accuracy {}, found actual accuracy {}.'.format(
                exp_acc, cur_score))
    num_checks += 1

    test_score = score / num_checks * max_points

    # test_score = score
    if len(msg_list) == 1:
        test_output = 'PASS\n'
    else:
        test_output = '\n'.join(msg_list)

    return int(test_score), test_output


def run_and_testNN(test_params, expected, max_points):
    X_train, y_train, X_val, y_val = neural_network.load_data_small()
    num_epoch = test_params["num_epoch"]
    num_hidden = test_params["num_hidden"]
    init_rand = test_params["init_rand"]
    learning_rate = test_params["learning_rate"]
    result = neural_network.train_and_valid(X_train, y_train, X_val, y_val,
                                            num_epoch, num_hidden, init_rand, learning_rate)

    actual_loss_per_epoch_train = result[0]
    actual_loss_per_epoch_val = result[1]
    actual_err_train = result[2]
    actual_err_val = result[3]
    actual_y_hat_train = result[4]
    actual_y_hat_val = result[5]

    expected_loss_per_epoch_train = expected["expected_loss_per_epoch_train"]
    expected_loss_per_epoch_val = expected["expected_loss_per_epoch_val"]

    if not init_rand:
        expected_err_train = expected["expected_err_train"]
        expected_err_val = expected["expected_err_val"]
        expected_train_labels_list = load_labels("Reference_Outputs/" + expected["expected_y_hat_train"])
        expected_y_hat_train = np.asarray(expected_train_labels_list)
        expected_val_labels_list = load_labels("Reference_Outputs/" + expected["expected_y_hat_val"])
        expected_y_hat_val = np.asarray(expected_val_labels_list)

    score = 0
    num_checks = 0
    tol = 0.01
    if init_rand:
        tol = 0.15

    msg_list = ['']
    if init_rand:
        exp_acc = 0.95
    else:
        exp_acc = 1.0

    # checking training metrics
    assert (len(actual_loss_per_epoch_train) == len(
        expected_loss_per_epoch_train)), 'Incorrect length found for Train Loss. \nExpected: \n{}\n\nFound: \n{}\n'.format(
        len(expected_loss_per_epoch_train), len(actual_loss_per_epoch_train))
    cur_score = check_metrics(expected_loss_per_epoch_train, actual_loss_per_epoch_train, tol)
    if init_rand and cur_score >= 0.95:
        cur_score = 1.0
    score += cur_score
    if abs(cur_score - 1) > 0.000001:
        msg_list.append(
            'Incorrect cross entropy loss found in Train Loss. Expected matching accuracy {}, found actual accuracy {}.'.format(
                exp_acc, cur_score))
    num_checks += 1

    if not init_rand:
        assert (isinstance(actual_err_train,
                           (int, float))), 'Incorrect type found for Train error. Expected int/float, found {}.'.format(
            type(actual_err_train))
        cur_score = abs(expected_err_train - actual_err_train) / (expected_err_train + 0.0000000000000001)
        if cur_score <= tol:
            cur_score = 1.0
        if abs(cur_score) > 1.0 or cur_score < 0:
            cur_score = 0
        score += cur_score
        if abs(cur_score - 1) > 0.000001:
            msg_list.append(
                'Incorrect error rate found in Train error. \nExpected: \n{}\n\nFound actual: \n{}\n'.format(
                    expected_err_train, actual_err_train))
        num_checks += 1

    # checking validation metrics
    assert (len(actual_loss_per_epoch_val) == len(
        expected_loss_per_epoch_val)), 'Incorrect length found for Validation Loss. \nExpected: \n{}\n\nFound: \n{}\n'.format(
        len(expected_loss_per_epoch_val), len(actual_loss_per_epoch_val))
    cur_score = check_metrics(expected_loss_per_epoch_val, actual_loss_per_epoch_val, tol)
    if init_rand and cur_score >= 0.95:
        cur_score = 1.0
    score += cur_score
    if abs(cur_score - 1) > 0.0000000000000001:
        msg_list.append(
            'Incorrect cross entropy loss found in Validation Loss. Expected matching accuracy {}, found actual accuracy {}.'.format(
                exp_acc, cur_score))
    num_checks += 1

    if not init_rand:
        assert (isinstance(actual_err_val,
                           (int,
                            float))), 'Incorrect type found for Validation error. Expected int/float, found {}.'.format(
            type(actual_err_val))
        cur_score = abs(expected_err_val - actual_err_val) / (expected_err_val + 0.0000000000000001)
        if cur_score <= tol:
            cur_score = 1.0
        if abs(cur_score) > 1.0 or cur_score < 0:
            cur_score = 0
        score += cur_score
        if abs(cur_score - 1) > 0.000001:
            msg_list.append(
                'Incorrect error rate found in Validation error. \nExpected: \n{}\n\nFound actual: \n{}\n'.format(
                    expected_err_val, actual_err_val))
        num_checks += 1

    # checking labels
    if not init_rand:
        assert (len(expected_y_hat_train) == len(
            actual_y_hat_train)), 'Incorrect length found for Train Labels. \nExpected: \n{}\n\nFound: \n{}\n'.format(
            len(expected_y_hat_train), len(actual_y_hat_train))
        match = check_labels(expected_y_hat_train, actual_y_hat_train)
        cur_score = 0
        if match >= 0.65:
            cur_score = (match - 0.65) / 0.35
        if abs(cur_score - 1) > 0.000001:
            msg_list.append(
                'Incorrect prediction found for Train Labels. Expected matching accuracy {}, found actual accuracy {}.'.format(
                    exp_acc, cur_score))
        num_checks += 1
        score += cur_score

        # assert abs(train_labels_diff) < 0.01, 'Incorrect prediction found for Train Labels. {} labels are predicted incorrectly'.format(train_labels_diff)
        assert (len(expected_y_hat_val) == len(
            actual_y_hat_val)), 'Incorrect length found for Validation Labels. \nExpected: \n{}\n\nFound: \n{}\n'.format(
            len(expected_y_hat_val), len(actual_y_hat_val))
        match_test = check_labels(expected_y_hat_val, actual_y_hat_val)
        cur_score = 0
        if match_test >= 0.65:
            cur_score = (match_test - 0.65) / 0.35
        num_checks += 1
        if abs(cur_score - 1) > 0.000001:
            msg_list.append(
                'Incorrect prediction found for Validation Labels. Expected matching accuracy {}, found actual accuracy {}.'.format(
                    exp_acc, cur_score))
        score += cur_score

    test_score = score / num_checks * max_points

    # test_score = score
    if len(msg_list) == 1:
        test_output = 'PASS\n'
    else:
        test_output = '\n'.join(msg_list)

    return int(test_score), test_output

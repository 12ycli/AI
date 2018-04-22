import numpy as np
import os

def loader():
    training_files = os.listdir('../data/trainingDigits')
    training_inputs = [img2list('../data/trainingDigits/' + file) for file in training_files]
    training_inputs = np.array(training_inputs).T
    training_results = [int(file.split('_')[0]) for file in training_files]
    training_data = [training_inputs,training_results]

    test_files = os.listdir('../data/testDigits')
    test_inputs = [img2list('../data/testDigits/' + file) for file in test_files]
    test_inputs = np.array(test_inputs).T
    test_results = [int(file.split('_')[0]) for file in test_files]
    test_data = [test_inputs, test_results]
    return training_data, test_data


def img2list(filename):
    vector = [0]*1024
    with open(filename) as f:
        for i in range(32):
            line_str = f.readline()
            for j in range(32):
                vector[i*32+j] = int(line_str[j])
    return vector


def vectorized_result(num):
    vector = np.zeros((10,1))
    vector[num] = 1.0
    return vector











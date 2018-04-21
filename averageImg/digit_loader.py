import numpy as np
import os

def loader():
    training_files = os.listdir('../data/trainingDigits')

    training_data = [None]*10
    for i in range(10):
        training_data[i] = [img2list('../data/trainingDigits/' + file) for file in training_files
                            if int(file.split('_')[0]) == i]
        training_data[i] = np.array(training_data[i]).T

    test_files = os.listdir('../data/testDigits')
    test_data = [img2list('../data/testDigits/' + file) for file in test_files]
    test_results = [int(file.split('_')[0]) for file in test_files]
    return training_data,test_data, test_results


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











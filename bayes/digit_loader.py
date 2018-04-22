import numpy as np
import os

def loader():
    training_files = os.listdir('../data/trainingDigits')
    training_results = [int(file.split('_')[0]) for file in training_files]
    # 每个输入向量，后面加多一个结果
    training_data = [img2list('../data/trainingDigits/' + file) for file in training_files]
    for result,data in zip(training_results,training_data):
        data.append(result)

    test_files = os.listdir('../data/testDigits')
    test_inputs = [img2list('../data/testDigits/' + file) for file in test_files]
    test_inputs = test_inputs
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











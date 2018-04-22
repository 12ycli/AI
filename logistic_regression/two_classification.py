# filename:two_classification.py

import my_common
import math
import numpy as np
import matplotlib.pyplot as plt
import digit_loader


class logistic_regression_classification():
    def __init__(self,input,output):
        self.input= input
        self.output = output
        self.theta = np.array([0]*input.shape[0])
        self.step = 0.001

    def training_logistic_regression(self,epoch):
        cost = [self.calc_cost()]
        for i in range(epoch):
            # 这里m省略掉了，因为step就调整后也就一样
            h_x = sigmoid(np.dot(self.input.T, self.theta))
            diff = np.dot(self.input,(h_x - self.output))
            self.theta = self.theta - self.step * diff
            cost.append(self.calc_cost())

        plt.plot(cost)

    @my_common.print_result_after
    def predict(self,input,output):
        cnt = 0
        probability = sigmoid(np.dot(input.T,self.theta))

        predict_0 = np.where(probability < 0.5)
        for item in predict_0[0]:
            # print(type(item))
            # print(item)
            if output[item] == 0:
                cnt += 1

        predict_1 = np.where(probability >= 0.5)
        for item in predict_1[0]:
            if output[item] == 1:
                cnt += 1
        print('{a}-{b}'.format(a=cnt,b=len(output)))
        return float(cnt)/len(output)

    def calc_cost(self):
        h_x = sigmoid(np.dot(self.input.T,self.theta))
        return np.sum((-1)*(self.output*np.log(h_x)+(np.ones(len(self.output)) - self.output)*np.log(np.ones(h_x.shape) - h_x)),axis=0)


# @my_common.print_result_after
def sigmoid(z):
    return 1.0/(1+np.exp(-z))


# 这个例子运行的时候数据集只用2个数字，0和1
def main():
    training_data, test_data = digit_loader.loader()
    classifier = logistic_regression_classification(training_data[0],training_data[1])
    classifier.training_logistic_regression(epoch=200)
    classifier.predict(test_data[0],test_data[1])
    plt.show()


if __name__ == '__main__':
    main()

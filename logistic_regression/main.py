import my_common
import numpy as np
import matplotlib.pyplot as plt
import digit_loader


class logistic_regression_classification():
    def __init__(self,input,output,classes):
        self.input= input
        self.output = output
        self.classes = classes
        self.theta = np.zeros((input.shape[0],classes))
        self.step = 0.0001

    def training_logistic_regression(self,epoch):
        for i in range(self.classes):
            refixed_output = np.where(np.array(self.output)==i,1,0)
            # 判断矩阵是否只有一种类型，全0或者全1，如果是，跳过
            sum = np.sum(refixed_output)
            if sum == 0 or sum == refixed_output.shape[0]:
                continue

            cost = [self.calc_cost(refixed_output,i)]
            for _ in range(epoch):
                # 这里m省略掉了，因为step就调整后也就一样
                h_x = sigmoid(np.dot(self.input.T, self.theta[:,i]))
                diff = np.dot(self.input,(h_x - refixed_output))
                self.theta[:,i] = self.theta[:,i] - self.step * diff
                cost.append(self.calc_cost(refixed_output,i))

            plt.figure(i)
            plt.plot(cost)

    @my_common.print_result_after
    def predict(self,input,output):
        probability = sigmoid(np.dot(input.T,self.theta))
        predict_output = np.argmax(probability,axis=1)
        cnt = 0
        for i in range(len(output)):
            if(predict_output[i]==output[i]):
                cnt += 1
        return float(cnt)/len(output)

    def calc_cost(self,output,i):
        h_x = sigmoid(np.dot(self.input.T,self.theta[:,i]))
        return np.sum((-1)*(output*np.log(h_x)+(np.ones(output.shape) - output)*np.log(np.ones(h_x.shape) - h_x)),axis=0)


# @my_common.print_result_after
def sigmoid(z):
    return 1.0/(1+np.exp(-z))


def main():
    training_data, test_data = digit_loader.loader()
    classifier = logistic_regression_classification(training_data[0],training_data[1],10)
    classifier.training_logistic_regression(epoch=200)
    classifier.predict(test_data[0],test_data[1])
    plt.show()


if __name__ == '__main__':
    main()

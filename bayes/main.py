import math
import digit_loader
import my_common
import numpy as np


class bayes_classfier(object):
    def __init__(self,training_data,num_classes):
        self.num_features = len(training_data[0]) - 1
        self.num_classes = num_classes
        # 防止变成0
        self.model_para = [[1]*(self.num_features) for i in range(self.num_classes)]
        self.classes_probability = [0] * self.num_classes
        self.training_data = training_data

    def train(self):
        # self.classes_probabolity本来是要除以len(self.training_data)的
        # 但大家都要除以，最后比较，不除也可以，后面进一步求概率也刚好
        for training_data in self.training_data:
            self.classes_probability[training_data[-1]] += 1

        # 计总数
        for data in self.training_data:
            for i in range(self.num_features):
                if data[i] == 1:
                    self.model_para[data[-1]][i] += 1

        # 求概率
        for i in range(self.num_classes):
            for j in range(self.num_features):
                self.model_para[i][j] = self.model_para[i][j] / float(self.classes_probability[i])
                try:
                    self.model_para[i][j] = math.log(self.model_para[i][j])
                except:
                    print('error!')

    @my_common.print_result_after
    def test(self,inputs,outputs):
        cnt = 0
        for input,output in zip(inputs,outputs):
            probabilities = [0] * self.num_classes
            for i in range(self.num_classes):
                for feature_j,feature in zip(range(self.num_features),input):
                    if feature == 1:
                        probabilities[i] += self.model_para[i][feature_j]
                probabilities[i] += math.log(self.classes_probability[i])
            result = probabilities.index(max(probabilities))
            if result == output:
                cnt += 1
        return float(cnt)/len(inputs)


def main():
    training_data,test_data = digit_loader.loader()
    classfier = bayes_classfier(training_data,10)
    classfier.train()
    classfier.test(test_data[0],test_data[1])


if __name__ == '__main__':
    main()

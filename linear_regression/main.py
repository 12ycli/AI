import numpy as np
import matplotlib.pyplot as plt


theta_pre_setting = [8,2,-3]

# 梯度下降训练多元线性回归模型
# 输入参数，Data是个矩阵，array类型，m*n，m个样本，n个特征
# 返回值线性系数
def train_linear_regression_model(input,output):
    numOfSamples = input.shape[0]
    numOfFeatures = input.shape[1]
    theta = array([0,0,0]).reshape((-1,1))

    # 每次调整的步伐
    step = 0.0001

    # 记录调整过程代价的变化
    cost_list = []

    i = 0
    while True:
        # 更新theta
        partial_diff = dot(input.T,predict_result(input,theta) - output)/numOfSamples
        theta = theta - step * partial_diff

        # 计算新的代价
        cost = sum(power((predict_result(input,theta) - output),2))

        cost_list.append(cost)

        # if cost < 1:
        #     break

        i += 1
        if i > 10000:
            break

    plt.plot(cost_list)
    plt.show()
    return theta


def predict_result(input,theta):
    return dot(input,theta)


def generate_data(numOfSamples):
    area = np.random.randint(0, 100, size=[numOfSamples,])
    age = np.random.randint(0, 100, size=[numOfSamples,])
    price = calc_price(area, age)

    # 这里reshape((-1,1))用来转置一维向量
    input = np.concatenate([area.reshape((-1, 1)), age.reshape((-1, 1))], axis=1)

    # 为了计算方便在最前面增加多一个特征，恒为1
    temp = np.ones(numOfSamples)
    input = np.concatenate([temp.reshape((-1, 1)), input], axis=1)
    output = price.reshape((-1, 1))

    return input,output


# 测试
def test_data(theta):
    input,output = generate_data(100)
    ret = predict_result(input,theta)

    print('相差小于总体范围1%的准确率为:{a}%'.format(a=len(where(abs(output - ret)<=0.5)[0])))

    # 为了对比预测数据与应该正确产生的数据
    print('对比预测结果与应该产生的结果的对比：')
    ret = concatenate([ret.reshape((-1, 1)), output.reshape((-1, 1))], axis=1)
    print(ret)


def calc_price(area,age,theta = theta_pre_setting):
    return theta[0]+theta[1]*area+theta[2]*age


# 令导数为0的解决方法
def normal_equation(input,output):
    return np.linalg.lstsq(input,output)
    # return np.dot(np.linalg.inv(input),output)


def main():
#     print('数据实际设定的的参数（模型）是：{theta0}、{theta1}、{theta2}'.format(theta0=theta_pre_setting[0],theta1=theta_pre_setting[1],theta2=theta_pre_setting[2]))
#
# # 产生模拟数据
#     numOfSamples = 500
#     input,output = generate_data(numOfSamples)
#
# # 训练模型，得到系数theta
#     theta = train_linear_regression_model(input,output)
#     print('梯度下降计算出来的参数（模型）是：{theta0}、{theta1}、{theta2}'.format(theta0=theta[0],theta1=theta[1],theta2=theta[2]))
#     test_data(theta)
    input,output = generate_data(100)
    theta = normal_equation(input,output)
    print(theta)



if __name__ == '__main__':
    main()

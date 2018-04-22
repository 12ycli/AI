import my_common
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as ani
import random
import copy

# 数据大致范围
_range = 3000


def init():
    fig = plt.figure()
    d1 = np.array(data)[:, 0]
    d2 = np.array(data)[:, 1]
    plt.scatter(d1, d2)

    plt.show()


def generate_data(k,n,data_num):
    '''

    :param k: 聚集点个数
    :param n: 数据维数
    :param data_num: 每个聚居点附近点数
    :return:
    '''

    rate = 0.05
    distance_around_cluster = int(_range * rate)

    data = [[[0]*n for _ in range(data_num)] for __ in range(k)]

    # 随机产生k个中心点
    clusters = np.random.randint(_range,size=(k,n))
    print('随机选中的中心点坐标：{}'.format(clusters.tolist()))
    clusters_ranges = [[0]*n for _ in range(k)]
    for i in range(k):
        for j in range(n):
            clusters_ranges[i][j] = [clusters[i][j] - distance_around_cluster,clusters[i][j] + distance_around_cluster]

    for i in range(k):
        for j in range(data_num):
            for l in range(n):
                data[i][j][l] = random.randint(*clusters_ranges[i][l])

    # 数据降一维，然后打乱
    new_data = []
    for d in data:
        new_data.extend(d)
    random.shuffle(new_data)

    return new_data,clusters


def k_means(k,n,data):
    # 随机产生k个分类点

    clusters = np.random.randint(_range, size=(k, n))

    clusterss = []
    clusterss.append(copy.deepcopy(clusters))

    iter_times = 200
    J = [0.0]*iter_times
    for _ in range(iter_times):

        # 将数据进行分类
        data_in_types = [[] for _ in range(k)]
        for d in data:
            distances = [0]*k
            for i in range(k):
                for j in range(n):
                    distances[i] += (d[j] - clusters[i][j])**2
            min_distance = min(distances)
            data_in_types[distances.index(min_distance)].append(d)
            J[_] += min_distance

        # 移动分类点
        for i in range(k):
            length = len(data_in_types[i])
            if length == 0:
                clusters[i] = np.random.randint(_range, size=(1, n))
            else:
                data_i_type = np.array(data_in_types[i]).T
                clusters[i] = data_i_type.sum(axis=1) / length

        clusterss.append(copy.deepcopy( clusters ))

    return clusterss,J


def main():
    data,random_points = generate_data(3,2,20)
    clusterss,J = k_means(3,2,data)

    print(J)

    plt.figure()
    d1 = np.array(data)[:, 0]
    d2 = np.array(data)[:, 1]
    plt.scatter(d1, d2, c = 'b')

    d1 = np.array(clusterss[-1])[:, 0]
    d2 = np.array(clusterss[-1])[:, 1]
    plt.scatter(d1, d2, c='g')

    d1 = np.array(random_points)[:, 0]
    d2 = np.array(random_points)[:, 1]
    plt.scatter(d1, d2, c='r')



    # 第二张图
    plt.figure()
    plt.plot(J[:10])

    plt.show()


if __name__ == '__main__':
    main()

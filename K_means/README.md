本工程实现了k-means非监督学习算法，基本思路和Ng课程差不多。
实验过程：
1.首先产生k个随机样点，然后再其周围distance_around_cluster = int(_range * rate)的四个方向内产生若干个随机点
2.用k-means算法计算出k个聚集点
3.用图片的形式显示效果。

下面这幅图中蓝色点是待找出结构的点，红点是产生这些蓝点的中心点，绿色是算法计算出来的点，因为随机的因素，绿红蓝点只要接近
就可以说效果非常好了
![描点](https://github.com/12ycli/AI/blob/master/K_means/%E5%AE%9E%E9%AA%8C%E5%9B%BE%E7%89%87/%E6%8F%8F%E7%82%B9.png)

cost-function在算法前十轮的迭代中下降的图示，由于绿色点无法跟每个蓝色的点重合，故最后一定存在不为0，甚至说远大于0的cost-
function
![cost-function](https://github.com/12ycli/AI/blob/master/K_means/%E5%AE%9E%E9%AA%8C%E5%9B%BE%E7%89%87/cost%20function.png)


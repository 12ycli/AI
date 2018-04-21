import my_common
import digit_loader


def calc_averager_img(training_data):
    for i in range(10):
        training_data[i] = training_data[i].sum(axis=1)/float(training_data[i].shape[1])

    return training_data


@my_common.print_result_after
def test_average_method(average_imgs,test_data,test_results):
    cnt = 0
    total_len = len(test_data)

    for i in range(total_len):
        distances = [0] * 10
        for j in range(len(average_imgs)):
            for k in range(1024):
                distances[j] += (test_data[i][k] - average_imgs[j][k])**2

        if distances.index(min(distances)) == test_results[i]:
            cnt += 1

    return cnt/float(total_len)


def main():
    training_data, test_data, test_results = digit_loader.loader()
    average_imgs = calc_averager_img(training_data)
    test_average_method(average_imgs,test_data, test_results)


if __name__ == '__main__':
    main()

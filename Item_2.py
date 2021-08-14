def get_even_num(min_num, max_num):
    """
    :param min_num:
    :param max_num:
    :return:
    """
    res_list =[]
    for x in range(min_num + 1, max_num):
        if x % 2 == 0:
            res_list.append(x)

    print(res_list)



if __name__ == '__main__':
    get_even_num(2,10)



sample_list =[]


def get_multiple_args(*arguments, **keywords):

    for arg in arguments:
        sample_list.append(arg)
    for kw in keywords:
        sample_list.append(keywords[kw])

    str_list = str(sample_list).replace("'", '')
    print(str_list)


if __name__ == '__main__':
    get_multiple_args('HX0001', client='ETarget', courier='Yodel')
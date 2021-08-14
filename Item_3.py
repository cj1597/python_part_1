def get_fibonacci(number):
    """
    :param number:
    :return:
    """
    a, b = 0, 1
    freq = 0
    fib_seq=[]

    while freq < number + 1:
        fib_seq.append(a)
        a, b = b, a + b
        freq += 1
    print(fib_seq)

if __name__ == '__main__':
    get_fibonacci(7)

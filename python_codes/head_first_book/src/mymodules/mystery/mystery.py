def double(arg):
    """ In the function suite a new reference to 'arg' is created, but in the
    code remains the same. """

    print('Before: ', arg)
    arg = arg * 2
    print('After: ', arg)


def change(arg):
    """ The reference to 'arg' remains the same, both in the function suite
    and in the entire code. """

    print('Before: ', arg)
    arg.append('More data')
    print('After: ', arg)

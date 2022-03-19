def is_positive(x):
    try:
        print(x)
        if x <= 0:
            raise (ValueError('non positive number is illegal'))
    except ValueError as err:
        print(err)


x = -1
is_positive(x)

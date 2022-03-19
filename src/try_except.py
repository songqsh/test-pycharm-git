def is_positive(x):
    try:
        print(x**2)
        if x <= 0:
            raise (ValueError('non positive number is illegal'))
    except ValueError as err:
        print(err)
    return x


x = -21
y = is_positive(x)
print(y)

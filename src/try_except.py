def is_positive(x, y):
    try:
        out = x/y
        if out <= 0:
            raise (ValueError('non positive number is illegal'))
    except ValueError as err:
        print(err)
    return out


x = -21
y = 10
z = is_positive(x, y)
print(z)

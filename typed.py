import numpy as np


def typed(*types):
    types_array = np.array(types)

    def decorator(func):
        def wrapper(*args):
            args_array = np.array(args)
            if np.any(np.logical_not(np.vectorize(isinstance)(args_array, types_array))):
                raise TypeError("Arguments do not match expected types")
            func(*args)
        return wrapper
    return decorator


# @typed(int)
# def sum(num):
#     print(num)


# sum(2)
def test(num):
    return num+5


print(np.vectorize(test)([1, 2, 3]))

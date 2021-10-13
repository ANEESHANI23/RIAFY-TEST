def flatten(array):
    if isinstance(array, (list, tuple, set, range)):
        for sub in array:
            yield from flatten(sub)
    else:
        yield array

def myFunc(array, num):
    print(array.count(num))

array = [ [ [1, 2, 3], [1, 2, 3]] , [1, 2, 3], [1, 2, 3]]
array = flatten(array)
myFunc(list(array), 1)
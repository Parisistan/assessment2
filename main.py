
def two_number_sum(numbers, target):

    for x in numbers:
        for y in numbers[numbers.index(x):]:
            if x + y == target and x != y:
                return [x, y]
    return []


# numbers = [4, 17, 3, -10, 0, 6, 20, 11]
# target = 10
# print(two_number_sum(numbers, target))

# version 2
# try:
#     f = open(file.txt)
# not all numbers
# except Exception:
#     print("this file is nowhere to be found!")
# else:
#
# finally:

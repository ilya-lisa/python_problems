__author__ = 'Patrikeev Ilya'

all_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']


def getMaxNumber(n, b):
    return [all_numbers[b - 1]] * n


def subtractOne(digits, b, back_offset=0):
    lastElem = digits[len(digits) - 1 - back_offset]
    if lastElem != 0:
        digits[len(digits) - 1 - back_offset] = all_numbers[all_numbers.index(lastElem) - 1]
    else:
        digits[len(digits) - 1 - back_offset] = all_numbers[b - 1]
        subtractOne(digits, b, back_offset + 1)


def is_zero(digits):
    for d in digits:
        if d != 0:
            return False
    return True


def is_sum_equal(digits_1, digits_2):
    # sums in numeric system with base 10
    sum_1 = 0
    for d in digits_1:
        sum_1 += all_numbers.index(d)

    sum_2 = 0
    for d in digits_2:
        sum_2 += all_numbers.index(d)

    return sum_1 == sum_2


if __name__ == "__main__":
    with open('W:\\input.txt') as f:
        iterator = iter(f)
        next(iterator)
        for data in iterator:
            n, b = [int(c) for c in data.split(' ')]

            if n == 1:
                print(b, end=' ')
                continue

            digits = getMaxNumber(n, b)
            cmp_n = n // 2
            lucky_numbers = 0

            while not is_zero(digits):
                if is_sum_equal(digits[:cmp_n], digits[-cmp_n:]):
                    lucky_numbers += 1

                subtractOne(digits, b)

            # add one to the counter for the zero number
            lucky_numbers += 1
            print(lucky_numbers, end=' ')

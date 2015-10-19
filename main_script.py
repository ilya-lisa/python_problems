from time import time

__author__ = 'Patrikeev Ilya'

all_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']


def get_max_number(numbers, base):
    return [all_numbers[base - 1]] * numbers


def subtract_one(digits, base, back_offset=0):
    last_elem = digits[len(digits) - 1 - back_offset]
    if last_elem != 0:
        digits[len(digits) - 1 - back_offset] = all_numbers[get_index_of(last_elem) - 1]
    else:
        digits[len(digits) - 1 - back_offset] = all_numbers[base - 1]
        subtract_one(digits, base, back_offset + 1)


def get_index_of(number):
    # if number < 10:
    #     return number
    # else:
        return all_numbers.index(number)


def is_zero(digs):
    for d in digs:
        if d != 0:
            return False
    return True


def calc_sum(digits):
    # sums in numeric system with base 10
    result = 0
    for d in digits:
        result += get_index_of(d)
    return result


def init_sum_array(sums, digits):
    while not is_zero(digits):
        sums.append(calc_sum(digits))
        subtract_one(digits, b)
    sums.append(0)
    sums.sort()


if __name__ == "__main__":
    with open('W:\\input.txt') as f:
        iterator = iter(f)
        cases = int(next(iterator))
        start = time()
        results = ""
        for data in iterator:
            n, b = [int(c) for c in data.split(' ')]

            if n == 1:
                results += str(b) + " "
                continue

            digits = get_max_number(n, b)
            cmp_n = n // 2
            lucky_numbers = 0

            sums = []
            initStart = time()
            init_sum_array(sums, digits[0:cmp_n])
            print("initializing sum array is done in " + str(round(time() - initStart, 2)))
            result = 0
            row = 1
            prev = sums[0]
            for n in range(1, len(sums)):
                if sums[n] == prev:
                    row += 1
                elif row == 1:
                    result += 1
                else:
                    result += row * row
                    row = 1
                prev = sums[n]
            # add one to the counter for the number of zeros
            result += 1
            results += str(result) + " "
        print()
        print("running time: " + str(round(time() - start, 2)))
        print("\n" + results)

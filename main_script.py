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


def add_value(value_map, key, value):
    if key in value_map:
        value_map[key] += value
    else:
        value_map[key] = value


def init_start_data(sums, digits):
    while not is_zero(digits):
        add_value(sums, sum(digits), 1)
        subtract_one(digits, b)
    sums['0'] = 1


def init_sum_array(digits, b):
    slice = 4
    sums = {}
    if len(digits) < slice:
        init_start_data(sums, digits)
        return sums
    else:
        start_data = {}
        init_start_data(start_data, digits[:slice])
        sums = {k: v for k, v in start_data.items()}
        temp1 = start_data
        temp2 = {}

        for d in range(0, len(digits) - slice):
            for i in range(0, get_index_of(b)):
                for k, v in temp1.items():
                    new_value = int(k) + i
                    add_value(sums, new_value, v)
                    add_value(temp2, new_value, v)

            temp1 = temp2
            temp2 = {}
        return sums

if __name__ == "__main__":
    with open('W:\\input.txt') as f:
        n, b = [int(c) for c in f.readline().split(' ')]

        if n == 1:
            print(b)
        else:
            digits = get_max_number(n, b)
            cmp_n = n // 2
            factor = 1 if n % 2 == 0 else b

            initStart = time()
            sums = init_sum_array(digits[0:cmp_n], b)
            print("initializing sum array is done in " + str(round(time() - initStart, 2)))

            result = 0
            for value in sums.values():
                result += value * value

            result *= factor
            print(result)

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
    if number < 10:
        return number
    else:
        return all_numbers.index(number)


def is_zero(digs):
    for d in digs:
        if d != 0:
            return False
    return True


def is_sum_equal(digits_1, digits_2):
    # sums in numeric system with base 10
    sum_1 = 0
    for d in digits_1:
        sum_1 += get_index_of(d)

    sum_2 = 0
    for d in digits_2:
        sum_2 += get_index_of(d)

    return sum_1 == sum_2


if __name__ == "__main__":
    with open('W:\\input.txt') as f:
        iterator = iter(f)
        cases = int(next(iterator))
        start = time()
        current = 1
        result = ""
        for data in iterator:
            innerStart = time()
            n, b = [int(c) for c in data.split(' ')]

            if n == 1:
                result += str(b) + " "
                print("case " + str(current) + " from " + str(cases) + " finished in " + str(round(time() - innerStart, 2)))
                current += 1
                continue

            digits = get_max_number(n, b)
            cmp_n = n // 2
            lucky_numbers = 0
            while not is_zero(digits):
                if is_sum_equal(digits[:cmp_n], digits[-cmp_n:]):
                    lucky_numbers += 1

                subtract_one(digits, b)

            # add one to the counter for the number of zeros
            lucky_numbers += 1
            result += str(lucky_numbers) + " "
            print("case " + str(current) + " from " + str(cases) + " finished in " + str(round(time() - innerStart, 2)))
            current+=1
        print()
        print("running time: " + str(round(time() - start, 2)))
        print("\n" + result)


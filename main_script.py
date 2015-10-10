
__author__ = 'Patrikeev Ilya'

if __name__ == "__main__":
    with open('W:\\input.txt') as f:
        iterator = iter(f)
        next(iterator)
        times = next(iterator).split()
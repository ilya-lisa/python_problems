import math

__author__ = 'Patrikeev Ilya'

START_X = 10
START_Y = 10


def calcCoordinates(start_x, start_y, angle, radius):
    x1 = start_x + (math.cos(angle) * radius)
    y1 = start_y + (math.sin(angle) * radius)
    return str(x1) + ' ' + str(y1)


def getHourAngle(h):
    return h % 12 * 360 / 12


def getMinuteAngle(m):
    return m * 360 / 60


def gradToRad(grad):
    return grad * math.pi / 180


if __name__ == "__main__":
    with open('W:\\input.txt') as f:
        iterator = iter(f)
        next(iterator)
        for time in next(iterator).split():
            splitted = time.split(':')
            hours = splitted[0]
            minutes = splitted[1]
            print(calcCoordinates(START_X, START_Y, float(gradToRad(float(getHourAngle(int(hours))))), 6), end=' ')
            print(calcCoordinates(START_X, START_Y, float(gradToRad(float(getMinuteAngle(int(minutes))))), 9), end=' ')

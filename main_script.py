import math

__author__ = 'Patrikeev Ilya'

START_X = 10
START_Y = 10


def calcCoordinates(start_x, start_y, angle, radius):
    x1 = start_x + (math.cos(angle) * radius)
    y1 = start_y + (math.sin(angle) * radius)
    return str(x1) + ' ' + str(y1)


def getHourAngle(h, m):
    return (360 + (90 - (h % 12 * 360 / 12))) % 360 - (360 / 12 * m / 60)


def getMinuteAngle(m):
    return (360 + (90 - (m * 360 / 60))) % 360


def gradToRad(grad):
    return grad * math.pi / 180


if __name__ == "__main__":
    with open('W:\\input.txt') as f:
        iterator = iter(f)
        next(iterator)
        times = next(iterator).split()
        for time in times:
            splitted = time.split(':')
            hours = splitted[0]
            minutes = splitted[1]
            print(calcCoordinates(START_X, START_Y, gradToRad(float(getHourAngle(int(hours), int(minutes)))), 6), end=' ')
            print(calcCoordinates(START_X, START_Y, gradToRad(float(getMinuteAngle(int(minutes)))), 9), end=' ')

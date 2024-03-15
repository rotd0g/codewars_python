"""
Description
Imagine a city where the streets are perfectly laid out to form an infinite square grid. In this city finding the shortest path between two given points (an origin and a destination) is much easier than in other more complex cities. Your task is to create an algorithm that does the following calculation.

Given user's departure and destination coordinates, each of them located on some street, find the length of the shortest route between them assuming that cars can only move along the streets. Each street can be represented as a straight line defined by the x = n or y = n formula, where n is an integer.
Example
For departure = [0.4, 1] and destination = [0.9, 3], the output should be perfectCity(departure, destination) = 2.7.
0.6 + 2 + 0.1 = 2.7, which is the answer.
Guaranties
An array [x, y] of x and y coordinates. It is guaranteed that at least one coordinate is integer.
0.0 ≤ departure[i] ≤ 10.0.
0.0 ≤ destination[i] ≤ 10.0.
Result shoud be in format xx.x(0.0, 2.3, 4.5, 6.0, 23.0)
"""

def perfectCity(departure, destination):
    # def x
    # def y
    # if x dest >x depa: move right: x depa + to int, x dest - to int
    # if x dest < x depa: move left: x depa - to int, x dest + to int
    # if y dest > y depa: move up: y departure + int, y dest - to int
    # if y dest < y depa: move down: y departure - int, y dest + to int
    # for integer part take abs(delta)
    # sum deltas for overall result

    result = 00.0
    xdepa, ydepa = departure
    print(xdepa, ydepa)
    xdest, ydest = destination
    # delta_ints = abs(int(xdest) - int(xdepa))
    #XXXX
    if int(xdest) != int(xdepa):
        result += abs(xdest-xdepa)
    else:
        x_float_sum = (xdepa - int(xdepa)) + (xdest - int(xdest))
        if ydest == ydepa:
            result += abs(xdest - xdepa)
        elif x_float_sum > 1:
            #move right
            result += 2 - x_float_sum
        elif x_float_sum <=1:
            #move left
            result += x_float_sum
    #YYYY
    if int(ydest) != int(ydepa):
        result += abs(ydest-ydepa)
    else:
        y_float_sum = (ydepa - int(ydepa)) + (ydest - int(ydest))
        if xdest == xdepa:
            result += abs(ydest - ydepa)
        elif y_float_sum > 1:
            #move up
            result += 2 - y_float_sum
        elif x_float_sum <=1:
            #move down
            result += y_float_sum

    return result

print(perfectCity([0.4, 1], [0.9, 3]))

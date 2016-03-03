#i did some monte carlo simulations in college but have since forgotten a lot and want to make sure i can still
#understand the concepts : )

import random

def montecarlopi(datapointsinsimulation):
    """use 1 as the radius of a circle, which will also be the side of (1/4 of) the square,
    and takes as an arg the amount of data wanted to be in the simulation
    note: will look at 1/4 of the square and circle because it's easier"""
    #pi will come from the ratio of the square's area and circle's area:
    #circle = (pi*r^2)/4
    #square = (r^2)
    #since r != 0 --> pi = 4*circle/r^2 = 4*circle/ square
    circlepoints = 0
    squarepoints = 0
    radius = 1
    while squarepoints < datapointsinsimulation:
        x = random.random()
        y = random.random()
        distance = (x**2 + y**2)**0.5
        #print squarepoints, x, y, distance
        if distance <= radius:
            circlepoints += 1
        else:
            pass
        squarepoints += 1
    ratio = 4*float(circlepoints)/float(squarepoints)
    return ratio

if __name__ == "__main__":
    #print montecarlopi(25)
    #print montecarlopi(100)
    #print montecarlopi(1000)
    print montecarlopi(10000)
    #ex results - 3.172, 3.1332, 3.134

import sys
import math

# This code automatically collects game data in an infinite loop.
# It uses the standard input to place data into the game variables such as x and y.
# YOU DO NOT NEED TO MODIFY THE INITIALIZATION OF THE GAME VARIABLES.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def distance(self, newPoint):
        dist = ((self.x - newPoint.x) ** 2 + (self.y - newPoint.y) ** 2)**(1/2)
        return dist
        
class Pod:
    def __init__(self, location, destination, angle):
        self.location = location
        self.destination = destination
        self.distance = self.location.distance(destination)
        self.power = 0
        self.angle = angle
        
    def get_power(self):
        if self.angle > 90 or self.angle < -90:
            self.power = 0
        else:
            self.power = 'BOOST'# Change this to 100 in lower leagues
            
    def update(self, location, destination, angle):
        self.location = location
        self.destination = destination
        self.distance = self.location.distance(destination)
        self.angle = angle
        
    def print_move(self):
        self.get_power()
        print('{} {} {}'.format(self.destination.x, self.destination.y, self.power))
        
        
random = Point(0, 0)
my_pod = Pod(random, random, 0)
opp_pod = Pod(random, random, 0)
# game loop
while True:
    # x: x position of your pod
    # y: y position of your pod
    # next_checkpoint_x: x position of the next check point
    # next_checkpoint_y: y position of the next check point
    x, y, next_checkpoint_x, next_checkpoint_y, nextDist, nextAngle = [int(i) for i in input().split()]
    oppX, oppY = [int(i)for i in input().split()]
    
    source = Point(x, y)
    target = Point(next_checkpoint_x, next_checkpoint_y)
    oppSource = Point(oppX, oppY)
    
    my_pod.update(source, target, nextAngle)
    my_pod.print_move()
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)


    # Edit this line to output the target position
    # and thrust (0 <= thrust <= 100)


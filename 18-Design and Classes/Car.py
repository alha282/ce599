"""
Create a yellow car.  Move the yellow car forward two units, turn left, move forward one space. 
Create a green car.  Turn left.  Move forward one space.  Turn right.  Move forward two spaces. 
Print both cars. 
 
 Usage: 
 
    python Car.py
  
 e.g.
 
    python Car.py 2
 
"""
---------------------------------------------------------------------------------------------------

# general imports first
import sys

class Car(object):
    def __init__(self, color, direction, location):
        if len(location)<2 or len(location)>2: 
            print('The location of the car is the x,y coordinates')
        else:
            self.color = color
            self.location = location
            self.x = location[0]
            self.y = location[1]
            self.direction = direction

            
    def go(self, units):
        if self.direction == 'North':
            self.y = self.y + units
        elif self.direction == 'South':
            self.y = self.y - units
        elif self.direction == 'East':
            self.x = self.x + units
        elif self.direction == 'West':
            self.x = self.x - units
        else:
            print('North, South, East & West')
    
    def right_turn(self):
        if self.direction == 'North':
            self.direction ='East'
        elif self.direction == 'East':
            self.direction = 'South'
        elif self.direction == 'South':
            self.direction = 'West'
        elif self.direction == 'West':
            self.direction = 'North'
        else:
            print ('Wrong Way')
            
    def left_turn(self):
        if self.direction == 'North':
            self.direction = 'West'
        elif self.direction == 'West':
            self.direction = 'South'
        elif self.direction == 'South':
            self.direction = 'East'
        elif self.direction == 'East':
            self.direction = 'North'
        else:
            print ('Wrong Way')

    def car_print(c):
        print('The' , str(c.color), 'car is headed' , str(c.direction) 
              , 'and located at position' , (c.x, c.y))
        
#----------------------------------------------------------------------------------------------------
# Main function call. 
#----------------------------------------------------------------------------------------------------
if __name__ == "__main__":        
    car1 = Car(color = 'yellow', location =[0,0], direction = 'North')
    car2 = Car(color = 'green', location = [0,0], direction = 'North')

    car1.go(units = 2)
    car1.left_turn()
    car1.go(1)

    car2.left_turn()
    car2.go(1)
    car2.right_turn()
    car2.go(2)

    car_print(car1)
    car_print(car2)
class Robot:
    def __init__(self, name, colour, weight):#This is a contructor
        self.name=name
        self.colour=colour
        self.weight=weight
    def introduceSelf(self):
        print('My name is ' + self.name)#Note that self is a method of class.
        print('My colour is '+self.colour)
        print('My weight is',self.weight)
#---------------Object Creation------------#
r1 = Robot('Tom','red',30)
r2=Robot('Jerry','blue',40)
#-----------------Robot 1------------------#
r1.name='Tom'
r1.colour='red'
r1.weight=30
r1.x=1
#-----------------Robot 2---------------------#
r2.name="Jerry"
r2.colour='blue'
r2.weight=40
r2.x=2
#----------------method execution-------------#
r1.introduceSelf()
r2.introduceSelf()
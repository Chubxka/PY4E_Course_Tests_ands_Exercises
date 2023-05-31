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
#r1.name='Tom'
#r1.colour='red'
#r1.weight=30
#r1.x=1
#-----------------Robot 2---------------------#
#r2.name="Jerry"
#r2.colour='blue'
#r2.weight=40
#r2.x=2
#----------------method execution-------------#


class person:
    def __init__(self,n,p,i):#method one of linking objects is to set a further argument in the constructor which allows to link the robot to the person
        self.name=n
        self.personality=p
        self.isSitting=i
    
    def sit_down(self):
        self.isSitting=True
    def stand_up(self):
        self.isSitting=False

    def introduceSelf(self):
        print('My name is ', self.name)
        print("I'm a person who's", self.personality)
        print('My robot is', self.robotOwned)

p1=person('Alice','aggressive',False)
p2=person('Becky','talkative',True)

#Methiod 2 of linking object

p1.robotOwned=r2
p2.robotOwned=r1

p1.robotOwned.introduceSelf()
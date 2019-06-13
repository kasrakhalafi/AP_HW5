import random
import math

########### TO FIND TO BE INSIDE CIRCLE OR NOT#############

def IsInCircle(x, y):
    if math.pow(x,2) + math.pow(y,2) <= 1:
        print("Inside of circle")
    else:
        print("outside of circle")

############# CALLING INCIRCLE FUCTION ####################

IsInCircle(0.5,0.6)

############# FOR FINDING BEST NUMBER #####################

def find():
    for i in range(1000000):
        bestNum(random.uniform(-1, 1), random.uniform(-1, 1))


def static_var(varname, value):#this function is used for static numbers
    def decorate(func):
        setattr(func, varname, value)
        return func
    return decorate


@static_var("counter1", 0)
@static_var("counter2", 0)
def bestNum(x, y):     #like the isincicle function but for finding the best number
    bestNum.counter1 += 1
    pi = 4 * bestNum.counter2 / bestNum.counter1
    if pi > math.pi*.99 and pi< math.pi*1.01:
        print("this is our pi: {:.5f}".format(pi))
        print("finded number is: {}".format(bestNum.counter1))
        exit()
    if math.pow(x, 2) + math.pow(y, 2) <= 1:
        bestNum.counter2 += 1

####################CALLING THE FIND FUNCTION ##############

find()



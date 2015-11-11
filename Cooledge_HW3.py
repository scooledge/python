#Samuel Cooledge
#csc 110 sec 08
#April 27 2015
#Program calculates buoancy of a sphere/cube

#Import math
import math

#Declare global variables
gravity = 9.81
density = 999.97
volWater = 1/3

#Set up main function
def main():
    #Intro
    print("So you think you can float? let's see:")

    #Gather user input
    radius = float(input("please input radius of sphere:"))
    length = float(input("please input length of cube:"))
    width = float(input("please input width of cube:"))
    height = float(input("please input height of cube:"))

    #Perform calculations (processing)
    cubeVolume = myCube(height, width, length)
    sphereVol = mySphere(radius)
    buoySphere = myBuoancy(sphereVol)
    buoyCube = myOtherBuoancy(cubeVolume)

    #Output section of input info and calculations, formatted to 4 decimal places and configured to cubic meters and newtons
    print('cube volume is:', format(cubeVolume,",.4f"), "cubic meters")
    print('sphere volume is:',format(sphereVol,",.4f"),"cubic meters")
    print('buoancy of sphere is:', format(buoySphere,",.4f"),"newtons")
    print('buoancy of cube is:', format(buoyCube,",.4f"),"newtons")


    #Volume of cube = height*width*length
    #function myCube has input info for height, width, and length. myCube calls on cubeVolume which multiplies those inputs
    #returns answer for cubeVolume
def myCube(height, width, length):
    cubeVolume = height*width*length
    return cubeVolume
    
    #Volume of sphere = (4/3)*math.pi*(radius**3)
    #Function mySphere calls for radius, asked for in input under main().
    #Mysphere calls on sphereVol equation with radius input
    #returns volume of sphere
    
def mySphere(radius):
    sphereVol = ((4/3)*math.pi*(radius**3))
    return sphereVol

    #Calls for buoancy of sphere using volume obtained from previous function mySphere
    #Function myBuoancy uses sphereVol as a return function, inputs that information into equation for buoancy of a sphere
    #calculation completed and returned for call in main for print
def myBuoancy(sphereVol):
    buoySphere = (sphereVol*density*gravity*volWater)
    return buoySphere

    #Calls for buoancy of cube using previous function that obtained volume of cube
    #Calculates buoancy using volume of cube
    #outputs that equation with return buoycube
def myOtherBuoancy(cubeVolume):
    buoyCube = (cubeVolume*density*gravity*volWater)
    return buoyCube

main()

# TEST CASE #1:
# Radius of sphere: .5 , Length of cube: 2 , Width of cube: 2 , Height of cube: 2 
# Expected volume of cube : 8 cubic meters
# Expected volume of sphere : 0.5236 cubic meters
# Expected buoancy of sphere : 1,712.1166 newtons
# Expected buoancy of cube : 26,159.2152 newtons
# Result : PASS

# TEST CASE #2:
# Radius of sphere: 6, Length of cube: 3.5 , Width of cube: 6.5 , Height of cube: 7.9 
# Expected volume of cube : 179.7250 cubic meters
# Expected volume of sphere : 904.7787 cubic meters
# Expected buoancy of sphere : 2,958,537.5387 newtons
# Expected buoancy of cube : 587,683.1190 newtons
# Result : PASS

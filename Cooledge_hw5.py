#Samuel Cooledge
#csc 110 sec 08
#may 12 2015

#program that offers discounts on various food selections depending on what size of sandwich



#several print statements that introduce you to program
print("Welcome to Sam's Sandwhich Shop")
print("We have several deals: 1.) Small : $5.99")
print("                       2.) Medium : Buy one for $9.99; get the second for $5.99")
print("                       3.) Large : $20.99 per sandwich. Buy 3 or more and get 10% off your bill!")
print("                       4.) Jumbo : $29.99 per sandwich. Any sandwich bought after the 4th will be 50% off")

#user input section also happens to set the global variables, how_many is set to an integer using int
size = input("please enter the size of sandwich you would like: ")
how_many = int(input("how many sandwiches would you like:"))
tax = float(.095)
tax_inc = float(1.095)

#if/else statement that makes it so the user has to input a whole positive number
if (how_many <= 0 ):
    print("that is impossible, are you gonna order a sandwich or not?")
else:
# continues only if the user has entered a whole positive number, then sets it to uppercase. program works regardless of upper or lower   
    sandwich_size = size.upper()
    if((sandwich_size != "S") and (sandwich_size != "M") and (sandwich_size != "L") and (sandwich_size != "J")):
        print("WHOA no need to get angry")
        
def main(): #first and main function, takes user size and calls corresponding function, depending on function called, example small() it then calculates for a small sandwich
    sandwich(size)
    if (sandwich_size == "S"):
        small()
    elif (sandwich_size == "M"):
        medium()
    elif (sandwich_size == "L"):
        large()
    else:
        jumbo()
        
def sandwich(size):#function determindes size. depending size it gets put thru a series of elif's in main()and begins output statements
    if ( how_many == 1): #parameter: size
        if (size == "s"):
            print("you want", how_many, "small sandwich? that will be:" )
        
        elif (size == "m"):
            print ("you want", how_many, "medium sandwiches?, cool. Can you give me a few minutes?:")

        elif (size == "l"):
            print("you want,", how_many, "large sandwiches?, ok dokay give me a few minutes:")

        else:
            print("you want,", how_many, "jumbo sandwiches?, cool beans, give me a few minutes please:")
    else:
        if (size == "s"):
            print("you want", how_many, "small sandwich? that will be:" )
        
        elif (size == "m"):
            print ("you want", how_many, "medium sandwiches?, cool. Can you give me a few minutes?:")

        elif (size == "l"):
            print("you want,", how_many, "large sandwiches?, ok dokay give me a few minutes:")

        else:
            print("you want,", how_many, "jumbo sandwiches?, cool beans, give me a few minutes please:")
# each of the following functions uses global variables input by user , calculates , and then outputs information!

#calculation section. depending on size and how many sandwiches. user input is forwarded to main(), at this point main()calls next function depending elif condition it fulfills
def small(): #function calcutes information regarding small sandwiches, outputs info
    if (how_many >= 1): 
        s = float(5.99*how_many,)
        print("total before tax is:","$", format(s,".2f"))
        print("your tax is:","$",float(format(5.99*tax,".2f")))#calculates and displays tax
        print("your total is:","$",format(s,".2f"))#calculates and displays total cost
    
def medium(): #if parameter is 1 it runs first if statement
    if (how_many == 1):
        m = float(9.99*how_many)
        print("before tax your order cost is: " , "$", format(m,".2f")) #calculates cost before tax
        print("your tax is:","$",float(format(m*tax,".2f")))#calculates and displays tax
        print("your total is:","$",format(m*tax_inc,".2f"))#calculates and displays total cost including tax
    elif (how_many % 2 == 0): #elif parameter is an even number of sandwiches sized medium, it calculates accordingly 
        m = float(9.99*(how_many/2)+5.99*(how_many/2))
        print("the price of your order before tax is:", "$" , format(m,".2f")) #calculates cost before tax
        print("your tax is:","$", float(format(m*tax,".2f"))) #calculates and displays tax
        print("Your total order including tax is","$",(format(m*tax_inc, ".2f")))#calculates and displays total cost including tax
    else:
        m = float((9.99*(how_many-1)/2)+5.99*((how_many-1)/2)+9.99)#calculates buy one get one half off discount
        print("the price of your order before tax is: ","$", format(m,".2f"))#calculates cost before tax
        print("your tax is: ","$", float(format(m*tax,".2f"))) #calculates and displays tax
        print("Your total order including tax is","$",(format(m*tax_inc, ".2f"))) #calculates and displays total cost including tax
        
def large():
    if (how_many <=3): #determines if user input is less or equal to three
        l = float(20.99*how_many) #if less than or equal to three it proceeds with calculation and output
        print("before tax, your order will cost: ","$", l)#calculates cost before tax
        print("tax for your order is: ","$", float(format(l*tax, ".2f")))#calculates and displays tax
        print("total cost of your order including tax is: ","$",format(l*tax_inc,".2f"))#calculates and displays total cost including tax
    elif (how_many >= 3):
        l = float(20.99*how_many*.9)#if input is great than or equal to three it proceeds with calculation; specific calculation determines a 10  percent discount if how_many is greater than 3
        print("before tax your order will cost: " ,"$",format(l,".2f"))#calculates cost before tax
        print("tax:","$",format(l*tax,".2f"))#calculates and displays tax
        print("total cost of your order including tax is: ","$",format(l*tax_inc,".2f"))#calculates and displays total cost including tax

def jumbo():
    if (how_many <= 4):#if input is less than or equal to four it proceeds with below calculation and output
        j = float(29.99*how_many)
        print("before tax, your order will cost: ","$",format(j,".2f"))#calculates cost before tax
        print("tax for your order is: ","$", format(j*tax, ".2f"))#calculates and displays tax
        print("total cost of your order including tax is: ","$",format(j*tax_inc,".2f"))#calculates and displays total cost including tax
        
    elif (how_many >= 5): #if input is greater than/equal to 5. proceeds with calculation
        j = float((29.99*4)+((how_many-4)*29.99)*.5) #this equation determines cost of sandwich after 4 have already been input
        print("before tax, your order will cost: ","$",format(j,".2f"))#calculates cost before tax
        print("tax for your order is: ","$", format(j*tax,".2f"))#calculates and displays tax
        print("total cost of your order including tax is: ","$",format(j*tax_inc,".2f"))#calculates and displays total cost including tax

main()

#Test sample
#1.) User input global variable what size: M
#    User input global variable how many: 6
#    Expected result: before tax : $ 47.94
#                            tax : $ 4.55
#                     total cost : $ 52.49
#2.)
#    User input global variable what size: j
#    User input global variable how many: 5
#    Expected result: before tax : $ 134.95
#                            tax : $ 12.82
#                     total cost : $ 147.78


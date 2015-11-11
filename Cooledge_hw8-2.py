#Samuel Cooledge
#june 11 2015
#csc 110 HW 8

def wordSearch():
    
    a = [] #create an empty list


    addWords = input("would you like to enter a word? (y/n):") #asks for words to search y/n; if yes begins first iteration

    while(addWords != "n"): # first iteration
        words = input("please enter your word:") #user input
        a.append(str.lower(words)) #sets it to lower case
        print(a)
        addWords = input("would you like to enter a word? (y/n)")

        if addWords == "n":
            print("ok you have no more words you would like to enter in your search")

    print(a) #print word list for transparency 
    

    file2search = open("jurassic.txt","r") #open up file "jurassic.txt" and reads it (jurassic.txt contains the synopsis for new Jurassic World movie)
    file = open("hw8.txt","w")
    myJurassic = str.lower(file2search.read()) 
    

    for i in range(0,len(a)): #for statement runs and searches all strings in list
        search = myJurassic.find(a[i]) #search is index
        counter = 0

        if search == -1: #if search is -1 then there is no match
            file.write('0' + " " + a[i] + "\n")

        else:
            while search != -1: #finds match with all occurances. 
                counter += 1
                search = myJurassic.find(a[i], search + 1)
            file.write(str(counter)+ " " + a[i]+ "\n")
    
    file.close()
    file2search.close()

def main():
    wordSearch()

main()

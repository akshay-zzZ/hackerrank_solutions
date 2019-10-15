from random import *
running = True 
adjective = ["awesome "," confident "," smart "," superb "," sexy "] 
hobby = [" cooking "," bike riding "," programming "," public speaking "," vella he tu"] 
print("complement generator ")


print(" - - - - - - - - - - - - - - - ")
name = input("what is your name :")

print('''
	 menu 
       c = get compliment 
       d = delete a hobby 
       a = add a hobby 
       p = printhobby
       q = quit
        ''') 

while running == True :
	inputchoice = input("\n^_").lower()
	if inputchoice == c :
		print("here is your compliment ", name,":")
		print(name," you are", choice(adjective), "at", choice(hobby))
		
	elif inputchoice == d :
		inputchoice = input("enter a hobby to delete:")
		hobby.remove(inputchoice)
		
	elif inputchoice == a :
		inputchoice = input("please add a hobby :")
		hobby.append(inputchoice)
		
	elif inputchoice == p:
		print(hobby)
	
	elif inputchoice == q :
		running = false 
		
	else :
		print("error")
    
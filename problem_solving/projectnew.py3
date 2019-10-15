import sys
#running = TRUE 
print("poems of your choice ")
print("---------------------")

name = input(" enter your name")
print("Dear ", name," you have to choose from the following keywords ")
print('''
	keywords 
	 eyes
	 moon
	 peace
	 happiness 
	 twinke
	 Johnny_jhonny
	 black_sheep
	 starts
	 away
	 father_father
	 my_mother 
	'''
	)

inputkeywords = input().split()
print(inputkeywords)
for i in range(inputkeywords):
    if inputkeywords[0] == eyes :
        open eyes.txt
    
#print("Enter how many words you want in your poem")
#numberofwords = int(input())




    
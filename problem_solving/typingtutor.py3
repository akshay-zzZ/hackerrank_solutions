import  time
import os

""""
t0 provide splash scrren in beggining and
to display input file and
 give prompt to typing in
 """

class color:

	RED = '\033[91m'
	GREEN = '\033[92m'
	BLUE = '\033[94m'
	CRAYN = '\033[96m'
	WHITE = '\033[97m'
	YELLOW = '\033[93m'
	MAGENTA = '\033[95m'
	BLACK = '\033[90m'
	DEFAULT = '\033[99m'


def splashscreen():
	# it will splash the screen for 5 seconds
	print(color.RED + "welcome to the typing tutor 1.0 by Alfaij Mansuri" + color.MAGENTA)
	time.sleep(5)
	os.system("clear")


def displaycontentof(a):
	# to dispay content of file
	try:
		with open("a.txt" , 'r') as f:
			print(color.BLUE + f.read() + color.DEFAULT)
			print(color.MAGENTA + "\nTYPE_THE__GIVEN_ABOVE_TEXT" + color.DEFAULT)
	except:
		print(color.YELLOW + "ERROR FILE NOT" + color.CRAYN)

def takeinput():
	#create a new file for user input
	with open("userinput.txt" , 'w') as userinput:
		while(True):
			curline = input()
			if (curline == "#end"):
						break
			userinput.write(curline + "\n")

#provide analysis to users


def analyse(totaltime):

	totype = open("bc.txt", "r")
	correctlist = totype.read().replace("\n", " ").split(" ")
	userinput = open("userinput.txt" , "r")
	enteredlist = userinput.read().replace("\n"," ").split(" ")

	#starting incorect form -1 to compensate from last #end
	incorrect = -1

    #here least function is used to avoid out bound errors
	leastrange = min(len(enteredlist),len(correctlist))

	for i in range(leastrange):
		if(correctlist[i] == enteredlist[i]):
			print(color.YELLOW + enteredlist[i] + color.RED, end=" ")
		else:
			print(color.MAGENTA + enteredlist[i] + color.DEFAULT,end=" ")
			incorrect += 1
		if i%10 == 0 and i != 0:
			print()

		difference = abs(len(enteredlist)- len(correctlist) + 1)
		incorrect += difference

		if(len(enteredlist) < len(correctlist) - 1):
			for i in range(difference , len(correctlist)):
				print(color.CRAYN + correctlist[i] + color.GREEN,end=" ")
				if i%10 ==0 and i !=0 :
					print()

		print(color.GREEN + "\n Showing status in 5 sec" + color.BLUE)
		time.sleep(5)
		os.system("clear")
		accuracypercent = ((len(correctlist) - incorrect) / len(correctlist)*100)
		print(color.MAGENTA + "________________________" + color.GREEN)
		print(color.MAGENTA + "________________________" + color.GREEN)
		print("Accuracy : ",accuracypercent,"%")
		print("Words per min :", len(enteredlist)/(totaltime/60))
		print(color.GREEN + " ________________________" + color.MAGENTA)
		print(color.GREEN + " ________________________" + color.MAGENTA)


#MAIN PROGRAMME

splashscreen()
displaycontentof("b.txt")

#recoed string time
startingtime = time.time()

takeinput()
#calculate total time
finaltime = time.time()
totaltime = finaltime - startingtime
analyse(totaltime)

numOfLevels = int(input("Enter the number of levels: "))

for x in range((numOfLevels)+1):
	#print(" "*(x+1), "*"*(x), " "*x, " "*(int(x/2)), end="")
	#print("\n")
	#print()
	#numOfLevels -= 1
	print(" "*(numOfLevels-x), "* "*x)
value = input("Enter Fib Squence Index: ")

listThing = [0,1]
satisfied = False
"""
for x in range(len(value)):
	listThing.append(listThing[x]+listThing[x+1])
	"""
x=0
counter = 0
while counter != 100000:
	listThing.append(listThing[x]+listThing[x+1])
	x +=1
	#print(listThing, len(listThing))
	counter+=1
print(listThing[int(value)])
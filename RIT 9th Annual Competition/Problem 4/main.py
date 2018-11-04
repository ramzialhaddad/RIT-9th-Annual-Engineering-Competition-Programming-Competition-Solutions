inputString = input("Enter the Compressed String: ")
strings = []
multipliers = []
end = []
for x in inputString:
	if not x.isalpha():
		multipliers.append(x)
	else:
		strings.append(x)

for x in range(len(multipliers)):
	for y in range(int(multipliers[x])): 
		end.append(strings[x])

for z in end:
	print(z,end="")
#print(end)
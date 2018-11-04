shiftValue = int(input("Enter the shift value 1-25: "))
unencryptedText = input("Enter the text: ")
alpahbet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
endString=[]

for x in range(len(unencryptedText)):
	if unencryptedText[x] != ' ':
		endString.append(alpahbet[alpahbet.index(unencryptedText[x])+shiftValue])

for x in endString:
	print(x, end="")
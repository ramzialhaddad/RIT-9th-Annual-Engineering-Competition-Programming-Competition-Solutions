with open(str(input("Enter filename: ")), "r") as file:
	text = file.read()
counter = 0
for x in text:
	if x != " ":
		counter += 1
print("Number of Characters: ", counter)
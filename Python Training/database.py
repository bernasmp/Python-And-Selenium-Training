def main():
	personList = [0]
	programOn = True
	numberOfPeople = 0
	firstPerson = True

	while programOn:
		command = input("\n Command --> ")
		if command == "Print":
			print("\n List of People Inserted:")
			for person in personList:
				print(person)
		elif command == "Insert":
			personInfo = [0]*3
			personInfo[0] = input("Enter person name: ")
			personInfo[1] = input("Enter person age: ")
			personInfo[2] = input("Enter person country: ")

			if firstPerson:
				personList[0] = personInfo
				firstPerson = False
			else:
				personList.append(personInfo)

			print("\n <<Person Info Inserted>> \n")

if 1==1:
	main()
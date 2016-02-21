from notes_application import NotesApplication

# command line section
author = input("Enter name of author: ")
noteObject = NotesApplication(author)
userInput = None
while userInput != 0:
	userInput = int(input("\n\n" +
		               "Enter 1 to create note.\n" +
		               "Enter 2 to list all notes.\n" +
		               "Enter 3 to get a specific note.\n" +
		               "Enter 4 to search for all notes for a particular string.\n" +
		               "Enter 5 to delete a specific note.\n" +
		               "Enter 6 to edit a specific note.\n" +
		               "Enter 0 to exit Application.\n\n>>> "
	                 ))

	if userInput == 1:
		methodArgument = input("Enter new content:")
		noteObject.create(methodArgument)
	elif userInput == 2:
		noteObject.list()
	elif userInput == 3:
		methodArgument = input("Enter index for the specific note you want from the list: ")
		noteObject.get(int(methodArgument))
	elif userInput == 4:
		methodArgument = input("Enter your search string: ")
		noteObject.search(methodArgument)
	elif userInput == 5:
		methodArgument = input("What is the index of the note you want to remove: ")
		noteObject.delete(int(methodArgument))
	elif userInput == 6:
		methodArgumentOne = input("What is the index of the note you want to remove: ")
		methodArgumentTwo = input("What do you want to replace it with: ")
		noteObject.edit(int(methodArgumentOne), methodArgumentTwo)
	elif userInput == 0:
		print ("You have successfully exited the Application")
	else:
		print ("You entered an invalid input.")
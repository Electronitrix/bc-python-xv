class NotesApplication(object):
	""" Defines attributes and methods for managing a note application.

	Keyword atrributes:
	self.author -- string represents object's author
	self.notes -- list holds all notes by author
	"""

	def __init__(self, author):
		""" Initializes object.

		Keyword Aguments:
		author -- a string that represents author of note
		"""
		self.author = author
		self.notes = []

	def create(self, note_content):
		""" Creates and adds a new note to self.notes attribute.
		
		Keyword Arguments:
		note_content -- a string containing the new note to be added
		"""
		self.notes.append(note_content)

	def list(self):
		""" Prints each content of the object according to defined format."""
		for i in range(len(self.notes)):
			print("Note ID: %s" %(i))
			print(self.notes[i])
			print("\n\nBy Author %s" %(self.author))

	def get(self, note_id):
		""" Retrieves a specific note based on supplied note_id

		Keyword arguments:
		note_id -- points to the item on self.notes to be retrieved
		Returns:
		Specified item on self.note
		"""
		numOfNotes = len(self.notes)
		if numOfNotes == 0:
			print("You have not saved any notes")
		elif note_id >= 0 and note_id < numOfNotes:
			return "{}".format(self.notes[note_id])
		else:
			print("The index you entered does not exist")

	def search(self, search_text):
		""" 
		Searches self.note for occurrence search string and prints all matches.

		Keyword arguments:
		search_text -- the string to look for
		"""
		found = False
		for i in range(len(self.notes)):
			if search_text in self.notes[i]:
				print("Note ID: %s" %(i))
				print(self.notes[i])
				print("\n\nBy Author %s" %(self.author))
				found = True
		if not found:
			print("NO MATCH FOUND!!!")

	def delete(self, note_id):
		""" Deletes a note from self.notes

		Keyword arguments:
		note_id -- integer points to the item on self.notes to be retrieved
		"""
		self.notes.pop(note_id)

	def edit(self, note_id, new_content):
		""" Replaces an item in self.notes located at note_id with new_content

		Keyword arguments:
		note_id -- integer points to the item on self.notes to be retrieved
		new_content - a string containing the new note to be added
		"""
		self.notes[note_id] = new_content
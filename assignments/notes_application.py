class NotesApplication(object):
	def __init__(self, author):
		self.author = author
		self.notes = []

	def create(self, note_content):
		self.notes.append(note_content)

	def list(self):
		for i in range(len(self.notes)):
			print ("Note ID: %s" %(i))
			print (self.notes[i])

			print ("\n\nBy Author %s" %(self.author))

	def get(self, note_id):
		numOfNotes = len(self.notes)
		if numOfNotes == 0:
			print ("You have not saved any notes")
		elif note_id >= 0 and note_id < numOfNotes:
			return "{}".format(self.notes[note_id])
		else:
			print ("The index you entered does not exist")

	def search(self, search_text):
		found = False
		for i in range(len(self.notes)):
			if search_text in self.notes[i]:
				print ("Note ID: %s" %(i))
				print (self.notes[i])

				print ("\n\nBy Author %s" %(self.author))
				found = True

		if not found:
			print ("NO MATCH FOUND!!!")

	def delete(self, note_id):
		self.notes.pop(note_id)

	def edit(self, note_id, new_content):
		self.notes[note_id] = new_content
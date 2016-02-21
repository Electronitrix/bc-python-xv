import unittest
import sys
from notes_application import NotesApplication
from notes_application_context_manager import capture

class NotesApplicationTestSuite(unittest.TestCase):
    def test_NotesApplication_instance(self):
        erika = NotesApplication("Erika")
        self.assertIsInstance(erika, NotesApplication, msg="The object should be an instance of the 'NotesApplication' class")

    def test_object_type(self):
        erika = NotesApplication("Erika")
        self.assertTrue((type(erika) is NotesApplication), msg="The object should be a type of 'NotesApplication'")

    def test_create_one_note(self):
        erika = NotesApplication("Erika")
        erika.create("Black Justice")
        self.assertEqual(["Black Justice"], erika.notes, msg="The class should have a create method adds its argument to a property called notes")

    def test_create_two_notes(self):
        erika = NotesApplication("Erika")
        erika.create("Black Justice")
        erika.create("Erasmus")
        self.assertEqual(["Black Justice", "Erasmus"], erika.notes, 
                          msg="The create method should add multiple notes to the same 'notes' property")

    def test_create_three_notes(self):
        erika = NotesApplication("Erika")
        erika.create("Black Justice")
        erika.create("Erasmus")
        erika.create("Elixir")
        self.assertEqual(["Black Justice", "Erasmus", "Elixir"], erika.notes, 
                          msg="The create method should add multiple notes to the same 'notes' property")

    def test_list_empty_note_list(self):
        erika = NotesApplication("Erika")
        with capture(erika.list) as output:
            self.assertEqual("", output,
                              msg="The note_list should be empty until you create a list with the create method")

    def test_list_one_note_in_notes(self):
        erika = NotesApplication("Erika")
        erika.create("Black Justice")
        appOutput = "Note ID: 0\nBlack Justice\n\n\nBy Author Erika\n"
        with capture(erika.list) as output:
            self.assertEqual(appOutput, output, msg="The list method should print according to the specified format")

    def test_list_five_notes_in_notes(self):
        erika = NotesApplication("Erika")
        erika.create("Black Justice")
        erika.create("Erasmus")
        erika.create("Elixir")
        erika.create("Manchi")
        erika.create("Ultron")
        appOutput = ("Note ID: 0\nBlack Justice\n\n\nBy Author Erika\n"
                     "Note ID: 1\nErasmus\n\n\nBy Author Erika\n"
                     "Note ID: 2\nElixir\n\n\nBy Author Erika\n"
                     "Note ID: 3\nManchi\n\n\nBy Author Erika\n"
                     "Note ID: 4\nUltron\n\n\nBy Author Erika\n"
                    )
        with capture(erika.list) as output:
            self.assertEqual(appOutput, output, msg="The list method should print according to the specified format")

    def test_list_notes_of_digits(self):
        erika = NotesApplication("Erika")
        erika.create(1)
        erika.create(2)
        erika.create(3)
        appOutput = ("Note ID: 0\n1\n\n\nBy Author Erika\n"
                     "Note ID: 1\n2\n\n\nBy Author Erika\n"
                     "Note ID: 2\n3\n\n\nBy Author Erika\n"
                    )
        with capture(erika.list) as output:
            self.assertEqual(appOutput, output, msg="List method doesn't handle a note list of only digits well")

    def test_list_notes_of_digits_and_numbers(self):
        erika = NotesApplication("Erika")
        erika.create("Tripping")
        erika.create(1)
        erika.create(2)
        erika.create("Ultron")
        erika.create("Ultimatio")
        erika.create(3)
        erika.create("Thoughts are random")
        appOutput = ("Note ID: 0\nTripping\n\n\nBy Author Erika\n"
                     "Note ID: 1\n1\n\n\nBy Author Erika\n"
                     "Note ID: 2\n2\n\n\nBy Author Erika\n"
                     "Note ID: 3\nUltron\n\n\nBy Author Erika\n"
                     "Note ID: 4\nUltimatio\n\n\nBy Author Erika\n"
                     "Note ID: 5\n3\n\n\nBy Author Erika\n"
                     "Note ID: 6\nThoughts are random\n\n\nBy Author Erika\n"                     
                    )
        with capture(erika.list) as output:
            self.assertEqual(appOutput, output, msg="List method does not handle a note list that has a combination of numbers well")

    def test_get_note_from_begining(self):
        erika = NotesApplication("Erika")
        erika.create("Black Justice")
        self.assertEqual("Black Justice", erika.get(0), msg="get() method does not return the right value at 0 index")

    def test_get_note_from_end(self):
        erika = NotesApplication("Erika")
        erika.create("Tripping")
        erika.create(1)
        erika.create(2)
        erika.create("Ultron")
        erika.create("Ultimatio")
        erika.create(3)
        erika.create("Thoughts are random")
        self.assertEqual("Thoughts are random", erika.get(6), msg="get() method does not return the right value at the last index")

    def test_get_note_from_mid(self):
        erika = NotesApplication("Erika")
        erika.create(1)
        erika.create(2)
        erika.create("Ultron")
        erika.create("Ultimatio")
        erika.create(3)
        erika.create("Thoughts are random")
        self.assertEqual("Ultimatio", erika.get(3), msg="get() method does not return the right value within the list")

    def test_get_with_nonexistent_index(self):
        erika = NotesApplication("Erika")
        erika.create("Tripping")
        erika.create(1)
        erika.create(4)
        appOutput = "The index you entered does not exist\n"
        with capture(erika.get, 8) as output:
            self.assertEqual(appOutput, output, msg="get() method does not handle entry of invalid indices appropriately")

    def test_get_note_from_empty_notes(self):
        erika = NotesApplication("Erika")
        appOutput = "You have not saved any notes\n"
        with capture(erika.get, 0) as output:
            self.assertEqual(appOutput, output, msg="get() method is supposed to warn user that the note list is empty")

    def test_search_finds_matches(self):
        erika = NotesApplication("Erika")
        erika.create("Black Justice")
        appOutput = ("Note ID: 0\nBlack Justice\n\n\nBy Author Erika\n")
        with capture(erika.search, "Justice") as output:
            self.assertEqual(appOutput, output, msg="search() method does not find matches")

    def test_search_handles_non_matches(self):
        erika = NotesApplication("Erika")
        erika.create("Black Justice")
        appOutput = ("NO MATCH FOUND!!!\n")
        with capture(erika.search, "Erika") as output:
            self.assertEqual(appOutput, output, msg="search() method does not handle non matches")

    def test_search_finds_multiple_matches(self):
        erika = NotesApplication("Erika")
        erika.create("Reality")
        erika.create("Merciless giver")
        erika.create("Real studio")
        appOutput = ("Note ID: 0\nReality\n\n\nBy Author Erika\n"
                     "Note ID: 2\nReal studio\n\n\nBy Author Erika\n"
                    )
        with capture(erika.search, "Real") as output:
            self.assertEqual(appOutput, output, msg="search() method does not find multiple matches")

    def test_delete_note(self):
        erika = NotesApplication("Erika")
        erika.create("Reality")
        erika.create("Merciless giver")
        erika.create("Real studio")
        appOutput = ("Note ID: 0\nReality\n\n\nBy Author Erika\n"
                     "Note ID: 1\nReal studio\n\n\nBy Author Erika\n"
                    )
        erika.delete(1)
        with capture(erika.list) as output:
            self.assertEqual(appOutput, output, msg="delete() method does not delete the note specified by index")

    def test_edit_note(self):
        erika = NotesApplication("Erika")
        erika.create("Reality")
        erika.create("Merciless giver")
        erika.create("Real studio")
        appOutput = ("Note ID: 0\nReality\n\n\nBy Author Erika\n"
                     "Note ID: 1\nElixir\n\n\nBy Author Erika\n"
                     "Note ID: 2\nReal studio\n\n\nBy Author Erika\n"
                    )
        erika.edit(1, "Elixir")
        with capture(erika.list) as output:
            self.assertEqual(appOutput, output, msg="edit() method does not edit note specified by index")

if __name__ == "__main__":
    unittest.main()
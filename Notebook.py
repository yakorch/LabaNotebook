"""A module for a Notebook class"""

import sys
import datetime
ind = 0


class Note:
    """A Note class, contains record and tags to be serached by"""
    def __init__(self, memo, tags=''):
        """
        Initializes a class. Each note is unique by its index.
        >>> note = Note("You, coward, are afraind to live but not to suffer")
        >>> record = Note("We have two lives, and the second begins when we realize we only have one")
        >>> note.ind == record.ind
        False
        >>> note.memo
        'You, coward, are afraind to live but not to suffer'
        """
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global ind
        ind += 1
        self.ind = ind

    def match(self, match):
        """
        Checks if a note contains 'match' string in text or tags.
        >>> note = Note("You, coward, are afraind to live but not to suffer")
        >>> record = Note("We have two lives, and the second begins when we realize we only have one")
        >>> note.match('coward')
        True
        >>> record.match('coward')
        False
        >>> record.match('lives')
        True
        >>> note.match("")
        True
        """
        if match in self.memo or match in self.tags:
            return True
        return False


class Notebook:
    """Notebook class, contains notes, changes and finds them"""
    def __init__(self):
        """
        Initializes a class.
        """
        self.notes = []

    def new_note(self, memo, tags=''):
        """
        Appends one note to notes list
        """
        self.notes.append(Note(memo, tags))

    # def modify_memo(self, note_ind, memo):
    #     '''Find the note with the given ind and change its
    #     memo to the given value.'''
    #     for note in self.notes:
    #         if note.ind == note_ind:
    #             note.memo = memo
    #             break

    def modify_tags(self, note_ind, tags):
        """
        Changes tags in a note, if found.
        """
        for note in self.notes:
            if note.ind == note_ind:
                note.tags = tags
                break

    def search(self, match):
        """
        Returns the list of all notes that match criteria ('match' in a note).
        """
        return [note for note in self.notes if note.match(match)]

    def _find_note(self, note_ind):
        """
        Returns a note by its index if found
        """
        print(note_ind)
        for note in self.notes:
            if note.ind == int(note_ind):
                return note

    def modify_memo(self, note_ind, memo):
        """
        Finds a note and changes it content.
        """
        note = self._find_note(note_ind)
        if note:
            note.memo = memo
        else:
            print("Invalid id. Possible ids:", [el.ind for el in self.notes])


class Menu:
    """Menu class that responds to user's whims"""

    def __init__(self):
        """
        Returns a method by user's choice
        """
        self.notebook = Notebook()
        self.choices = {
            "1": self.show_notes,
            "2": self.search_notes,
            "3": self.add_note,
            "4": self.modify_note,
            "5": self.quit
        }

    def display_menu(self):
        """
        Offers a choice for a user.
        """
        print("""
        Notebook Menu
        1. Show all Notes
        2. Search Notes
        3. Add Note
        4. Modify Note
        5. Quit
        """)

    def run(self):
        """
        Converts user's response to a command. Recalls itself if invalind input
        """
        self.display_menu()
        choice = input("Enter an option: ")
        action = self.choices.get(choice)
        if action:
            action()
            self.run()
        else:
            print("{0} is not a valind choice".format(choice))
            self.run()

    def show_notes(self, notes=None):
        """
        Prints the notes.
        """
        if not notes:
            notes = self.notebook.notes
        for note in notes:
            print(f"{note.ind}: {note.tags}\n{note.memo}")

    def search_notes(self):
        """
        Shows all notes that match user's will.
        """
        match = input("Search for: ")
        notes = self.notebook.search(match)
        self.show_notes(notes)

    def add_note(self):
        """
        Adds a notation to the Notebook.
        """
        memo = input("Enter a memo: ")
        self.notebook.new_note(memo)
        print("The note has been added.")

    def modify_note(self):
        """
        Changes the note by its index.
        """
        ind = input("Enter a note ind: ")
        memo = input("Enter a memo: ")
        tags = input("Enter tags: ")
        if memo:
            self.notebook.modify_memo(ind, memo)
        if tags:
            self.notebook.modify_tags(ind, tags)

    def quit(self):
        """
        The end of fun :( 
        """
        print("The program has finished")
        sys.exit(0)


if __name__ == "__main__":
    Menu().run()

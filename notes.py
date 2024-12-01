import os
import sys


os.chdir("C:/")
try:
    os.mkdir("Notes")
except FileExistsError:
    os.chdir("C:/Notes")
notes = []
filenames = os.listdir("C:/Notes")
for item in filenames:
    notes.append(item)

print("Notes app v0.1")
print("type 'help' to see all commands")
print()



while True:
    inp = input("> ")
    if inp == "help":
        print()
        print("New - creates a new note.")
        print("View - view all notes")
        print("Open (note_name) - views note contents.")
        print("Edit (note_name) - edit note contents.")
        print("Delete (note_name) - delete note.")
        print("Exit - exits the program.")
        print()

    elif inp == "new":
        name = input("Name: ")
        try:
            fileCreate = open(name + ".txt", "x")
            print("File created.")
            notes.append(name)
            fileCreate.close()
            print()
        except FileExistsError:
            print("A file with that name already exists.")
            print()
        except PermissionError:
            print("An error occurred creating the file.")
            print()

    elif inp == "view":
        print()
        for item in notes:
            print(item)
        print()

    elif inp.startswith("open "):
        print()
        noteName = inp[5:]
        try:
            note = open(noteName + ".txt", "r")
            print(note.read())
            note.close()
        except FileNotFoundError:
            print("Note does not exist.")
        print()

    elif inp.startswith("edit "):
        print()
        noteName = inp[5:]
        try:
            note = open(noteName + ".txt", "w")
            contents = input("Note contents: ")
            note.write(contents)
            print("Notes updated.")
            note.close()
        except FileNotFoundError:
            print("Note does not exist.")
        print()

    elif inp.startswith("delete "):
        print()
        noteName = inp[7:]
        try:
            os.remove(noteName + ".txt")
            print("Note deleted.")
        except FileNotFoundError:
            print("Note does not exist.")
        print()

    elif inp == "exit":
        sys.exit()

    else:
        print("INVALID COMMAND IDIOT!!!!🔥🔥🔥🔥🔥")
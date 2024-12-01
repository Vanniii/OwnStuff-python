import os
import sys
import socket


print("Python Terminal v0.6")
print("'help' to list commands!")
print()


while True:
    currentDir = os.getcwd()
    cmd = input(currentDir + "> ")


    if cmd == "help":
        print()
        print("DIRECTORY CONTROL - help-dir")
        print("SYSTEM CONTROL - help-sys")
        print("TOOLS - help-tool")
        print("exit - Exits the program.")
        print()

    elif cmd == "help-dir":
        print()
        print("DIRECTORY CONTROL")
        print("cd - Change Directory")
        print("cd/ - Root Directory")
        print("dir - View Directory Contents")
        print("mkdir - Create a New Directory")
        print("ren - Rename Directory")
        print("del - Delete File")
        print("rd - Delete Directory")
        print()

    elif cmd == "help-sys":
        print()
        print("SYSTEM CONTROL")
        print("hostname - get hostname of PC")
        print("ip -  get ip of PC")
        print("shutdown - shutdown PC")
        print("restart - restart PC")
        print()

    elif cmd == "help-tool":
        print()
        print("Coming Soon!")
        print()





    elif cmd.startswith("cd "):
        directory = cmd[3:]
        try:
            os.chdir(directory)
        except FileNotFoundError:
            print("Directory not found.")
            print()

    elif cmd == "cd/":
        drive = currentDir.split(":")[0] + "://"
        os.chdir(drive)

    elif cmd == "dir":
        print()
        contents = os.listdir(currentDir)
        for item in contents:
            print(item)
        print()

    elif cmd.startswith("mkdir "):
        print()
        name = cmd[6:]
        try:
            os.mkdir(name)
            print("Directory " + name + " created.")
        except FileExistsError:
            print("A file or directory with that name already exists.")
        except FileNotFoundError:
            print("There was an error creating the directory.")
        except PermissionError:
            print("The program does not have permission to create a directory.")
        except OSError:
            print("There was an error creating the directory.")
        print()

    elif cmd.startswith("ren "):
        print()
        try:
            directory = cmd[4:].split(", ")
            oldDir = directory[0]
            newDir = directory[1]
            try:
                os.rename(oldDir, newDir)
                print("Renamed " + oldDir + " to " + newDir + ".")
            except FileNotFoundError:
                print("That file does not exist.")
            except FileExistsError:
                print("A file or directory with that name already exists.")
            except PermissionError:
                print("The program does not have permission to rename the directory.")
            except OSError:
                print("There was an error renaming the file.")
        except IndexError:
            print("Invalid format. Use format 'ren (old name), (new name)'")
        print()

    elif cmd.startswith("del "):
        print()
        filename = cmd[4:]
        try:
            os.remove(filename)
            print("Deleted " + filename + ".")
        except FileNotFoundError:
            print("A file with that name was not found.")
        except PermissionError:
            print("The program does not have permission to delete the file.")
        except OSError:
            print("There was an error deleting the file.")

    elif cmd.startswith("rd "):
        print()
        directory = cmd[3:]
        try:
            os.rmdir(directory)
            print("Removed " + directory + ".")
        except FileNotFoundError:
            print("A directory with that name was not found.")
        except PermissionError:
            print("The program does not have permission to remove the directory.")
        except OSError:
            print("There was an error removing the directory.")

    elif cmd == "hostname":
        print()
        print(socket.gethostname())
        print()

    elif cmd == "ip":
        print()
        print(socket.gethostbyname(socket.gethostname()))
        print()

    elif cmd == "shutdown":
        os.system("shutdown /s /t 0")
    elif cmd == "restart":
        os.system("shutdown /r /t 0")

    elif cmd == "exit":
        sys.exit()
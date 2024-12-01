print("To-Do In Python! v0.2")
print()


todo = []


print("Commands: "
      "add (taskname) - adds a task  | "
      "del (taskname) - removes a task | "
      "clear - removes all tasks | "
      "view - view task list |")
print()


while True:
    inp = input("> ")

    if inp.startswith("add "):
        name = inp[4:]
        todo.append(name)
        print("Added " + name)
        print()
        continue

    elif inp.startswith("del "):
        name = inp[4:]
        isExist = name in todo
        if not isExist:
            print("No such task.")
            print()
            continue
        else:
            todo.remove(name)
            print("Deleted " + name)
            print()
            continue


    elif inp == "clear":
        confirm = input("Are you sure you want to clear all tasks? (y/n) ")
        if confirm.lower() == "y":
            todo.clear()
            print("All tasks are cleared")
            print()
            continue
        else:
            print("Cancelled.")
            print()
            continue

    elif inp == "view":
        for item in todo:
            print(item)
        print()
        continue

    else:
        print("Invalid input.")
        print()
        continue
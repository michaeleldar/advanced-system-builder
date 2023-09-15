from os import listdir, system
import json


def choose_config():
    files = listdir(".")
    newfiles = []
    for file in files:
        if file.startswith("n"):
            newfiles.append(file)

    print("Choose your configuration by number: ")
    x = 1
    for file in newfiles:
        data = json.loads(open(file).read())
        print(f"{x}: {data['name']}")
        x += 1
    answer = input("What is your choice?")
    y = 1
    for file in newfiles:
        if y == int(answer):
            data = json.loads(open(file).read())
            for item in data["install"]["packages"]:
                system(f"sudo pacman -S {item} --no-confirm")
        y += 1


choose_config()

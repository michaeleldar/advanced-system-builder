print("Welcome to the Advanced System Builder!")
import urllib.request
from os import system, listdir
import json


def curl(url):
    response = urllib.request.urlopen(url)
    data = response.read()
    text = data.decode("utf-8")
    return text


def main_menu():
    print("Chose an option by specifying the number:")
    print("1. Use a configuration from a repository")
    print("2. Use a configuration from a file")
    choice = input("Make your choice: ")
    if choice == "1":
        repo_menu()
    elif choice == "2":
        file_menu()
    else:
        main_menu()


def repo_menu():
    x = 1
    repos = open("repos.txt").read().splitlines()
    for repo in repos:
        configs = curl(repo).splitlines()
        for config in configs:
            c = curl(config)
            d = open(f"n{x}.py", "w")
            d.write(c)
            choose_config()
            x += 1


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
                system(f"sudo pacman -S {item} --noconfirm")
        y += 1


def file_menu():
    file = open(input("Enter the name of your config file: ")).read()
    d = open(f"n.py", "w")
    d.write(file)
    system(f"python3 n.py")


main_menu()

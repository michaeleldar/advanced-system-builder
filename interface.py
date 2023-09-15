print("Welcome to the Advanced System Builder!")
import urllib.request
from os import system


def curl(url):
    response = urllib.request.urlopen(url)
    data = response.read()
    text = data.decode("utf-8")
    return text


def main_menu():
    while True:
        print("Chose an option by specifying the number:")
        print("1. Use a configuration from a repository")
        print("2. Use a configuration from a file")
        choice = input("Make your choice: ")
        if choice == "1":
            repo_menu()
            break
        elif choice == "2":
            file_menu()
            break


def repo_menu():
    x = 1
    repos = open("repos.txt").read().splitlines()
    for repo in repos:
        configs = curl(repo).splitlines()
        for config in configs:
            c = curl(config)
            d = open(f"n{x}.py", "w")
            d.write(c)
            system(f"python3 n{x}.py")

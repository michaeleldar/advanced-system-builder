from os import system


def cinstall(package):
    system(f"sudo pacman -S {package}")

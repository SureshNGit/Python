#!/usr/bin/env python3
"""
file=open("UsefulCommands.txt")
print(file.readline())
print(file.read())
file.close

with open("UsefulCommands.txt") as file:
    print(file.read())


with open("UsefulCommands.txt") as file:
    for line in file:
        print(line)

with open("UsefulCommands.txt") as file:
    for line in file:
        print(line.strip())

with open("UsefulCommands.txt") as file:
    for line in file:
        print(line.strip().upper())

file=open("UsefulCommands.txt")
line=file.readlines()
file.close
print(line)
line.sort()
print(line)

"""

with open("fileWrite.txt","w") as file:
    file.write("Hello World!!! How are you?")

with open("fileWrite.txt","a") as file:
    file.write("May TN gets rain thrice a month...")

with open("fileWrite.txt","r") as file:
    print(file.readlines())

import os

print(os.path.exists("fileWrite.txt"))
os.rename("fileWrite.txt","fileWrite-Renamed.txt")

with open("fileWrite-Renamed.txt") as file:
    print(file.readlines())

print("File size= "+ str(os.path.getsize("fileWrite-Renamed.txt")))

print("File modified timestamp= "+ str(os.path.getmtime("fileWrite-Renamed.txt")))

import datetime

ts = os.path.getmtime("fileWrite-Renamed.txt")
print(datetime.datetime.fromtimestamp(ts))

print("Absolute file path= "+ os.path.abspath("fileWrite-Renamed.txt"))

os.remove("fileWrite-Renamed.txt")
print(os.path.exists("fileWrite-Renamed.txt"))







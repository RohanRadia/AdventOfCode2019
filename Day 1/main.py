import os
import sys

# Procedure is:
# (Round Down(Initial number / 3))-2

masses = []

file = input("File name: ")

with open(file, "r") as f:
    for line in f:
        masses.append(line.split("\n")[0])

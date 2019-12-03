# Procedure is:
# (Round Down(Initial number / 3))-2

fuel = 0
extra_req = 0

file = input("File name: ")

with open(file, "r") as f:
    for line in f:
        extra_req = (int((int(line.split("\n")[0]))/3))-2

        while extra_req > 0:
            fuel += extra_req

            extra_req = (int(extra_req/3))-2

print(f"Fuel needed: {fuel}")

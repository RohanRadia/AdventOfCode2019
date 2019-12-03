# 1; Add together inputs
# 2; Multiplies inputs 
# 99; Halt

commands = []
opcode = 0

while commands[opcode] != 99:
    
    if commands[opcode] == 1:
        commands[commands[opcode+3]] = commands[commands[opcode+1]] + commands[commands[opcode+2]]

    elif commands[opcode] == 2:
        commands[commands[opcode+3]] = commands[commands[opcode+1]] * commands[commands[opcode+2]]

    else:
        print("Error, not a valid opcode!")

    opcode += 4

print(f"Position 0 containts: {commands[0]}")


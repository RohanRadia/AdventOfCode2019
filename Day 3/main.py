moves = [['R3', 'U5'], ['U2', 'R6']]
positions = []
distances = []

def run(moveset):
    mapped = [['o']]
    current_x = 0
    current_y = 0
    for moves in moveset:
        for a in range(len(mapped)):
            for b in range(len(mapped[0])):
                if mapped[a][b] == 'o':
                     current_y = a
                     current_x = b
                
        for move in moves:
            if move[0] == 'L':
                for step in range(1, int(move[1:])+1):
                    try:
                        if mapped[current_y][current_x+1] == '-':
                            mapped[current_y][current_x+1] == 'X'
                        elif mapped[current_y][current_x+1] == 'o':
                            pass
                        elif mapped[current_y][current_x+1] == 'X':
                            pass
                        else:
                            mapped[current_y][current_x+1] = '-'
                    except:
                        mapped[current_y].append('-')
                    finally:
                        current_x += 1

                for layer in mapped:
                    while len(layer) < len(mapped[current_y]):
                        layer.append('.')

            elif move[0] == 'R':
                for step in range(1, int(move[1:])+1):
                    if current_x == 0:
                        mapped[current_y].insert(0, '-')
                    else: 
                        if mapped[current_y][current_x-1] == '-':
                            mapped[current_y][current_x-1] = 'X'
                        elif mapped[current_y][current_x-1] == 'o':
                            pass
                        elif mapped[current_y][current_x-1] == 'X':
                            pass
                        else:
                            mapped[current_y][current_x-1] = '-'

                    if current_x != 0:
                        current_x -= 1

                for layer in mapped:
                    while len(layer) < len(mapped[current_y]):
                        layer.insert(0, '.')
                            
            elif move[0] == 'U':
                for step in range(1, int(move[1:])+1):
                    if current_y == len(mapped)-1:
                        mapped.append([])
                        for i in range(len(mapped[0])):
                            mapped[len(mapped)-1].append('.')
                            
                        current_y += 1
                        
                        if mapped[current_y][current_x] == '-':
                            mapped[current_y][current_x] = 'X'
                        elif mapped[current_y][current_x] == 'X':
                            pass
                        elif mapped[current_y][current_x] == 'o':
                            pass
                        else:
                            mapped[current_y][current_x] = '-'

                    else:
                        current_y += 1
                        mapped[current_y][current_x] = '-'
                    

            elif move[0] == 'D':
                for step in range(1, int(move[1:])+1):
                    if current_y == 0:
                        mapped.insert(0, [])
                        for i in range(len(mapped[1])):
                            mapped[0].append('.')
                    else:
                        current_y -= 1
                    
                    #you can just add these things below
                    if mapped[current_y][current_x] == '-':
                        mapped[current_y][current_x] = 'X'
                    elif mapped[current_y][current_x] == 'X':
                        pass
                    elif mapped[current_y][current_x] == 'o':
                        pass
                    else:
                        mapped[current_y][current_x] = '-'

    return mapped


output = run(moves)

for y in range(len(output)):
    for x in range(len(output[0])):
        if output[y][x] == 'o':
            positions.append([y, x])
            distances.append([y, x])
            
for y in range(len(output)):
    for x in range(len(output[0])):
        if output[y][x] == 'X':
            positions.append([y, x])

for intersect in range(1, len(positions)):
    val1 = 0
    val2 = 0
    if positions[intersect][0] > positions[0][0]:
        val1 = positions[intersect][0] - positions[0][0]
    else:
        val1 = positions[0][0] - positions[intersect][0]
    if positions[intersect][1] > positions[0][1]:
        val2 = positions[intersect][1] - positions[0][1]
    else:
        val2 = positions[0][1] - positions[intersect][1]
    distances.append(val1 + val2)

smallest = distances[1]
for dist in range(1, len(distances)):
    if distances[dist] < smallest:
        smallest = distances[dist]

for map in output:
    print(map)

print(f'Closest intersect: {smallest}')

grid, count, won = [['-' for i in range(7)] for j in range(6)], 0, False
while not won:
    print("\n".join(" ".join(line) for line in reversed(grid)))
    loc = int(input(f"{['x','0'][count]}'s turn "))
    (grid[[grid[i][loc-1] for i in range(6)].index('-')][loc-1], count) = ('x', 1) if count == 0 else ('0', 0)

    
